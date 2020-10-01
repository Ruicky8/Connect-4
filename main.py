from functions import *

A = np.zeros((6,7))
counter = 0
keepPlaying = True
#-------------------------------------------------------------------------------
show_table(A)
while keepPlaying:
	if counter % 2 == 0:
		keepPlaying = player(A, 1)
	elif counter % 2 != 0:
		keepPlaying = player(A, 2)
	counter += 1
	
