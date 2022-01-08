from linkedList import SinglyLinkedList
from node import Node

# The main actions that happen when we start program    
def main():        
    Ll = SinglyLinkedList()
    Ll.prepend(Node(423))
    Ll.append(Node(324))
    Ll.prepend(Node(331))
    print(Ll)


#Starting the program
main()