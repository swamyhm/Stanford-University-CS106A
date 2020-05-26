"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    i = 1
    while i < 4:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        print("What is " + str(num1) + "+" + str(num2) + "?")
        total = num1 + num2
        enter = int(input("Your answer: "))
        if total == enter:
            print("Correct! You have got " + str(i) + " corrected in a row")
            i = i + 1
        else:
            print("Incorrect. The expected answer is " + str(total) )
    print("Congratulations! You mastered addition")
    pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
