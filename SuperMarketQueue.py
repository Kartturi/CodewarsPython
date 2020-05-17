import heapq

#Challenge made by mattlub
# There is a queue for the self-checkout tills at the supermarket. 
# Your task is write a function to calculate the total time required 
# for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. 
# Each integer represents a customer, and its value is the amount of
#  time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.


#own implementation none

#best solution method, from siebenschlaefer
def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)



queue_time([5,3,4], 2)