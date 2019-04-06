# 12-1

install.packages("plotly")
library(plotly)
library(ggplot2)

mpg_p <-ggplot(data=mpg, aes(x=displ,y=hwy,col=drv))+geom_point() #drv는 컬러값으로 구분
ggplotly(mpg_p)

dia_p <- ggplot(data=diamonds, aes(x=cut, fill=clarity)) + geom_bar(position="dodge");
ggplotly(dia_p)

# 12-2
install.packages("dygraphs")
library(dygraphs)

eco_p <- economics #라이브러리 로드 별도로 안하고 부르고싶다면 eco_p <- ggplot2::economics
head(eco_p)
library(xts)
eco <- xts(economics$unemploy, order.by=economics$date)
head(eco)
dygraph(eco) %>%
  dyRangeSelector()

eco_a <- xts(economics$psavert, order.by=economics$date)
eco_b <- xts(economics$unemploy/1000, order.by=economics$date)

eco2 <- cbind(eco_a, eco_b)
?cbind

eco2
colnames(eco2) <- c("psavert", "unemploy")
dygraph(eco2) %>% dyRangeSelector()
