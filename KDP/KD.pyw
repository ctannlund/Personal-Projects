import keyboard
import random
import time
import ctypes

a = input('Input value here:')


kernel32 = ctypes.WinDLL('kernel32')

user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']



while True:
    if keyboard.is_pressed('ctrl+k+c'):
        time.sleep(1.5)
        print('begun')
        while True:  # making a loop
            if keyboard.is_pressed('ctrl+x+j'):
                print('ended')
                break
            elif keyboard.is_pressed('a') or keyboard.is_pressed('b') or keyboard.is_pressed('c') or keyboard.is_pressed('d')\
                    or keyboard.is_pressed('e') or keyboard.is_pressed('f') or keyboard.is_pressed('g') or keyboard.is_pressed('h')\
                    or keyboard.is_pressed('i') or keyboard.is_pressed('j') or keyboard.is_pressed('k') or keyboard.is_pressed('l')\
                    or keyboard.is_pressed('m') or keyboard.is_pressed('n') or keyboard.is_pressed('o') or keyboard.is_pressed('p')\
                    or keyboard.is_pressed('q') or keyboard.is_pressed('r') or keyboard.is_pressed('s') or keyboard.is_pressed('t')\
                    or keyboard.is_pressed('u') or keyboard.is_pressed('v') or keyboard.is_pressed('w') or keyboard.is_pressed('x')\
                    or keyboard.is_pressed('y') or keyboard.is_pressed('z') or keyboard.is_pressed('0') \
                    or keyboard.is_pressed('1') or keyboard.is_pressed('2')or keyboard.is_pressed('3') or keyboard.is_pressed('4')\
                    or keyboard.is_pressed('5') or keyboard.is_pressed('6') or keyboard.is_pressed('7') or keyboard.is_pressed('8')\
                    or keyboard.is_pressed('9'):
                time.sleep(.1)
                chance = random.randint(1, 100)
                key = keyboard.read_key()
                print(str(chance))
                if chance <= 3:
                    keyboard.press_and_release('backspace')
                    keyboard.press_and_release('backspace')
                elif chance <= 5:
                    keyboard.write(key.upper())
                else:
                    pass
            elif keyboard.is_pressed('backspace'):
                time.sleep(.1)
                chance = random.randint(1, 100)
                print(str(chance))
                if chance <= 5:
                    letter_choice = letters[random.randint(0, 25)]
                    letter_choice2 = letters[random.randint(0, 25)]
                    letter_choice3 = letters[random.randint(0, 25)]
                    keyboard.write(letter_choice)
                    keyboard.write(letter_choice2)
                    keyboard.write(letter_choice3)
                else:
                    pass
            else:
                pass
