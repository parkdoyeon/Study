library(dplyr)
df_raw <- data.frame(var1=c(1,2,1),
                     var2=c(2,3,2))
df_raw

df_new <- df_raw

df_new <- rename(df_new, v2= var2)
df_new

df_raw$var3 <- df_raw$var1 + df_raw$var2
df_raw
df_raw$var_mean <- mean(df_raw$var1+df_raw$var2)
df_raw
df_raw$var_mean <- (df_raw$var1+df_raw$var2)/2

df_raw %>% filter(var1==1)

?mean
mpg
mpg$total <- (mpg$cty + mpg$hwy)/2
summary(mpg$total)
hist(mpg$total)
mpg$test <- ifelse(mpg$total >= 20, "pass", "fail")
head(mpg)
table(mpg$test)
qplot(mpg$test)


head(midwest)
midwest
newmw <- rename(midwest, total=poptotal, asian=popasian)
newmw
newmw$asianratio <- (newmw$asian)/(newmw$total)
head(newmw$asianratio)
hist(newmw$asianratio)
summary(newmw)
qplot(newmw$asianratio)
dim(newmw)
total_av <- mean(newmw$total)
asian_av <- mean(newmw$asian)
asianav_rt <- asian_av/total_av
newmw$asianlarge <- ifelse(newmw$asianratio > asianav_rt, "large", "small")
table(newmw$asianlarge)
newmwz



library(ggplot2)
midwest %>%
  mutate(deadultratio = (poptotal-popadults)/poptotal) %>%
  select(popadults, poptotal, deadultratio, county) %>%
  mutate(level=ifelse(deadultratio > 0.4, "large", ifelse(deadultratio > 0.3, "middle", "small"))) %>%
  group_by(level) %>%
  summarise(n())

midwest %>%
  mutate(asianratio= (popasian/poptotal)) %>%
  select(state, county, asianratio) %>%
  arrange(asianratio) %>%
  head(10)

mpg[c(10, 14, 58, 93), "drv"] <- "k"
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 5, 39, 42)
table(mpg$drv)
mpg$drv <- ifelse(mpg$drv == "k", NA, mpg$drv)
mpg %>% filter(drv %in% c(4, "f", "r")) %>%
  group_by(drv) %>%
  summarise(n())
table(mpg$drv)
boxplot(mpg$cty)$stats
mpg <- ifelse(mpg$cty > 26 & mpg$cty < 9, NA, mpg$cty)
mpg
table(mpg)
str(mpg)
install.packages("ggplot2")
library(ggplot2)
