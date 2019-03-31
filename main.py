from graphics import *
from sqlalchemy import create_engine
import os
from gui import interface
from validator import event, parseCode

def main():

	# Create DB
	
	db_connection = "postgres://{}:{}@{}/{}"
	db_connection = db_connection.format(dcuser, dcpass, dcip, dcdb)
	db = create_engine(db_connection)

	gui = interface()
	# Add houses to the whitelist
	houses = {'Phi Delts', 'Sigma Chi'}
	party = event(houses, db)

	print("hello")
	# Create Graphics
	win = GraphWin("DOORCODE", 800, 800)
	win.setBackground("White")
	while(True):
		scan = input()
		student_id = parseCode(scan)
		if(party.validate(student_id)):
			win.setBackground("Green")
			print(party.get_name(student_id))
		else:
			win.setBackground("Red")
			print(student_id + " is not on the guestlist")
		# message = Text(Point(10, 0), str(whitelist[doorcode]))
		time.sleep(.5)
		win.setBackground("White")


main()
