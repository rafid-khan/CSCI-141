""" 
file: linked_list_type.py
description: type definitions for linked list construction, plus some print
    functions and a simple test/demo main function
author: RIT CS
"""

from typing import Union
from dataclasses import dataclass
from node_types import MutableNode

@dataclass( frozen=False )
class LinkedList:
    """
    For mutable linked lists, we 'encapsulate' the list nodes in a wrapper
    class. This will allow functions that work with mutable lists to not
    worry about whether the list is empty or not. An empty list is still an
    instance of this LinkedList class; it's just that its head is None.
    The size of the list is stored here, too, as an example of the tradeoff
    between computing something every time you need it and using extra
    memory to store the value so that it does not have to be recomputed.
    """
    head: Union[ MutableNode, None ] = None
    size: int = 0

def make_empty_list():
    """
    make_empty_list: -> LinkedList
    Make an empty list
    ("maker function")
    :return: a LinkedList object of size 0, head = None
    """
    return LinkedList( None, 0 )

def print_linked_list( lst, ending="\n" ):
    """
    print_linked_list: LinkedList, str -> None
    Print the contents of a linked list, surrounded by brackets, and with the
    elements separated by commas.
    :param lst: The LinkedList whose contents will be printed
    :param ending: what to print after the closing brace (default: new line)
    """
    print( '[', end="" )
    node = lst.head
    while node is not None:
        print( ' ' + str(node.value), end="" )
        node = node.next
    print( " ](" + str( lst.size ) + ')', end=ending )

# ---------------------- Very Basic Test Code --------------------------------

def test() -> None:
    """
    Let's make some node structures.
    """
    our_list = MutableNode( 4, MutableNode( 5, MutableNode( 6, None ) ) )
    our_list_object = LinkedList( our_list, 3 )
    print_linked_list( our_list_object )
    print( "Above line should be [ 4 5 6 ](3)." )

    # Don't do this in regular code: MutableNodes shouldn't normally be shared!
    our_list_object = LinkedList( our_list_object.head.next, 2 )
    print_linked_list( our_list_object )
    print( "Above line should be [ 5 6 ](2)." )

    our_list_object = make_empty_list()
    print_linked_list( our_list_object )
    print( "Above line should be [ ](0)." )


if __name__ == '__main__':
    test()
