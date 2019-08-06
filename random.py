import os.path
import random, pyautogui, os

path = r'C:\Users\sarth\Pictures\Backgrounds'
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

print(num_files)

rand = random.randint(0, num_files - 1)
background = os.listdir(path)[rand]
rand = random.randint(0, num_files - 1)
lockscreen = os.listdir(path)[rand]

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.click(28, 1054)
pyautogui.click(30, 939)
pyautogui.click(1631, 301)
pyautogui.click(486, 691)

os.chdir('C:\\coding\\backgroundRandom')

pyautogui.click(154, 57)
pyautogui.typewrite(path)
pyautogui.press('enter')

pyautogui.click(280, 520)
pyautogui.typewrite(background)
pyautogui.press('enter')

pyautogui.click(79, 386)
pyautogui.click(482, 762)

pyautogui.click(154, 57)
pyautogui.typewrite(path)
pyautogui.press('enter')

pyautogui.click(280, 520)
pyautogui.typewrite(lockscreen)
pyautogui.press('enter')

pyautogui.click(1893, 20)
