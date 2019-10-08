import heapq

lists = [1,2,3,4,5]

heapq.heapify(lists)
heapq.heappush(lists, 100)
print ("The created heap is : ", end="") 
print (list(lists)) 


