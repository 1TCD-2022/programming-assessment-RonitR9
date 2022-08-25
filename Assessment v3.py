"""
Filename: mathsquiz.py
Author: Ronit Rathore
Date: July 2022
Description: This program will ask the user a maths question and they will enter an answer. If the answer is wrong then the computer will tell them so and if it's right then they will also be told so.
A menu will also be added so the user can be greeted and asked to see if they want to play or not
"""

import time
import random


VALID_CHOICE = ["yes","no"]
operators = ["+","-","*","/"]

valid = False
continue_play = True
counter=0
count=0

print("                      ~~~~~~ Maths Program ~~~~~~")


#greet the user and ask them if they want to play or not
user_name = input("hello what's your name: ")
user_name = print("hello",user_name,)
print("      ")
time.sleep(0.8)
print("""This program will print out a randomly generated maths question,
you will be asked to enter an input and then the computer will tell you
if you got it correct or not, would you like to play?""")
print("  ")
time.sleep(1)


#allow the user to only enter yes or no
menu_choice = input("please enter either yes or no: ").lower().strip()
while not menu_choice in VALID_CHOICE:
    menu_choice = input("please enter either 'yes' or 'no': ").lower().strip()



    

#validate their input
#print a message depending on their input
if menu_choice == "no":
    print("maybe you'll like to play some other time, goodbye")
elif menu_choice == "yes":
    print("let's begin")
        

    while continue_play:
    
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
        print("    ")
        print("what is",rand,operation,rand2)
        time.sleep(1)
        while not valid:
            try:
                question = float(input("please enter your answer: "))
                valid = True
            except ValueError:
                print("  ")

        if question==maths:
            print("correct")
            counter+=1
        else:
            print("incorrect, the right answer was",maths)
        count+=1



        
        
        #ask user if they want to play again
        #validate their input
        #if they select no then end game else print another maths question
        print("   ")
        play_again = input("do you want to play again, yes or no: ").lower().strip()
        while not play_again in VALID_CHOICE:
            play_again = input("do you want to play again, please enter either yes or no: ").lower().strip()
        if play_again == "no":
            print("hope you had fun, you got", counter,"right out of",count)
            continue_play = False
        else:
            valid = False
            
       
