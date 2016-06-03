library(dplyr)
dat <- read.csv("femaleMiceWeights.csv")

control <- filter(dat, Diet=="chow") %>% select(Bodyweight) %>% unlist
treatment <- filter(dat, Diet=="hf") %>% select(Bodyweight) %>% unlist

population <- read.csv("femaleControlsPopulation.csv")
population <- unlist(population)

mean(sample(population, 12))

head(dat)

#for loop to check 2 groups of control mice against each other x1000
n <- 10000
null <- vector("numeric", n) #null distribution
for (i in 1:n)
{
##12 randomly selected control mice
  control <- sample(population, 12) ##selects 12 random mice from the population
##12 randomly selected simulated-treatment mice
  treatment <- sample(population, 12)
  null[i] <- mean(treatment) - mean(control)
}
##percent of null > obsdiff
mean(null >= obsdiff)

print(mean(treatment)-mean(control))

