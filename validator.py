from graphics import *

# ;10016370535670?
# caleb = student("caleb", val, "Phi Delt", 3)
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

whitelist = {'1637053': 'Joe Schmoe, Phi Delts'}

def parseCode(code):
	return code[4:11]

def main():
	win = GraphWin("DOORCODE", 800, 800)
	win.setBackground("White")
	while(True):
		code = input()
		doorcode = parseCode(code)
		if(doorcode in whitelist.keys()):
			win.setBackground("Green")
			print(whitelist[doorcode])
		else:
			win.setBackground("Red")
		time.sleep(.5)
		win.setBackground("White")


main()
