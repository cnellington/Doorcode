from graphics import *
from sqlalchemy import create_engine
import os

# ;10016370535670?
# caleb = student("caleb", val, "Phi Delt", 3)

class event:
	houses_ = []
	whitelist_ = {}
	affiliation_ = {}
	db_ = None
	# TODO: add dates 

	def __init__(self, houses, db):
		self.houses_ = houses
		self.db_ = db
		for house in self.houses_:
			query = "SELECT * FROM uwgreeks WHERE house=\'" + house + "\'";
			result = self.db_.execute(query)
			for row in result:
				self.whitelist_[row[0]] = row[1]
				self.affiliation_[row[0]] = row[2]

	def validate(self, student_id):
		return None



class student:
	name = "default"
	st_id = -1
	house = "non-greek"
	year = -1

	def __init__(self, name_in, st_id_in, house_in, year_in):
		name = name_in
		st_id = st_id_in
		house = house_in
		year = year_in




def parseCode(code):
	return code[4:11]

def main():
	# Event whitelist
	whitelist = {}

	# Create DB
	dcuser = os.environ.get('DCUSER')
	dcpass = os.environ.get('DCPASS')
	dcip   = os.environ.get('DCIP')
	dcdb   = os.environ.get('DCDB')
	db_connection = "postgres://{}:{}@{}/{}"
	db_connection = db_connection.format(dcuser, dcpass, dcip, dcdb)
	db = create_engine(db_connection)

	# Add houses to the whitelist
	houses = {'Phi Delts', 'Sigma Chi'}
	party = event(houses, db)
	print(party.validate())

	exit()
	# Create Graphics
	win = GraphWin("DOORCODE", 800, 800)
	win.setBackground("White")
	while(True):
		scan = input()
		student_id = parseCode(scan)
		if(scan in whitelist.keys()):
			win.setBackground("Green")
			print(whitelist[doorcode])
		else:
			win.setBackground("Red")
		# message = Text(Point(10, 0), str(whitelist[doorcode]))
		time.sleep(.5)
		win.setBackground("White")


main()
