import numpy as np
import os
import math

#6x7 zeros matrix in order to play
#0 will be empty, 1 the first player, 2 the second player
def show_table(A):
	print(A)
	print(" ----------------------")
	print(" [1. 2. 3. 4. 5. 6. 7.]")

def who_wins(A,i,j):
	if A[i,j] == 1:
		print("Player 1 wins!\n")
	elif A[i,j] == 2:
		print("Player 2 wins!\n")
	return False
		
def check_winner(A):
	#There is a drawing which explains this properly
	#vertical
	keepPlaying = True
	for i in range(0,3):
		for j in range(0,7):
			if (A[i,j] == A[i+1,j] == A[i+2,j] == A[i+3,j] == 1
			or  A[i,j] == A[i+1,j] == A[i+2,j] == A[i+3,j] == 2):
				keepPlaying = who_wins(A,i,j)
	#horizontal
	for i in range(0,6):
		for j in range(0,4):
			if (A[i,j] == A[i,j+1] == A[i,j+2] == A[i,j+3] == 1
			or  A[i,j] == A[i,j+1] == A[i,j+2] == A[i,j+3] == 2):
				keepPlaying = who_wins(A,i,j)		
	#increasing diagonal
	for i in range(0,3):
		for j in range(3,7):
			if (A[i,j] == A[i+1,j-1] == A[i+2,j-2] == A[i+3,j-3] == 1
			or  A[i,j] == A[i+1,j-1] == A[i+2,j-2] == A[i+3,j-3] == 2):
				keepPlaying = who_wins(A,i,j)
	#decreasing diagonal
	for i in range(0,3):
		for j in range(0,4):
			if (A[i,j] == A[i+1,j+1] == A[i+2,j+2] == A[i+3,j+3] == 1
			or  A[i,j] == A[i+1,j+1] == A[i+2,j+2] == A[i+3,j+3] == 2):
				keepPlaying = who_wins(A,i,j)
	return keepPlaying
	
def check_errors(A, test):
	#Check if play is a string or a blank input
	try:
		int(test)+1
		test_1 = 1
	except ValueError:
		if test == 'q':
			return 2
		else:
			os.system('cls')
			print("That's not a number!")
			return 0
	#Check if play is 0
	try:
		1/int(test)
		test_2 = 1
	except ZeroDivisionError:
		os.system('cls')
		print("That move is out of the table!")
		return 0
	#Check if play is a negative number
	try:
		math.sqrt(int(test))
		test_3 = 1
	except ValueError:
		os.system('cls')
		print("That move is out of the table!")
		return 0
	#Check if a is between 1 and 7
	try:
		B = np.zeros((1,7))
		j = int(test) - 1
		B[0,j] = 1
		test_4 = 1
	except IndexError:
		os.system('cls')
		print("That move is out of the table!")
		return 0
	#Check if the column is already full
	if A[0,int(test)-1] != 0:
		os.system('cls')
		print("That column is already full!")
		return 0 
	else:
		test_5 = 1
	if test_1 == test_2 == test_3 == test_4 == test_5 == 1:
		return 1
			
def player_move(A, player_number, play):
	#Since we are choosing between 1 and 7 and arrays start in 0 we have to add 1
	j = int(play) - 1
	#j will be the column the player wanna play
	for i in range(5,-1,-1):
		if A[i,j] == 0:
			A[i,j] = player_number
			break
			
	os.system('cls')
	keepPlaying = check_winner(A)
	show_table(A)
	return keepPlaying

def player(A, player_number):
	keepPlaying = True
	if player_number == 1:
		print("\nFirst player,")
	else:
		print("\nSecond player,")
	play = input("Where do you wanna play?\nEnter 'q' to quit\n")
	error = check_errors(A, play)
	if error == 1:
		keepPlaying = player_move(A, player_number, play)
		return keepPlaying
	elif error == 0:	
		print("Try again...\n")
		show_table(A)
		player(A, player_number)
	elif error == 2:
		keepPlaying = False
		return keepPlaying
