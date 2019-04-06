library(ggplot2, dplyr)
library(dplyr)
mpg

?table

mpg %>%
  select(cty, -drv)

desc(mpg$cty)

table(mpg$drv)
boxplot(mpg$cty)$stats
mpg %>%
  filter(cty > 26 & cty < 9) %>%
  select(cty, drv)

?desc()
# 8-2
ggplot(mpg, aes(x=cty, y=hwy)) + geom_point()
options(scipen=99)
ggplot(midwest, aes(x=poptotal, y=popasian)) + xlim(0,500000) + ylim(0,10000) + geom_point()

# 8-3
ggplot(mpg %>% filter(class=="suv") %>% group_by(manufacturer) %>% summarise(av_cty=mean(cty)) %>% head(5),
       aes(x=manufacturer, y=av_cty))+
  geom_col()
ggplot(mpg,
       aes(x=class))+
  geom_bar()

# 8-4
ggplot(mpg %>% filter(class=="compact" | class == "subcompact" | class == "suv"), aes(x=class, y=cty))+geom_boxplot()
ggplot(economics, aes(x=date, y=psavert))+geom_line()
