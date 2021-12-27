"""
file: mobiles.py
language: python3
author: CS.RIT.EDU
author: Rafid Khan rk3051
description: Build mobiles using a tree data structure.
date: 04/2021
purpose: starter code for the tree mobiles lab
"""


from dataclasses import dataclass
from typing import Union


############################################################
# structure definitions
############################################################


@dataclass
class Ball:
    """
    class Ball represents a ball of some weight hanging from a cord.
    field description:
    cord: length of the hanging cord in inches
    weight: weight of the ball in ounces (diameter of ball in a drawing)
    """

    cord: float
    weight: float


@dataclass
class Rod:
    """
    class Rod represents a horizontal rod part of a mobile with
    a left-side mobile on the end of a left arm of some length,
    and a right-side mobile on the end of a right arm of some length.
    In the middle between the two arms is a cord of some length
    from which the rod instance hangs.
    field description:
    leftmobile: subordinate mobile is a mobile type.
    leftarm: length of the right arm in inches
    cord: length of the hanging cord in inches
    rightarm: length of the right arm in inches
    rightmobile: subordinate mobile is a mobile type.

    An assembled mobile has valid left and right subordinate mobiles;
    an unassembled mobile does not have valid subordinate mobiles.
    """

    leftmobile: Union[None, "Rod"]
    leftarm: float
    cord: float
    rightarm: float
    rightmobile: Union[None, 'Rod']


#########################################################
# Create mobiles from mobile files
#########################################################

def read_mobile(file):
    """
    read_mobile : OpenFileObject ->List( strings representing mobile parts )
    read_mobile reads the open file's content and
    Builds a mobile 'parts list' from the specification in the file,
    for example:
    Rod B1 30 20 30 B2
    B1 100 30
    B2 100 30

    returns parts=["Rod B1 30 20 30 B2", "B1 100 30", "B2 100 30"]

    If there is an error in the mobile specification, then
    report invalid lines.
    # blank lines and '#' comment lines are permitted.
    """

    parts = []
    for lines in file:
        if lines[0] == "#":
            pass
        elif len(lines) == 0:
            pass
        else:
            lines.strip()
            parts.append(lines)

    if len(parts) == 0:
        raise Exception("Error: File has no contents")
    return parts


def construct_mobile(parts):
    """
    construct_mobile : list -> Ball | Rod | NoneType

    construct_mobile reads the parts to put together the
    mobile's components and return a completed mobile object.

    The parts list has the components for assembling the mobile.

    If the parts list contains no recognizable mobile specification,
    or there is an error in the mobile specification, then 
    return None.
    """
    top = parts.pop(0).strip().split()
    if top[0][0] == "R":
        left = construct_mobile(parts)
        right = construct_mobile(parts)
        the_mobile = Rod(left, float(top[2]), float(top[3]), float(top[4]), right)
    elif top[0][0] == "B":
        the_mobile = Ball(float(top[1]), float(top[2]))
    else:
        raise Exception("Error: Not a valid mobile\n\t")

    return the_mobile


############################################################
# mobile analysis functions
############################################################

def is_balanced(the_mobile):
    """
    is_balanced : Mobile -> Boolean

    is_balanced is trivially True if the_mobile is a simple ball. 

    Otherwise the_mobile is balanced if the product of the left side
    arm length and the left side is approximately equal to the 
    product of the right side arm length and the right side, AND
    both the right and left subordinate mobiles are also balanced.

    The approximation of balance is measured by checking
    that the absolute value of the difference between
    the two products is less than 1.0.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """

    if the_mobile is None:
        return False
    elif isinstance(the_mobile, Ball):
        return True
    elif isinstance(the_mobile, Rod):
        var = the_mobile.leftarm * (weight(the_mobile.leftmobile)) - \
              the_mobile.rightarm * weight(the_mobile.rightmobile)
        if -1 < var < 1:
            return True and is_balanced(the_mobile.rightmobile) and \
                   is_balanced(the_mobile.leftmobile)
        return False
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


def weight(the_mobile):
    """
    weight : Mobile -> Number
    weight of the the_mobile is the total weight of all its Balls.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """

    if the_mobile is None:
        return 0
    elif isinstance(the_mobile, Ball):
        return the_mobile.weight
    elif isinstance(the_mobile, Rod):
        lD = weight(the_mobile.leftmobile)
        rD = weight(the_mobile.rightmobile)
        return lD + rD
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


def height(the_mobile):
    """
    height : the_mobile -> Number
    height of the the_mobile is the height of all tallest side.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """

    if the_mobile is None:
        return 0
    elif isinstance(the_mobile, Ball):
        return the_mobile.cord + the_mobile.weight
    elif isinstance(the_mobile, Rod):
        lD = height(the_mobile.leftmobile)
        rD = height(the_mobile.rightmobile)

        if lD > rD:
            return lD + the_mobile.cord
        else:
            return rD + the_mobile.cord
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
