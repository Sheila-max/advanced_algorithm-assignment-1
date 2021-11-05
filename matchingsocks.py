import math
import os
import random
import re
import sys

# Create a matchingSocks function
# Initialize the number of pairs variable to zero. 
# Create a set and assign it to colors variable

def matchingSocks(n, ar):  #The function carries two arguments integers n and an array ar
    num_pairs = 0
    colors = set()

# Loop through the sorted array
# If the set doesn’t have the current value, add it to the set
# Else, increment the number of pairs variable.
# Then remove it from the pair

    for i in range (len(ar)):
        if ar[i] not in colors:
            colors.add(ar[i])

        else:
            num_pairs += 1
            colors.remove(ar[i])
        
    return num_pairs

if __name__ == '__main__':
   
    n = input(int()).strip()

    # Sort the given array
    ar = list(map(int, input().rstrip().split()))
    ar.sort()

    result = matchingSocks(n, ar)
    print(result)

