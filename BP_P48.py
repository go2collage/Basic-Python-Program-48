# Python Program

# generate six random integers between 10 and 30

# import lib.
import numpy as np

size_num = int(input("Enter size of random integers number between 10 to 30: "))

num = np.random.randint(low= 10, high= 30, size= size_num)

# size is output shape
# low is start value
# high is end value
# number of values show based on size, let's see

print(f" {size_num} Random integers between 10 and 30: ")
print(num)

# Thanks for Watching