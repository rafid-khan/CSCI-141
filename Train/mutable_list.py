""" 
file: mutable_list.py
description: functions for manipulating mutable linked lists
"""
__author__ = 'RIT CS'

from node_types import MutableNode
from linked_list_type import LinkedList, make_empty_list

def to_str( lst ):
    """
    to_str: LinkedList -> str
    Construct a string that shows the contents of a linked list.
    The elements are separated by commas and surrounded by brackets.
    :param lst: The LinkedList whose contents will be printed
    """
    result = "[" # result is the accumulator
    node = lst.head.head
    while node is not None:
        result += " " + str(node.value)
        if node.next is not None:
            result += ","
        node = node.next
    result += " ]"
    return result

def append( lst, new_value ):
    """
    append: LinkedList, Any -> None
    Place a new value at the end of a list.
    :param lst: the LinkedList whose node chain will be extended
    :param new_value: the value with which to append the list
    """
    new_node = MutableNode( new_value, None )
    node = lst.head
    if node is None:
        lst.head = new_node
    else:
        successor = node.next
        while successor is not None:
            node = successor
            successor = node.next
        node.next = new_node
    lst.size += 1

def insert_before_index( lst, new_value, index ):
    """
    insert_before_index: LinkedList, Any, int -> None
    Stick a new value in front of the node at a certain ordinal
    position in a list.
    :param lst: the LinkedList object to be modified
    :param new_value: the new value to be inserted
    :param index: how far down, starting at head being index 0, to insert
                  the new value. Everything at the given index and later
                  is effectively shifted further down.
    :pre: index >= 0
    :except: IndexError if index is beyond the size of the list
    """
    new_node = MutableNode( new_value, None )
    current = lst.head
    if index == 0: # We must modify the head of the LinkedList object.
        new_node.next = current
        lst.head = new_node
    elif current is None:
        raise IndexError( "List is shorter than index " + str( index ) + "!" )
    else:
        successor = current.next
        loc = 1
        while successor is not None and loc < index:
            current = successor
            successor = current.next
            loc += 1
        if loc < index: # The list ended prematurely.
            raise IndexError(
                "List is shorter than index " + str( index ) + "!" )
        else:
            new_node.next = successor
            current.next = new_node
    lst.size += 1

def remove_value( lst, value ):
    """
    remove_value: LinkedList, Any -> None
    Locate a value in a list and remove it.
    :param lst: the LinkedList object to be modified
    :param value: the value to search for, starting at head
    :except: ValueError if the value is not present in the sequence
    """
    node = lst.head
    if node is None:
        raise ValueError( "No such value " + str( value ) + " in list!" )
    elif node.value == value:
        lst.head = node.next
    else:
        successor = node.next
        while successor is not None and successor.value != value:
            node = successor
            successor = node.next
        if successor is None:
            raise ValueError( "No such value " + str( value ) + " in list!" )
        else:
            node.next = successor.next
    lst.size -= 1


def test():
    print( "Create list [5,10,15]." )
    lst = make_empty_list()
    lst.head = MutableNode( 15, None )
    lst.head = MutableNode( 10, lst.head )
    lst.head = MutableNode( 5, lst.head )
    lst.size = 3
    print( to_str( lst ), "size =", lst.size )
    print( "Insert 1 before each element in the list." )
    for i in range( lst.size - 1, -1, -1 ):
        insert_before_index( lst, 1, i )
        print( to_str( lst ), "size =", lst.size )
    print( "Append [70,90] to the end of the list." )
    append( lst, 70 )
    append( lst, 90 )
    print( to_str( lst ), "size =", lst.size )
    print( "Extend the list with 100." )
    insert_before_index( lst, 100, lst.size )
    print( to_str( lst ), "size =", lst.size )
    print( "Remove the first 1 by value." )
    remove_value( lst, 1 )
    print( to_str( lst ), "size =", lst.size )
    print( "Remove 15 by value." )
    remove_value( lst, 15 )
    print( to_str( lst ), "size =", lst.size )
    print( "Remove 100 by value." )
    remove_value( lst, 100 )
    print( to_str( lst ), "size =", lst.size )
    print( "Empty the rest of the list!" )
    while lst.size != 0:
        remove_value( lst, lst.head.value ) # removes the head of the list
    print( to_str( lst ), "size =", lst.size )



if __name__ == '__main__':
    test()

