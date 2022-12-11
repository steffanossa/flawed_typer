from random import randint, choice, uniform
from time import sleep
import pydirectinput
import pyautogui
import numpy as np


kb_de = np.array([
		['' ,'1','2','3','4','5','6','7','8','9','0','ß', ''],
		['' ,'q','w','e','r','t','z','u','i','o','p','ü','+'],
		['' ,'a','s','d','f','g','h','j','k','l','ö','ä','#'],
		['<','y','x','c','v','b','n','m',',','.','-', '', '']
		])
kb_de_caps = np.array([
		['°','!','\"','§','$','%','&','/','(',')','=','?',  ''],
		['' ,'Q', 'W','E','R','T','Z','U','I','O','P','Ü', '*'],
		['' ,'A', 'S','D','F','G','H','J','K','L','Ö','Ä','\''],
		['>','Y', 'X','C','V','B','N','M',';',':','_', '',  '']
		])
kb_de_altgr = np.array([
		['°','1', '²','³','4','5','6','{','[',']','}','\\',  ''],
		['' ,'@', 'w','e','r','t','z','u','i','o','p','ü' , '~'],
		['' ,'a', 's','d','f','g','h','j','k','l','ö','ä' , '#'],
		['|','y', 'x','c','v','b','n','µ',',','.','-', '' ,  '']
		])
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

def get_neighbours(target, keyboard):
	neighbours = []
	for row in range(len(keyboard)):
		for  col in range(len(keyboard[row])):
			if keyboard[row][col] == target:
				#  left
				if col > 0:
					neighbours.append(keyboard[row][col - 1])
				# right
				if col < len(keyboard[row]) - 1:
					neighbours.append(keyboard[row][col + 1])
				# above
				if row > 0:
					neighbours.append(keyboard[row - 1][col])
					# above left
					if col > 0:
						neighbours.append(keyboard[row - 1][col - 1])
					# above right
					if col < len(keyboard[row]) - 1:
						neighbours.append(keyboard[row - 1][col + 1])
				# below
				if row <  len(keyboard) - 1:
					neighbours.append(keyboard[row + 1][col])
					# below left
					if col > 0:
						neighbours.append(keyboard[row + 1][col - 1])
					# below right
					if col < len(keyboard[row]) - 1:
						neighbours.append(keyboard[row + 1][col + 1])
	#  remove empty string
	neighbours = [neighbour for neighbour in neighbours if neighbour !=  '']
	return(neighbours)

def get_neighbours_np(target, keyboard):
    above = np.roll(keyboard, -1, axis=0)
    below = np.roll(keyboard, 1, axis=0)
    left = np.roll(keyboard, -1, axis=1)
    right = np.roll(keyboard, 1, axis=1)
    neighbours = np.stack((above, below, left, right))
    result = np.where(neighbours == target)
    return(neighbours)

a = get_neighbours_np("g", kb_de)
print(a)

def type_single_character(character, wpm, neighbours=[], accuracy=1, correct_rate=1, on_keyboard = True):
    if on_keyboard:
        error = randint(1, 100)
        correction = randint(1, 100)
        if error > accuracy * 100:
            faulty_character = choice(neighbours)
            pyautogui.write(faulty_character)
            #delay = 60 / (wpm * 5) * uniform(.9, 1.1)
            #sleep(delay)
            if correction > correct_rate * 100:
                return
            pydirectinput.press('backspace')
            #delay = 60 / (wpm * 5) * uniform(.9, 1.1)
            #sleep(delay/5)
    pyautogui.write(character)
    #delay = 60 / (wpm * 5) * uniform(.9, 1.1)
    #sleep(delay)
    return



def type(string, wpm = 80, accuracy = .95, correct_rate = 1.0, kb_layout = "de", all_lower = False):
    for character in string:
        on_keyboard = True
        neighbours = []
        if kb_layout == "de":
            if any(character in row for row in kb_de):
                neighbours = get_neighbours(character, kb_de)
            elif any(character in row for row in kb_de_caps):
                neighbours = get_neighbours(character, kb_de_caps)
            elif any(character in row for row in kb_de_altgr):
                neighbours = get_neighbours(character, kb_de_altgr)
            else:
                on_keyboard = False
            type_single_character(character, wpm, neighbours, accuracy, correct_rate, on_keyboard)




#test_string = "Ja, keine ahnung schreib halt einfach mal was oder so lol ey"
#sleep(2)
#type(test_string, 80, .97, .99, "de", False)
#a = get_neighbours("²", kb_de_altgr)
#print(a)
#a = "de"
#print(globals()[f"kb_{a}"])
#print([globals()[f"kb_{a}"], globals()[f"kb_{a}_caps"]])
#type_single_character("bb", 50, ["r","t","z","f","h","v","b","n"], 1, 1, True)
#for i in range(100):
#    type_single_character("G", 100, ["1","2","3"], 0.99, 0)

