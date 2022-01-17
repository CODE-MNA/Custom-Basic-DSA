def CustomSort(array):
    
    for i in range(len(array)):
        start = i
        smallest = array[i]
        for j in range(start,len(array)):
           
      
            if array[j] < smallest :
                smallest = array[j]
                array[i],array[j] = array[j],array[i]
    
    return array           

#FASTER for SMALL
def InsertionSort(array):
    
    for i in range(len(array)):
        value = array[i]
        while value < array[i-1] and i > 0:
            array[i],array[i-1] = array[i-1],array[i]
            i -=1
    return array

#FOR BIGG

def QuickSort(array):
    #Base Case is array is out of indexes else remove an item
    if len(array) <= 0 :
        return array
    else:
        pivot = array.pop() 
   
    lower_array = []
    upper_array = []
    
    for i in array :
        if i < pivot:
            lower_array.append(i)
            
        else:
            upper_array.append(i)
            
        
        
    return QuickSort(lower_array) + [pivot] +QuickSort(upper_array)

