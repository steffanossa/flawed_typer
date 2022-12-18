from random import randint, choice, uniform, choices
from time import sleep
import win32api
import win32.lib.win32con as win32con
from keyboards import *
from vk_codes import VK_CODE

# problem w special chars, layouts need work
# all_lower not implemented yet
# set wpm will be hit +/- 10% approx (i think)



# hard coded variables
delay_constant = 50
swing = (.25 , 1.75)
swing_space = (1.11, 1.37)

def get_neighbours(target, array):
	neighbours = []
	for row in range(len(array)):
		for  col in range(len(array[row])):
			if array[row][col] == target:
				# left
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


def key_press(button: str):
	if button.isupper():
		button = button.lower()
		win32api.keybd_event(VK_CODE['shift'],0,0,0)
		win32api.keybd_event(VK_CODE[button], 0,0,0)
		win32api.keybd_event(VK_CODE['shift'], 0,  win32con.KEYEVENTF_KEYUP, 0)
	else:
		win32api.keybd_event(VK_CODE[button], 0,0,0)


def type_single_character(character, wpm, neighbours=[], accuracy=1, correct_rate=1, on_keyboard = True):
    if on_keyboard:
        error = randint(1, 100)
        correction = randint(1, 100)
        if error > accuracy * 100:
            faulty_character = choice(neighbours)
            key_press(faulty_character)
            delay = delay_constant / (wpm * 5) * uniform(swing)
            sleep(delay)
            if correction > correct_rate * 100:
                return
            key_press("backspace")
            delay = delay_constant / (wpm * 5) * uniform(swing)
            sleep(delay/5)
    key_press(character)
    delay = delay_constant / (wpm * 5) * uniform(swing)
	# extra delay after spaces
    if character == " ":
        delay = delay * uniform(swing_space)
    sleep(delay)
    return


def type(string, wpm = 80, accuracy = .95, correct_rate = 1.0, kb_layout = "de", all_lower = False):
	if all_lower:
		string = string.lower()
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