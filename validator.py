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
		return student_id in self.whitelist_.keys()

	def get_name(self, student_id):
		return self.whitelist_[student_id] + ", " + self.affiliation_[student_id]

def parseCode(code):
	return code[4:11]
