library(ggplot2)

t.test(mpg_diff, cty ~ class, var.equal=T) #집단간 분산이 같다고 가정하면 T 아니면 F
# 골고루 분포되어있다는 어떻게 계산하지?


# 13-2

carcor <- cor(mtcars)



carcor
round(carcor, 2)

install.packages("corrplot")
library(corrplot)

corrplot(carcor)
corrplot(carcor, method="number")

col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))
corrplot(carcor,
         method="color",
         col = col(200),
         type = "lower",
         order = "hclust",
         addCoef.col = "black",
         tl.col = "black",
         tl.srt = 45,
         diag = F)
