#15-1

exam <- read.csv("csv_exam.csv")
exam[,"math" & "class"] #안됨

library(ggplot2)

ggplot2::mpg # 324페이지 왜 as.data.frame변환하지?
s_ch <- mpg[mpg$class == "suv",c("cty", "hwy", "class")]
c_ch <- mpg[mpg$class == "compact",c("cty", "hwy")]

ch <- mpg[mpg$class == "suv" | mpg$class == "compact", c("cty", "hwy", "class")]
ch$aver <- (ch$cty + ch$hwy)/2

s_ch$aver <- (s_ch$cty + s_ch$hwy)/2
s_ch

aggregate(aver~class, data=ch, mean)

c_ch_m <- (c_ch$cty + c_ch$hwy)/2

#15-3
?boxplot
