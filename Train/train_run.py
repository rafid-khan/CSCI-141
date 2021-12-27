"""
Rafid Khan
CSCI 141
Lab 08
Professor Polak

This application utilizes linked lists to
help a train make delieveries in
take in accordance to commands from the
user, which can be inputted in a flexible order (within reason).
"""

# imports
from immutable_list import *
from linked_list_type import *
from mutable_list import *
from node_types import *
from dataclasses import dataclass
from typing import Any, Union


@dataclass()
class Car:
    contents: str
    station: str
    distance: float


@dataclass()
class Train:
    speed: float
    head: LinkedList
    size: int


def set_speed(velocity, trn):
    """
    Sets the speed of the train.
    Takes in velocity, and the linked list (train)
    as parameters.
    """
    trn.speed = velocity
    return trn.speed


def train_size(trn):
    """
    Prints the size of the train.
    Takes the linked list (train) as a parameter.
    """
    print(trn.size)


def car(ct, st, dist):
    """
    Helper function to help create a new car node.
    """
    new_car = Car(ct, st, dist)
    return new_car


def add_car(tr, new_car):
    """
    Creates a new car node, and adds it into the
    linked list train, in ascending order relative
    to distance.
    """
    car_node = MutableNode(new_car, None)
    nxt = tr.head.head
    previous = None
    while nxt is not None:
        if new_car.distance < nxt.value.distance:
            break
        previous = nxt
        nxt = nxt.next
    if previous is None:
        car_node.next = tr.head.head
        tr.head.head = car_node
    else:
        previous.next = car_node
    tr.size += 1


def show_train(trn):
    """
    Utilizes the to_str(lst) function from lecture
    to take in the linked list (train) and prints
    a readable version of the linked list.
    """
    readable_lst = to_str(trn)
    print("Engine (", trn.speed, ")", readable_lst)






def help_commands():
    """
    Prints a list of possible commands.
    """
    print("List of possible commands: "
          "\n set_speed <speed>."
          "\n add_car <content> <station> <distance>"
          "\n show_train"
          "\n train_size"
          "\n help"
          "\n quit")


def quit_func():
    """
    Ends the command processing function, and
    displays an ending message.
    """
    print("Train yard simulation ending.")
    return


def start(trn):
    """
    Visits all the stations and drops off the cars
    at their destined locations. Takes in linked list
    trn as a parameter.
    """
    overall_time = 0
    segment_time = 0
    d = 0
    while trn.head.head is not None:
        next_station = trn.head.head.value.station
        if d != trn.head.head.value.distance:
            print("En route to", next_station)
            segment = trn.head.head.value.distance - d
            segment_time += 0.50
            print("0.50 hours taken to separate cars.")
            segment_time += segment / trn.speed
            print("This segment took", segment_time, "hours to "
                                                     "travel.")
            overall_time += segment_time
            d += trn.head.head.value.distance

        unloaded_car = trn.head.head.value.contents
        trn.head.head = trn.head.head.next
        print("Unloading", unloaded_car, "in", next_station)

    print("Total time for trip was", overall_time, "hours.")


def process_commands(command, trn):
    """
    Takes in commands and slices them. Uses multiple
    conditional statements to call the correct function
    according to the command inputted by user. Takes in
    command, and a linked list (trn) as a parameter.
    """
    values = command.split()
    if len(values) == 0:
        print("Illegal use or form for this command: ")
        return True
    i = values[0]

    if i == "set_speed":
        if int(values[1]) < 0:
            print("Speed must be a positive value.")
            return True
        else:
            set_speed(int(values[1]), trn)
        return True

    elif i == "add_car":
        if len(values) != 4:
            print("Illegal use or form for this command:")
            print("add_car <content> <station> <distance>")
            return True
        else:
            ct = values[1]
            st = values[2]
            dist = float(values[3])
            if dist < 0:
                print("Distance must be a positive value.")
                return True
            else:
                new_car = car(ct, st, dist)
                add_car(trn, new_car)
                return True

    elif i == "show_train":
        if len(values) > 1:
            print("Illegal use or form for this command: ")
            return True
        else:
            show_train(trn)
            return True

    elif i == "train_size":
        if len(values) > 1:
            print("Illegal use or form for this command: ")
            return True
        else:
            train_size(trn)
            return True

    elif i == "help":
        if len(values) > 1:
            print("Illegal use or form for this command: ")
            return True
        else:
            help_commands()
            return True

    elif i == "start":
        if trn.head.head is None:
            print("You must add a car before you proceed.")
            return True
        elif trn.speed == 0:
            print("You must set a speed before you proceed")
            return True
        elif len(values) > 1:
            print("Illegal use or form for this command: ")
            return True
        else:
            start(trn)
            return True

    elif i == "quit":
        if len(values) > 1:
            print("Illegal use or form for this command: ")
        else:
            quit_func()
            return False

    else:
        print("Illegal command name")
        return True


def main():
    """
    Main function which initializes the dataclass,
    prints a welcome message, a list of possible
    commands, and then goes through a while loop
    to continue prompting user for commands until
    base case is met.
    """
    trn = Train(0.0, make_empty_list(), 0)
    print("Welcome to the train yard!")
    help_commands()
    while True:
        command = input("Enter command: ")
        if not process_commands(command, trn):
            break
    print("Thank you :)")


main()
