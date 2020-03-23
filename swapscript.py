import time
from subprocess import check_call
from subprocess import call
import os


board_names = ["MLB","NHL"] #commands to run various boards/processes
sleep_time  = 120 # seconds

def run(board_state):
	time.sleep(sleep_time)
	if board_state == len(board_names): # resets counter
		board_state = 0
	y = 0
	while y < len(board_names):  # iterates through all boards except selected and kills them
		if y != board_state:
			execcommand = "sudo supervisorctl stop %s" % board_names[y]
			os.system(execcommand)
		y = y + 1
	execcommand = "sudo supervisorctl start %s" % board_names[x]
	os.system(execcommand)  # runs the board
	board_state += 1
	
	run(board_state)
