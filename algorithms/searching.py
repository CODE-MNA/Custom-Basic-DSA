
def BinarySearch(array,search,start,end,mid):
    if (start == end and array[mid] != search):
        return False
   
    if (array[mid] == search):
        return True
    elif (array[mid]< search):
        start = mid+1
        end = end
    else:
        start = start
        end = mid-1

    mid = int((start + end)/2)
    return BinarySearch(array,search,start,end,mid)
     
    
    
    