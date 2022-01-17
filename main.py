from typing import List
from linkedList import SinglyLinkedList
from stack import Stack
from node import Node
from algorithms.sorting import *
from algorithms.searching import *
import timeit

# Append Code HERE    
def main():        
  
  StackTest()
  
    

def SORTING_TEST():
    TEST_AMOUNT = 10000
    numberArray = [34,124,4124,214,123,23,2,1,1,41,51,53,314,7,124,124,12421412412421,213123,123142,421412,21421,4,214,124215678,765412,367876,54,324,24,56578909876543,324234,6,765,2,42,63,2,57,3,7,8,765,6,78,764,3543,5,47876667,5654,3341,4145]

    
  

    print("Ins : " + str(timeit.timeit('InsertionSort([5,4,2,1,5])',setup='from algorithms.sorting import InsertionSort',number=TEST_AMOUNT)))
    
    print("Sel : " + str(timeit.timeit('CustomSort([5,4,2,1,5])',setup='from algorithms.sorting import CustomSort',number=TEST_AMOUNT)))
    
    print("Quick : " + str(timeit.timeit('QuickSort([5,4,2,1,5])',setup='from algorithms.sorting import QuickSort' ,number=TEST_AMOUNT)))

def LinkedListTest():
    L = SinglyLinkedList()
    L.appendList(['ab',325,1233,123,5325,63])
    print(L)
    

def StackTest():
    VALUE_TO_SEARCH = input('Enter the value that you like to search for : ')
    while VALUE_TO_SEARCH.isdigit() is False:
         VALUE_TO_SEARCH = input('Please enter a number')
    
    VALUE_TO_SEARCH = int(VALUE_TO_SEARCH)
        
    
    
    S = Stack()
    S.pushMultiple([523,432,11,213,12,124,512,321,562,424])
    arr = S.data
    k = BinarySearch(arr,VALUE_TO_SEARCH,0,len(arr)-1, int(len(arr)-1/2))
    print(k)
    
if __name__ == "__main__":  
    main()
    
