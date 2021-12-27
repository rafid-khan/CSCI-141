"""
file: draw_mobiles.py
description: main program to draw mobiles using turtle
language: python3
author: CS.RIT.EDU
date: 10/2015. updated 11/2019
purpose: supplied code for a solution to tree mobiles lab
"""

import sys  # for command line args
import tkinter as tk  # to get the screen width and height

import turtle as tt

import mobiles as mob  # this is the student's module


def get_screen_info():
    """
    get_screen_info : Void -> Tuple( width, height )
    return the screen dimensions
    """
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.withdraw()
    return screen_width, screen_height


#########################################################
# display a mobile
#########################################################

def init_canvas(wide, high):
    """
    init_canvas : Natural Natural -> NoneType
    init_canvas creates a square canvas with a coordinate system 
    that has the origin at the top-center of the canvas.
    This is suitable for 'hanging' a mobile.

    pre-conditions: wide and high values should be less than screen size.
    post-conditions: size 2 pen is down at origin, facing South.
    """

    margin = 10
    tt.setup(wide, high)
    tt.clear()
    tt.reset()
    tt.setworldcoordinates(-wide / 2, -high, wide / 2, margin)
    tt.right(90)
    tt.pensize(2)


def draw_cord(cordlen):
    """
    draw_cord : Natural -> NoneType
    draw_cord draws a cord as a line with the length written
    half-way down the line.

    pre-conditions: turtle pen is down to draw.
    pre-conditions: turtle start position is the 'cord hang point'
                    and orientation heading is South on the canvas.
    post-conditions: turtle end position is the bottom end of the cord.
    """
    tt.forward(cordlen / 2)
    tt.write(format(cordlen, " .2f"), False \
             , 'left', ('Arial', 12, 'bold'))
    tt.forward(cordlen / 2)


def draw_ball(cordlen, weight):
    """
    draw_ball : Natural Natural -> NoneType
    draw_ball draws a Ball as a circle with the weight inside it
    hanging from a cord of cordlen size.

    pre-conditions: turtle pen is down to draw starting with the cord.
    pre-conditions: turtle start position is the 'cord hang point'
                    and orientation heading is South on the canvas.
    post-conditions: turtle end position, orientation match the start.
    """

    draw_cord(cordlen)
    tt.write(format(weight, " .2f"), False \
             , 'left', ('Arial', 12, 'bold'))
    tt.right(90)
    # weight is represented by the diameter (i.e. half the radius)
    tt.circle(weight / 2)
    tt.left(90)
    tt.forward(- cordlen)


def draw_rod(leftmobile, leftarm, cordlen, rightarm, rightmobile):
    """
    draw_rod : Mobile Natural Natural Natural Mobile -> NoneType

    pre-conditions: turtle pen is down to draw starting with the cord.
    pre-conditions: turtle start position is the 'cord hang point'
                    and orientation heading is South on the canvas.
    post-conditions: turtle end position, orientation match the start.
    """

    draw_cord(cordlen)
    tt.right(90)
    # left side
    tt.forward(leftarm)
    tt.write(format(leftarm, ".2f"), False \
             , 'center', ('Arial', 12, 'bold'))
    tt.left(90)
    draw_mobile(leftmobile)  # recurse indirectly
    tt.left(90)

    # then right side
    tt.forward(leftarm + rightarm)
    tt.write(format(rightarm, ".2f"), False \
             , 'center', ('Arial', 12, 'bold'))
    tt.right(90)
    draw_mobile(rightmobile)  # recurse indirectly
    tt.left(90)
    tt.forward(- rightarm)
    # then back up to the cord hang point of this Rod
    tt.right(90)
    tt.forward(- cordlen)


def draw_mobile(the_mobile):
    """
    draw_mobile : the_mobile -> NoneType
    draw_mobile draws the mobile structure.
    If any of the components of the_mobile is not
    either a Ball or a Rod object, then raise an
    exception with the message 'not a valid mobile {mobile}',
    where {mobile} is the string representation of the_mobile.

    pre-conditions: turtle pen is down to draw starting with the cord.
    pre-conditions: turtle start position is the 'cord hang point'
                    and orientation heading is South on the canvas.
    post-conditions: turtle end position, orientation match the start.
    """

    if isinstance(the_mobile, mob.Ball):
        draw_ball(the_mobile.cord, the_mobile.weight)

    elif isinstance(the_mobile, mob.Rod):
        draw_rod(the_mobile.leftmobile \
                 , the_mobile.leftarm \
                 , the_mobile.cord \
                 , the_mobile.rightarm \
                 , the_mobile.rightmobile)

    else:
        raise Exception("Error: Not a valid mobile\n\t" + \
                        str(the_mobile))
    return


def width(the_mobile):
    """
    width : the_mobile -> Number
    return the width of the the_mobile.
    If the mobile is a simple Ball, then the width is the diameter.
    Remember that the ball's weight also represents its diameter.

    The width of its widest point must take into account 
    the rotation of complex mobiles.
    If the mobile is a Rod with submobiles, then
    the width has special issues because the mobile may
    rotate. The possible rotation may cause the widest side
    to shift from one side of the hang point to another.
    To account for this spinning, this function needs to
    identify the width of the widest side and use that as
    the width of both sides of the mobile.
    """

    return 2 * width_aux(the_mobile)


def width_aux(the_mobile):
    """
    width_aux : the_mobile -> Number
    return the width of the widest side of the_mobile.
    If the mobile is a simple Ball, then the width is the diameter.
    Remember that the ball's weight also represents its diameter.

    If the mobile is a Rod with submobiles, then
    identify the width of the widest side 
    and return the value of the widest.

    If the_mobile is not valid, then raise an exception
    with the message 'not a valid mobile {mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """

    if isinstance(the_mobile, mob.Ball):
        return the_mobile.weight

    elif isinstance(the_mobile, mob.Rod):

        lwide = the_mobile.leftarm + width_aux(the_mobile.leftmobile)
        rwide = the_mobile.rightarm + width_aux(the_mobile.rightmobile)
        return max(rwide, lwide)

        # else unconditionally raise exception for any other case.
    raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


def process_mobile_file(screen_width, screen_height, fname):
    """
    process_mobile_file : Natural Natural String -> NoneType
    process_mobile_file processes the mobile found in fname by
    constructing it, and displaying it within the limits of
    a canvas size less than or equal to the screen's width and height.
    Procedure:
        - read the mobile file, which builds the mobile.
        - print whether or not the mobile is balanced.
        - print the weight of the mobile.
        - print the width and height of the mobile.
        - set up the canvas. 
        - display the mobile.
    """

    parts = mob.read_mobile(open(fname))

    the_mobile = mob.construct_mobile(parts)

    if isinstance(the_mobile, mob.Ball) \
            or isinstance(the_mobile, mob.Rod):

        print("file:", fname)
        print("is balanced? :", mob.is_balanced(the_mobile))
        print("weight:", mob.weight(the_mobile))
        high = mob.height(the_mobile)
        wide = width(the_mobile)
        print('width X height:', wide, 'X', high)
        # set the canvas size so most of the mobile is visible.
        # Note that mobiles with one very long side arm
        # might not fully display without canvas enlargement.
        cwidth, cheight = (wide * 1.2, high * 1.2)
        print('canvas size (w x h):', cwidth, 'X', cheight)
        init_canvas(min(cwidth, screen_width) \
                    , min(cheight, screen_height))
        draw_mobile(the_mobile)

    else:
        print(fname, "did not contain a valid mobile")

    ############################################################


# main function
############################################################

def main():
    """
    main : Void -> NoneType
    The main program:
        - prompts for name of file containing one mobile description.
        -- if the name is the empty string, the program ends.
        - processes the mobile file in process_mobile_file.
    """

    while True:
        fname = input("Enter a Mobile file name(hit enter to quit): ")
        if fname == "":
            tt.bye()
            return
        width, height = get_screen_info()
        process_mobile_file(width, height, fname)

    return


if __name__ == "__main__":
    main()
