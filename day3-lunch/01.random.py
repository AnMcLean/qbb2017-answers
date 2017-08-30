#!/usr/bin/env python

import random

# Generates and prints a random number between 1 and 100
r = random.randint(1,100)
print r

# Generates 50 random numbers and prints a list with those numbers
nums = []

for i in xrange(5):
    print i
    r = random.randint(1,100)
    print "the %dth number is %d" % (i, r)
    nums.append(r)

print nums

# Sorts and prints the list of random numbers
nums.sort()

nums = range(100)
print nums

key = 4



potential_range = xrange(len(nums))

while i in potential_range:
    v = nums[i]
    if i == key:
        print "the %dth number is %d" % (i, v)
        break
    elif i < key:
        potential_range = xrange(0,key)
        continue  
    else:
        potential_range = xrange((key+1),100)
        continue
 
        
low = 0
high = len(nums) 

while low < high:
    mid_indx = (low + high) / 2
    mid = nums[mid_indx]
    
    print "checking in the range [%d, %d] mid_indx[%d]=%d" % (low, high, mid_indx, mid)
    
    if mid == key:
        print "hooray! found %d==%d AT %d" % (key, mid, mid_indx)
        break
    elif key > mid:
        low = mid_indx + 1
    else:
        hi = mid_indx