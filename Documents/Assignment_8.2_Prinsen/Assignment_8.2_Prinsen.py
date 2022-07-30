# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Ryan Prinsen>
# Creation Date: <07/30/2022>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
#Indentation issue with the while statement below.
	while cave != '1' and cave != '2':
#I would suggest defining the variable with the input function. "cave = input('Which cave will...')
		print('Which cave will you go into? (1 or 2)')
		cave = input()

#The variable below should be "cave".
	return caves

#It may be a good idea to space some of this code out to make it not so jumbled.
def checkCave(chosenCave):
#Indentation issues in the next several lines.
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#Print statement is missing parentheses below.
		print 'Gobbles you down in one bite!' 

playAgain = 'yes'
#The while statement should have two equal signs rather than one in the line below.
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
#The line below should be chooseCave not choosecave.
	caveNumber = choosecave()
	checkCave(caveNumber)
    
#Could also have playAgain = input("Do you want...").
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
#The line below should say "playing" not planing.
		print("Thanks for planing")

