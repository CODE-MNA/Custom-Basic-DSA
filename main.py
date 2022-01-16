from typing import List
from linkedList import SinglyLinkedList
from node import Node
from algorithms.sorting import *
import timeit

# Append Code HERE    
def main():        
  LinkedListTest()
  
    

def SORTING_TEST():
    TEST_AMOUNT = 10000
    numberArray = [34,124,4124,214,123,23,2,1,1,41,51,53,314,7,124,124,12421412412421,213123,123142,421412,21421,4,214,124215678,765412,367876,54,324,24,56578909876543,324234,6,765,2,42,63,2,57,3,7,8,765,6,78,764,3543,5,47876667,5654,3341,4145]

    
  

    print("Ins : " + str(timeit.timeit('InsertionSort([5,4,2,1,5])',setup='from algorithms.sorting import InsertionSort',number=TEST_AMOUNT)))
    
    print("Sel : " + str(timeit.timeit('CustomSort([5,4,2,1,5])',setup='from algorithms.sorting import CustomSort',number=TEST_AMOUNT)))
    
    print("Quick : " + str(timeit.timeit('QuickSort([5,4,2,1,5])',setup='from algorithms.sorting import QuickSort' ,number=TEST_AMOUNT)))

def LinkedListTest():
    Ll = SinglyLinkedList()
    Ll.prepend(Node(423))
    Ll.append(Node(324))
    Ll.prepend(Node(331))
    
 



if __name__ == "__main__":  
    main()