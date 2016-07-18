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
yrange <- (data_range) 

# Simple Scatterplot
attach(dat1)
plot(Time, Well.Damn, main="Scatterplot Example", 
  	xlab="Time", ylab="Optical Density ", type = "b")

setwd(old_wd) #reset working directory