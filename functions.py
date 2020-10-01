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

def move(A, player_number):
	while True:
		try:
			if player_number == 1:
				print("\nFirst player,")
			else:
				print("\nSecond player,")
			play = input("Where do you wanna play?\nEnter 'q' to quit\n")
			if (int(play) > 7 or int(play) < 1):
				os.system('cls')
				print("That move is out of the table!\n")
				show_table(A)
				continue
			if (A[0,int(play) - 1] != 0):
				os.system('cls')
				print("That column is already full!\n")
				show_table(A)
				continue
		except ValueError:
			if (play == 'q'):
				return play
			else:
				os.system('cls')
				print("That's not a number!\n")
				show_table(A)
				continue
		else:
			return play
			
def player_move(A, player_number, play):
	#Since we are choosing between 1 and 7 and arrays start in 0 we have to substract 1
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
	play = move(A, player_number)
	if play == 'q':
		#Returns keepPlaying
		return False
	else:
		keepPlaying = player_move(A, player_number, play)
		return keepPlaying