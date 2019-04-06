install.packages("foreign")

library(foreign)
library(dplyr)
library(ggplot2)
library(readxl)

raw_welfare <- read.spss(file = "Koweps_hpc10_2015_beta1.sav", to.data.frame=T)
welfare <- raw_welfare

head(welfare)
tail(welfare)
View(welfare)
dim(welfare)
str(welfare)
summary(welfare)

welfare <- rename(welfare, sex=h10_g3, birth=h10_g4,
                  marriage=h10_g10, religion=h10_g11,
                  income=p1002_8aq1, code_job=h10_eco9,
                  code_region=h10_reg7)

#9-2

table(welfare$sex)
welfare$sex <- ifelse(welfare$sex == 1, "male", "female")
summary(welfare$income)
qplot(welfare$income)+xlim(0,1000)

welfare$income <- ifelse(welfare$income %in% c(0, 9999), NA, welfare$income)
table(is.na(welfare$income))

sex_income <- welfare %>% filter(!is.na(income)) %>% group_by(sex) %>%
  summarise(mean_income = mean(income)) %>%
  select(sex, mean_income)

ggplot(welfare %>% filter(!is.na(income)) %>% group_by(sex) %>%
         summarise(mean_income = mean(income)) %>%
         select(sex, mean_income), aes(x=sex, y=mean_income))+geom_col()

ggplot(sex_income, aes(x=sex, y=mean_income))+geom_col()

#9-3

table(is.na(welfare$birth))

welfare$age <- 2015 - welfare$birth + 1
table(welfare$age)
summary(welfare$age)

age_income <- welfare %>% filter(!is.na(income)) %>%
  group_by(age) %>%
  summarise(mean_income=mean(income)) %>%
  select(age,mean_income)

ggplot(age_income, aes(x=age, y=mean_income))+geom_line()

#9-4

welfare$ageg <- ifelse(welfare$age<30,'young',ifelse(welfare$age<60, 'middle','old') )
table(welfare$ageg)
qplot(welfare$ageg)

ggplot(welfare %>% filter(!is.na(income))%>% group_by(ageg) %>% summarise(mean_income=mean(income)), aes(x=ageg, y=mean_income))+geom_col()+scale_x_discrete(limits=c('young', 'middle', 'old')) 

ggplot(welfare %>% filter(!is.na(age))%>% group_by(ageg) %>% summarise(mean_income=mean(income)), aes(x=ageg, y=mean_income))+geom_col()+scale_x_discrete(limits=c('young', 'middle', 'old'))#안나옴

#9-5

welfare5 <- welfare %>% filter(!is.na(income))%>% group_by(ageg, sex) %>% summarise(mean_income=mean(income))
welfare5
ggplot(welfare5, aes(x=ageg, y=mean_income, fill=sex)) +
  geom_col(position="dodge") +
  scale_x_discrete(limits=c("young", "middle","old"))

welfare5_1 <- welfare %>% filter(!is.na(income))%>% group_by(age, sex) %>% summarise(mean_income=mean(income))

ggplot(welfare5_1, aes(x=age, y=mean_income, fill=sex)) +
  geom_line() 

ggplot(welfare5_1, aes(x=age, y=mean_income, col=sex)) +
  geom_line()
# fill이 되긴 되는데 col처럼 예쁘게 나오지 않는다.

#9-6

library(readxl)
list_job <- read_excel("Koweps_Codebook.xlsx", col_names=T, sheet=2)
head(list_job)
dim(list_job)
welfare <- left_join(welfare, list_job, id="code_job")
welfare %>%
  filter(!is.na(code_job)) %>%
  select(code_job, job) %>%
  head(10)

top10 <- welfare %>%
  filter(!is.na(code_job) & !is.na(income)) %>% #왜 급여에 NA값이 있으면 평균값에 NA가 나오지?
  select(code_job, job, income) %>%
  group_by(job) %>%
  summarise(mean_income=mean(income)) %>%
  arrange(desc(mean_income)) %>%
  head(10)

#job을 mean_income순으로 정렬하라(음수값을 놓으면 반대순으로, 앞에 파라미터에는 음수값해당안됨!)
ggplot(top10, aes(x= reorder(job,mean_income), y=mean_income)) +
  geom_col() +
  coord_flip() # 그래프 회전
?reorder

#9-7

welfare %>% 
  filter(!is.na(job) & sex=="male") %>%
  select(sex, code_job, job) %>%
  group_by(job) %>%
  summarise(n=n()) %>%
  arrange(desc(n))
#논리적으로 여자 남자 둘다 직업별로 표시할수는 없나?

#9-8

table(welfare$religion)
welfare$religion <- ifelse(welfare$religion == 1, "yes", "no")

welfare$group_marriage <- ifelse(welfare$marriage == 1, "marriage",
                                 ifelse(welfare$marriage == 3, "divorce", NA))
table(welfare$group_marriage)
qplot(welfare$group_marriage)

religion_marriage <- welfare %>%
  filter(!is.na(group_marriage)) %>% #단일 형식의 테이블이 생성되지 않는 것 같다.
  group_by(religion, group_marriage) %>%
  summarise(n=n()) %>%  #groupby 케이스 전체 다 따짐
  mutate(tot_group=sum(n)) %>% #합계는 첫번째 인자 기준으로 산정
  mutate(pct=round(n/tot_group*100, 1)) %>%
  select(group_marriage, religion, tot_group, pct, n)

religion_marriage <- welfare %>%
  filter(!is.na(group_marriage)) %>% #단일 형식의 테이블이 생성되지 않는 것 같다.
  group_by(religion, group_marriage) %>%
  summarise(n=n())

?sum
religion_marriage

table(religion_marriage)

divorce <- religion_marriage %>%
  filter(group_marriage == "divorce") %>%
  select(religion, pct)

divorce

ageg_marriage <- welfare %>% filter(!is.na(group_marriage)) %>%
  group_by(ageg, group_marriage) %>%
  summarise(n=n()) %>%
  mutate(tot_group=sum(n)) %>%
  mutate(pct=round(n/tot_group*100, 1))
  
ageg_marriage

ageg_divorce <-ageg_marriage %>% filter(ageg != "young" & group_marriage == "divorce") %>%
  select(ageg, pct)
  

ageg_religion_marriage <- welfare %>%
  filter(!is.na(group_marriage) & ageg != "young") %>%
  group_by(ageg, religion, group_marriage) %>%
  summarise(n=n()) %>%
  mutate(tot_group=sum(n)) %>% # group_by 순서에 맞춰서 마지막 항목을 제외하고 집계됨 250p
  mutate(pct=round(n/tot_group*100, 1))

ageg_religion_marriage

ageg_religion_marriage <- welfare %>%
  filter(!is.na(group_marriage) & ageg != "young") %>%
  count(ageg, religion, group_marriage) %>% #n 필드 자동생성
  group_by(ageg, religion) %>%
  mutate(pct=round(n/sum(n)*100, 1))


#9-9

list_region <- data.frame(code_region=c(1:7), region=c("서울", "수도권(인천/경기)", "부산/경남/울산", "대구/경북", "대전/충남",
                                                       "강원/충북", "광주/전남/전북/제주도"))
list_region
welfare<- left_join(welfare, list_region, id="code_region")

welfare %>% group_by(region, ageg) %>%
  summarise(n=n()) %>%
  mutate(tot=sum(n)) %>%
  mutate(pct=round(n/tot*100,3))

region_ageg <- welfare %>% count(region, ageg) %>%
  group_by(region) %>%
  #summarise(tot=n()) %>% 왜안돼?
  mutate(pct=round(n/sum(n)*100,2))

ggplot(data=region_ageg, aes(x=region, y=pct, fill=ageg)) + geom_col() + coord_flip()

list_order_old <- region_ageg %>% 
  filter(ageg == "old") %>%
  arrange(pc)

order <- list_order_old$region

ggplot(region_ageg, aes(x=region, y=pct, fill=ageg)) +
  geom_col() +
  coord_flip() +
  scale_x_discrete(limits=order)

region_ageg$ageg <- factor(region_ageg$ageg, level=c("old", "middle", "young"))
levels(region_ageg$ageg)
ggplot(region_ageg, aes(x=region, y=pct, fill=ageg)) + geom_col() +
  coord_flip() +
  scale_x_discrete()

?scale_x_discrete

