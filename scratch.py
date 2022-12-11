from random import randint, choice, uniform, choices
from time import sleep
import pydirectinput
import pyautogui



kb_de = [
		['' ,'1','2','3','4','5','6','7','8','9','0','ß', ''],
		['' ,'q','w','e','r','t','z','u','i','o','p','ü','+'],
		['' ,'a','s','d','f','g','h','j','k','l','ö','ä','#'],
		['<','y','x','c','v','b','n','m',',','.','-', '', '']
		]
kb_de_caps = [
		['°','!','\"','§','$','%','&','/','(',')','=','?',  ''],
		['' ,'Q', 'W','E','R','T','Z','U','I','O','P','Ü', '*'],
		['' ,'A', 'S','D','F','G','H','J','K','L','Ö','Ä','\''],
		['>','Y', 'X','C','V','B','N','M',';',':','_', '',  '']
		]
kb_de_altgr = [
		['°','1', '²','³','4','5','6','{','[',']','}','\\',  ''],
		['' ,'@', 'w','e','r','t','z','u','i','o','p','ü' , '~'],
		['' ,'a', 's','d','f','g','h','j','k','l','ö','ä' , '#'],
		['|','y', 'x','c','v','b','n','µ',',','.','-', '' ,  '']
		]
kb_us = [
		['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',  '-', '=',  ''],
 		['' , 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',  '[', ']','\\'],
 		['' , 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'',  '',  ''],
 		['' , 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',   '',  '',  ''],
 		['' ,  '', ' ', ' ', ' ', ' ',' ' ,' ' ,' ' ,  '',  '',   '',  '',  '']
 		]
kb_us_caps = [
			['~','!', '@', '#', '$', '%',  '', '&', '*', '(', ')', '_', '+', ''],
 			[ '','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}','|'],
 			[ '','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';','\'',  '', ''],
 			[ '','Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?',  '',  '', ''],
 			['' , '', ' ', ' ', ' ', ' ',' ' ,' ' ,' ' ,  '',  '',  '',  '', '']
 			]
kb_us_altgr = [
		['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',  '-', '=',  ''],
 		['' , 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',  '[', ']','\\'],
 		['' , 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'',  '',  ''],
 		['' , 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',   '',  '',  ''],
 		['' ,  '', ' ', ' ', ' ', ' ',' ' ,' ' ,' ' ,  '',  '',   '',  '',  '']
		]
kb_uk = [
		[ '`','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-','='],
 		[  '','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[',']'],
 		[  '','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';','\'','#'],
 		['\\','z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',  '', ''],
 		[  '', '', ' ', ' ', ' ', ' ',' ' ,' ' ,' ' ,  '',  '',  '', '']
 		]
kb_uk_caps = [
		[ '','!', '"', '£', '$', '%',  '', '&', '*', '(', ')', '_', '+'],
		[ '','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}'],
 		[ '','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '@', '~'],
 		['|','Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?',  '',  ''],
 		['' ,  '',' ', ' ', ' ', ' ',' ' ,' ' ,' ' ,  '',  '',  '',  '']
		]
kb_uk_altgr = [
		[ '','!', '"', '£', '$', '%',  '', '&', '*', '(', ')', '_', '+'],
		[ '','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}'],
 		[ '','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '@', '~'],
 		['|','Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?',  '',  ''],
 		['' ,  '',' ', ' ', ' ', ' ',' ' ,' ' ,' ' ,  '',  '',  '',  '']
		]
kb_fr = [
		['²', '&', 'é', '"', '\'', '(', '-', 'è', '_', 'ç', 'à', ')', '='],
 		[ '', 'a', 'z', 'e',  'r', 't', 'y', 'u', 'i', 'o', 'p', '^', '$'],
 		[ '', 'q', 's', 'd',  'f', 'g', 'h', 'j', 'k', 'l', 'm', 'ù', '*'],
 		['<', 'w', 'x', 'c',  'v', 'b', 'n', ',', ';', ':', '!',  '',  ''],
 		['' ,  '', ' ', ' ', ' ', ' ',  ' ',' ' ,' ' ,  '',  '',  '',  '']
		]
kb_fr_caps = [
			['²','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '°', '+'],
         	[ '','A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '^', '£'],
         	[ '','Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', '%', 'µ'],
          	['>','W', 'X', 'C', 'V', 'B', 'N', '?', ',', ';', ':', '$',  ''],
          	['' , '', ' ', ' ', ' ', ' ', ' ',' ' ,' ' ,  '',  '',  '',  '']
          	]
kb_fr_altgr = [
		['²', '&', '~', '#', '{', '[', '|', 'è','\\', 'ç', '@', ']', '}'],
 		[ '', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '^', '$'],
 		[ '', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'ù', '*'],
 		['<', 'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':', '!',  '',  ''],
 		['' ,  '', ' ', ' ', ' ', ' ', ' ',' ' ,' ' ,  '',  '',  '',  '']
		]
pyautogui.write()
def get_neighbours(target, array):
	neighbours = []
	for row in range(len(array)):
		for  col in range(len(array[row])):
			if array[row][col] == target:
				#  left
				if col > 0:
					neighbours.append(array[row][col - 1])
				# right
				if col < len(array[row]) - 1:
					neighbours.append(array[row][col + 1])
				# above
				if row > 0:
					neighbours.append(array[row - 1][col])
					# above left
					if col > 0:
						neighbours.append(array[row - 1][col - 1])
					# above right
					if col < len(array[row]) - 1:
						neighbours.append(array[row - 1][col + 1])
				# below
				if row <  len(array) - 1:
					neighbours.append(array[row + 1][col])
					# below left
					if col > 0:
						neighbours.append(array[row + 1][col - 1])
					# below right
					if col < len(array[row]) - 1:
						neighbours.append(array[row + 1][col + 1])
	#  remove empty strings
	neighbours = [neighbour for neighbour in neighbours if neighbour !=  '']
	return(neighbours)

def get_neighbours2(target, array):
	neighbours = set()
	
	# Loop through each element in the array
	for row in range(len(array)):
		for col in range(len(array[row])):
			# Check if the current element is the target
			if array[row][col] == target:
				# Add the neighbors to the set
				if col > 0:
					neighbours.add(array[row][col - 1])
				if col < len(array[row]) - 1:
					neighbours.add(array[row][col + 1])
				if row > 0:
					neighbours.add(array[row - 1][col])  

def get_neighbours3(target, array):
	neighbours = []
	
	# Loop through each element in the array
	for row in range(len(array)):
		for col in range(len(array[row])):
			# Check if the current element is the target
			if array[row][col] == target:
				# Add the neighbors to the list
				if col > 0:
					neighbours.append(array[row][col - 1])
				if col < len(array[row]) - 1:
					neighbours.append(array[row][col + 1])
				if row > 0:
					neighbours.append(array[row - 1][col])
					if col > 0:
						neighbours.append(array[row - 1][col - 1])
					if col < len(array[row]) - 1:
						neighbours.append(array[row - 1][col + 1])
				if row <  len(array) - 1:
					neighbours.append(array[row + 1][col])
					if col > 0:
						neighbours.append(array[row + 1][col - 1])
					if col < len(array[row]) - 1:
						neighbours.append(array[row + 1][col + 1])
	
	# Remove empty strings
	neighbours = [neighbour for neighbour in neighbours if neighbour != '']
	return neighbours



def type_single_character(character, wpm, neighbours=[], accuracy=1, correct_rate=1, on_keyboard = True):
    if on_keyboard:
        error = randint(1, 100)
        correction = randint(1, 100)
        if error > accuracy * 100:
            faulty_character = choice(neighbours)
            pyautogui.write(faulty_character)
            delay = 60 / (wpm * 5) * uniform(.9, 1.1)
            sleep(delay)
            if correction > correct_rate * 100:
                return
            pydirectinput.press('backspace')
            delay = 60 / (wpm * 5) * uniform(.9, 1.1)
            sleep(delay/5)
    pyautogui.write(character)
    delay = 60 / (wpm * 5) * uniform(.9, 1.1)
    sleep(delay)
    return



def type(string, wpm = 80, accuracy = .95, correct_rate = 1.0, kb_layout = "de", all_lower = False):
    for character in string:
        on_keyboard = True
        neighbours = []
        if kb_layout == "de":
            if any(character in row for row in kb_de):
                neighbours = get_neighbours3(character, kb_de)
            elif any(character in row for row in kb_de_caps):
                neighbours = get_neighbours3(character, kb_de_caps)
            elif any(character in row for row in kb_de_altgr):
                neighbours = get_neighbours3(character, kb_de_altgr)
            else:
                on_keyboard = False
            type_single_character(character, wpm, neighbours, accuracy, correct_rate, on_keyboard)




test_string = "Ja, keine ahnung schreib halt einfach mal was oder so lol ey"
sleep(2)
type(test_string, 888, 1, 1, "de", False)
#a = get_neighbours("²", kb_de_altgr)
#print(a)
#a = "de"
#print(globals()[f"kb_{a}"])
#print([globals()[f"kb_{a}"], globals()[f"kb_{a}_caps"]])
#type_single_character("bb", 50, ["r","t","z","f","h","v","b","n"], 1, 1, True)
#for i in range(100):
#    type_single_character("G", 100, ["1","2","3"], 0.99, 0)

def getTuple(char):
    k = [(index, row.index(char)) for index, row in enumerate(kb_de) if char in row]
    print(k)
    arr = kb_de
    if len(k) == 0:
        k = [(index, row.index(char)) for index, row in enumerate(kb_de_caps) if char in row]
        arr = kb_de_caps
    if len(k) == 0:
        k = [(index, row.index(char)) for index, row in enumerate(kb_de_altgr) if char in row]
        arr = kb_de_altgr
    if len(k) == 0:
        #print("Please provide English text only")
        return (2, 0), arr
    return k[0], arr

def getAllNeighbors(tup, arr, dist=1):
    bounds = [len(i) - 1 for i in arr]
    xs = []
    ys = []
    tups = []
    r = list(range(dist + 1))
    r += [-1 * k for k in r if not k == 0]
    for i in r:
        val = tup[0] + i
        if val <= 4 and val >= 0:
            xs.append(val)
        val = tup[1] + i
        ys.append(val)
    for k in range(len(xs)):
        tups += [(xs[k], ys[i]) for i in range(len(ys)) if ys[i] <= bounds[xs[k]] and ys[i] >= 0]
    return tups

def get_character(position, keyboard):
    return keyboard[position[0]][position[1]]







def get_pos_kb(char):
    k = [(index, row.index(char)) for index, row in enumerate(kb_de) if char in row]
    print(k)
    arr = kb_de
    if len(k) == 0:
        k = [(index, row.index(char)) for index, row in enumerate(kb_de_caps) if char in row]
        arr = kb_de_caps
    if len(k) == 0:
        k = [(index, row.index(char)) for index, row in enumerate(kb_de_altgr) if char in row]
        arr = kb_de_altgr
    if len(k) == 0:
        #print("Please provide English text only")
        return (2, 0), arr
    return k[0], arr

