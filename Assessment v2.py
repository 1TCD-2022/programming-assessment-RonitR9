"""
Filename: mathsquiz.py
Author: Ronit Rathore
Date: July 2022
Description: This program will ask the user a maths question and they will enter an answer. If the answer is wrong then he computer will tell them so and if it's right then they will also be told so.
A menu will also be added so the user can be greeted and asked to see if they want to play or not
"""

import time
import random


VALID_CHOICE = ["yes","no"]
operators = ["+","-","*","/"]

valid = False

#greet the user and ask them if they want to play or not
user_name = input("hello what's your name: ")
user_name = print("hello",user_name,)
print("      ")
time.sleep(0.8)
print("""This program will print out a randomly generated maths question,
would you like to play, yes or no""")
print("  ")
time.sleep(1)

menu_choice = input("please enter either yes or no: ").lower()
while not menu_choice in VALID_CHOICE:
    menu_choice = input("please enter either 'yes' or 'no': ").lower()

    

#validate their input
#print a message depending on their input
if menu_choice == "no":
    print("goodbye")
elif menu_choice == "yes":
    print("let's begin")



    #make the computer generate a random number and operator
    #make the computer do the correct maths
    time.sleep(1)
    rand = random.randint(1,10)
    rand2 = random.randint(1,10)
    operation = ((random.choice(operators)))

    if operation == "+":
        maths = ((rand) + (rand2))
    elif operation == "-":
        maths = ((rand) - (rand2))
    elif operation == "/":
        maths = ((rand) / (rand2))
    else:
        maths = ((rand) * (rand2))
        
    #ask the user a randomly generated question
    #validate their input
    #print out a message depending on their input
    
    while not valid:
        try:
        
            print("what is",rand,operation,rand2)
            question = int(input("What is your answer: "))
            valid = True
        except ValueError:
            question = int(input("please enter a number: "))
        if question==maths:
            print("correct")
        else:
            print("incorrect, the right answer was",maths)
        

        

    #ask the user if they want another maths question
    print("would you like another maths question? ")
    print("    ")
    another_question = input("please enter either yes or no: ").lower()



    #print out another question if they ask to do so, otherwise end game
    while not another_question in VALID_CHOICE:
        another_question = input("please enter either yes or no: ").lower()
    if another_question =="no":
        print("hope you had fun, goodbye")
    else:
       print("quiz starting...")

       
