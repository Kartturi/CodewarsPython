import statistics 
from statistics import mode 

def find_missing(sequence):
    #find the gap
    gapList = []
    for i,item in enumerate(sequence):
        post = i + 1
        gap = sequence[post] - sequence[i]
        if len(gapList) != 3:
            gapList.append(gap)
        else:
            break
    
    gap = mode(gapList)

    #find the missing number
    for i,item in enumerate(sequence):
        post = i + 1
        desired = sequence[i] + gap
        actual = sequence[post]
        
        if desired != actual:
            return desired
        
        if post > len(sequence):
            break
    

print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))
            
