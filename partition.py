#Author: Michael Elgart
#Copyright 2016 CC-BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/

from collections import Counter
import sys

n = 1
# partition goal
if len(sys.argv) > 1:
	n = sys.argv[1]
else:
    n = int(input("What number do you want the partitions for?"))
    
#returns a list of lists. Each sublist sums to the partition_goal    
def recursive_partition(partition_goal):
	return_list =[]
	if partition_goal==1:
		return_list.append([1])
	else:
		return_list.append([partition_goal])
		for i in range(1,partition_goal):
			for j in recursive_partition(partition_goal - i):
				j.append(i)
				return_list.append(j)
	return return_list
	
list_of_lists = recursive_partition(n)

counted = Counter(tuple(sorted(entry)) for entry in list_of_lists)

print(list(counted.keys()))
