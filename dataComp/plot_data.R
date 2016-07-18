install.packages("plotly")
library(plotly)
old_wd <- getwd()
wd <- "C:/Users/goreg/OneDrive/Documents/GitHub/data-alpha-Guilf/dataComp"
setwd(wd)

filename <- "updated_plate_reader.csv"
dat1_unlisted <- unlist( read.csv(filename) ) #unlist?
dat1 <- read.csv(filename)

dat1_head <- head(dat1, n = 2L)
dat1_tail <- tail(dat1, n = 2L)

data_range <- 0
  
for (column in 2:length(dat1)) {
  if (range(column) > data_range) data_range <- range(column)
}

xrange <- (dat1$Time)
yrange <- 

x <- c(1:5); y <- x # create some data 
par(pch=22, col="red") # plotting symbol and color 
par(mfrow=c(2,4)) # all plots on one page 
opts = c("p","l","o","b") 
for(i in 1:length(opts)){ 
  heading = paste("type=",opts[i]) 
  plot(x, y, type="n", main=heading) 
  lines(x, y, type=opts[i]) 
}


setwd(old_wd) #reset working directory