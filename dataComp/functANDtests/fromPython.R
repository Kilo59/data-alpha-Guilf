# fromPython.R
# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)

# Convert to numerics
data_list = as.numeric(myArgs)

# cat will write the result to the stdout stream
cat(max(nums))
