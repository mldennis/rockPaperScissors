'''
Created on Nov 3, 2018

@author: ITAUser

OBJECTIVE:
We want to create a rock, paper, scissors game

ALGORITHM:
First, we will create code that checks who won each round
Second, we will create code that takes the input(choices) of the user
Third, we will create code that takes the 'input'(choices) of the computer
Fourth, we will create code that checks if the user wants to quit, or if the user doesn't enter one of the options(rock, paper, or scissors)
Fifth, we will loop each round
Sixth, we will add statements at the end and the beginning that welcome the user
Finally, we will loop the whole game, so that the user can keep playing until they choose to quit
'''

'''
rock = 1
scissors = 2
paper = 3
'''
import random

keepPlaying = True
while(keepPlaying):
    print("Welcome to Rock Paper Scissors")
    print("Best two out of three. Press 'q' to quit")
    cpuScore= 0
    humanScore= 0
    
    while(humanScore < 2 and cpuScore < 2):
        choice=input ("please chose(Rock, Paper, Scissors):")
        cpuChoice = random.randint(1,3)
        
        if(choice.lower() == 'q'):
                keepPlaying = False
                break
        #this if statement checks if the computer and human draw
        elif((choice.lower() == 'rock' and cpuChoice == 1) or (choice.lower() == 'scissors' and cpuChoice == 2) or (choice.lower() == 'paper' and cpuChoice == 3)):
            print("DRAW")
            print("Human: " + humanScore.__str__() + " CPU: " + cpuScore.__str__())
        #this if statement checks if the human wins
        elif((choice.lower() == 'rock' and cpuChoice == 2) or (choice.lower() == 'scissors' and cpuChoice == 3) or (choice.lower() == 'paper' and  cpuChoice == 1)):
            humanScore = humanScore + 1
            print("Human: " + humanScore.__str__() + " CPU: " + cpuScore.__str__())
        #this if statement checks if the computer wins
        elif((choice.lower() == 'rock' and cpuChoice == 3) or (choice.lower() == 'scissors' and cpuChoice == 1) or (choice.lower() == 'paper' and cpuChoice == 2)):
            cpuScore = cpuScore + 1
            print("Human: " + humanScore.__str__() + " CPU: " + cpuScore.__str__())
        else: 
            print("Not an option, try again")
    print("Thanks for playing!")
    if(humanScore ==2):
        print("You Win!!!")
    if(cpuScore== 2):
        print("You Lose!!!")
    print("Human: " + humanScore.__str__() +  "CPU:" + cpuScore.__str__())
    
    #testme
