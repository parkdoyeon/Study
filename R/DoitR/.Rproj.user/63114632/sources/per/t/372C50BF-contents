#brew install cairo
install.packages("gdtools", type = "source")
install.packages("ggiraphExtra")

library(ggiraphExtra)
library(tibble)

table(USArrests)
USArrests
crime <- rownames_to_column(USArrests, var="state")
?rownames_to_column
crime$state <- tolower(crime$state)
crime

library(ggplot2)
install.packages("maps")
library(maps)
states_map <- map_data("state")
str(states_map)
install.packages("mapproj")
library(mapproj)
ggChoropleth(data=crime,
             aes(fill=Murder,
                 map_id=state),
             map=states_map,
             interactive=T)

install.packages("stringi")
install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")
library(kormaps2014)
library(readr)
guess_encoding(korpop1)
?changeCode
korpop1
encoded <- changeCode(korpop1, from="UTF-8", to="CP949")
str(korpop1)

library(dplyr)
korpop1 <-rename(korpop1,
                 pop=총인구_명,
                 name=행정구역별_읍면동)

ggChoropleth(data=tbc,
             aes(fill=NewPts,
                 map_id=code,
                 tooltip=name),
             map=kormap1,
             interactive=T)  
?set.seed
