import pyautogui
import time
word= "hi"#what word you want to loop
time.sleep(4)
#^ time before loop starts
i = 0
while i < 10:#how many loops
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    i = i+1
    time.sleep(0.4)#time inbetween each loop