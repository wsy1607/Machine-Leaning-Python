#list: insert
a = ['a','b','c','d']
a.insert(0, 'e')
print(a)

#list: pop
a.pop(2)
print(a)

#list: sort by compare function
a = [('a',3), ('b',2), ('c',1), ('b',5), ('b',1)]
def compare_fun(a,b):
    if a[0] != b[0]:
        return((a[0] > b[0]) - (a[0] < b[0]))
    else:
        return((a[1] < b[1]) - (a[1] > b[1]))

print(sorted(a))
print(sorted(a, cmp=compare_fun))

#binary search function
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))

#queue using deque
from collections import deque

queue = deque([1,5,8,9])
queue.append(7)
queue.appendleft(0)
print(queue)
queue.popleft()
queue.pop()
print(queue)
queue.rotate(-1)
print(queue)

#heap using heapq
import heapq

data = [19, 9, 4, 10, 11, 8, 2]
heap = []
for n in data:
    heapq.heappush(heap, n)
print(heap)
heapq.heapify(data)
print(data)
