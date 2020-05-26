from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    building()
    turn_right()
    build()
    turn_left()
    move1()
    building()
    turn_right()
    build()
    turn_left()
    pass

#To build one single stage
#pre: karel starts building first wall
#post: karel finished building both the walls of first building
def building():
    turn_left()
    build()
    turn_right()
    move1()

#karel moves four steps
def move1():
    for i in range (4):
        move()

#To put beepers whereever not present
#pre: karel will move if front is not blocked
#post: Karel puts beepers wherever it is not present and stops when hits a wall
def build():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        else:
            move()

#karel is turn right
#pre: karel at any position looking to turn right
#post: karel turned right by flipping three times left
def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
