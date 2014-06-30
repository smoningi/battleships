import urllib
import json

boardURL = "https://student.people.co/api/challenge/battleship/f51e7725e078/boards/test_board_1"
data = urllib.urlopen(boardURL).read()

print data

# shotURL = boardURL + "/A"
# data = urllib.urlopen(shotURL).read()

# response = json.loads(data)
pastHit = False

hitList = []

boardURL = "https://student.people.co/api/challenge/battleship/f51e7725e078/boards/live_board_1"
data = urllib.urlopen(boardURL).read()

print data
# for x in range(ord('A'), ord('K')):
# 	for y in range(1, 11):
# 		if (chr(x)+str(y)) not in hitList:
# 			shotURL = boardURL + "/"+ chr(x) + str(y)
# 			data = urllib.urlopen(shotURL).read()
# 			response = json.loads(data)
# 			hitList.append(chr(x) + str(y))
# 			print response["location"] + " " + str(response["is_hit"])
# 			if pastHit == True:
# 				if response["is_hit"] == False :
# 					shotURL = boardURL + "/"+ chr(x+1) + str(y-1)
# 					data = urllib.urlopen(shotURL).read()
# 					response = json.loads(data)
# 					hitList.append(chr(x+1) + str(y-1))
# 					print "Conditional hit: " + response["location"] + " " + str(response["is_hit"])
# 					increment = 1
# 					while response["is_hit"] == True:
# 						increment = increment + 1
# 						shotURL = boardURL + "/"+ chr(x+increment) + str(y-1)
# 						data = urllib.urlopen(shotURL).read()
# 						response = json.loads(data)
# 						hitList.append(chr(x+increment) + str(y-1))
# 						print "Vertical hit: " + response["location"] + " " + str(response["is_hit"])
# 					pastHit = False
# 			if response["is_hit"] == True:
# 				pastHit = True
# 		# if response["is_finished"] == True:
# 			# break;
print data
del hitList[:]
hitList = []
boardURL = "https://student.people.co/api/challenge/battleship/f51e7725e078/boards/live_board_2"
data = urllib.urlopen(boardURL).read()

print data
for x in range(ord('A'), ord('K')):
	for y in range(1, 11):
		if (chr(x)+str(y)) not in hitList:
			shotURL = boardURL + "/"+ chr(x) + str(y)
			data = urllib.urlopen(shotURL).read()
			response = json.loads(data)
			hitList.append(chr(x) + str(y))
			print response["location"] + " " + str(response["is_hit"])
			if pastHit == True:
				if response["is_hit"] == False :
					shotURL = boardURL + "/"+ chr(x+1) + str(y-1)
					data = urllib.urlopen(shotURL).read()
					response = json.loads(data)
					hitList.append(chr(x+1) + str(y-1))
					print "Conditional hit: " + response["location"] + " " + str(response["is_hit"])
					increment = 1
					while response["is_hit"] == True:
						increment = increment + 1
						shotURL = boardURL + "/"+ chr(x+increment) + str(y-1)
						data = urllib.urlopen(shotURL).read()
						response = json.loads(data)
						hitList.append(chr(x+increment) + str(y-1))
						print "Vertical hit: " + response["location"] + " " + str(response["is_hit"])
					pastHit = False
			if response["is_hit"] == True:
				pastHit = True
del hitList[:]
hitList = []
boardURL = "https://student.people.co/api/challenge/battleship/f51e7725e078/boards/live_board_3"
data = urllib.urlopen(boardURL).read()

print data
for x in range(ord('A'), ord('K')):
	for y in range(1, 11):
		if (chr(x)+str(y)) not in hitList:
			shotURL = boardURL + "/"+ chr(x) + str(y)
			data = urllib.urlopen(shotURL).read()
			response = json.loads(data)
			hitList.append(chr(x) + str(y))
			print response["location"] + " " + str(response["is_hit"])
			if pastHit == True:
				if response["is_hit"] == False :
					shotURL = boardURL + "/"+ chr(x+1) + str(y-1)
					data = urllib.urlopen(shotURL).read()
					response = json.loads(data)
					hitList.append(chr(x+1) + str(y-1))
					print "Conditional hit: " + response["location"] + " " + str(response["is_hit"])
					increment = 1
					while response["is_hit"] == True:
						increment = increment + 1
						shotURL = boardURL + "/"+ chr(x+increment) + str(y-1)
						data = urllib.urlopen(shotURL).read()
						response = json.loads(data)
						hitList.append(chr(x+increment) + str(y-1))
						print "Vertical hit: " + response["location"] + " " + str(response["is_hit"])
					pastHit = False
			if response["is_hit"] == True:
				pastHit = True

del hitList[:]
hitList = []
boardURL = "https://student.people.co/api/challenge/battleship/f51e7725e078/boards/live_board_4"
data = urllib.urlopen(boardURL).read()

print data
for x in range(ord('A'), ord('K')):
	for y in range(1, 11):
		if (chr(x)+str(y)) not in hitList:
			shotURL = boardURL + "/"+ chr(x) + str(y)
			data = urllib.urlopen(shotURL).read()
			response = json.loads(data)
			hitList.append(chr(x) + str(y))
			print response["location"] + " " + str(response["is_hit"])
			if pastHit == True:
				if response["is_hit"] == False :
					shotURL = boardURL + "/"+ chr(x+1) + str(y-1)
					data = urllib.urlopen(shotURL).read()
					response = json.loads(data)
					hitList.append(chr(x+1) + str(y-1))
					print "Conditional hit: " + response["location"] + " " + str(response["is_hit"])
					increment = 1
					while response["is_hit"] == True:
						increment = increment + 1
						shotURL = boardURL + "/"+ chr(x+increment) + str(y-1)
						data = urllib.urlopen(shotURL).read()
						response = json.loads(data)
						hitList.append(chr(x+increment) + str(y-1))
						print "Vertical hit: " + response["location"] + " " + str(response["is_hit"])
					pastHit = False
			if response["is_hit"] == True:
				pastHit = True

del hitList[:]
hitList = []
boardURL = "https://student.people.co/api/challenge/battleship/f51e7725e078/boards/live_board_5"
data = urllib.urlopen(boardURL).read()

print data
for x in range(ord('A'), ord('K')):
	for y in range(1, 11):
		if (chr(x)+str(y)) not in hitList:
			shotURL = boardURL + "/"+ chr(x) + str(y)
			data = urllib.urlopen(shotURL).read()
			response = json.loads(data)
			hitList.append(chr(x) + str(y))
			print response["location"] + " " + str(response["is_hit"])
			if pastHit == True:
				if response["is_hit"] == False :
					shotURL = boardURL + "/"+ chr(x+1) + str(y-1)
					data = urllib.urlopen(shotURL).read()
					response = json.loads(data)
					hitList.append(chr(x+1) + str(y-1))
					print "Conditional hit: " + response["location"] + " " + str(response["is_hit"])
					increment = 1
					while response["is_hit"] == True:
						increment = increment + 1
						shotURL = boardURL + "/"+ chr(x+increment) + str(y-1)
						data = urllib.urlopen(shotURL).read()
						response = json.loads(data)
						hitList.append(chr(x+increment) + str(y-1))
						print "Vertical hit: " + response["location"] + " " + str(response["is_hit"])
					pastHit = False
			if response["is_hit"] == True:
				pastHit = True