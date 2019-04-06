install.packages("rJava",,"http://rforge.net/",type="source")
install.packages("memoise")
install.packages("KoNLP")



useNIADic()

txt <- readLines("hiphop.txt")

dyn.load("/Library/Java/JavaVirtualMachines/jdk-11.0.2.jdk/Contents/Home/lib/server/libjvm.dylib")
options(JAVA.HOME="/Library/Java/JavaVirtualMachines/jdk-11.0.2.jdk/")
Sys.setenv(DYLD_FALLBACK_LIBRARY_PATH="/Library/Java/JavaVirtualMachines/jdk-11.0.2.jdk/Contents/Home/jre/lib/server/")
Sys.getenv("JAVA_HOME")

Sys.setenv(JAVA_HOME = '/Library/Java/JavaVirtualMachines/jdk1.11.0.2.jdk/Contents/Home/jre')

library(KoNLP)
library(dplyr)
remove.packages("rJava")

install.packages("wordcloud")
library(wordcloud)
library(RColorBrewer)
?read.csv
?brewer.pal
?set.seed
??wordcloud

#factor에 관하여

credit_rating <- c("A", "A", "BB")
bond_owners <- c("Dan", "Tom", "Joe")

bonds <- data.frame(credit_rating, bond_owners, stringsAsFactors = T)
bonds
str(bonds)
