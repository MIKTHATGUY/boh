from pynput.keyboard import Key,Controller
import time



Keyboard = Controller()






n = 1
m = int(input("quante volte?: "))
s = float(input("ogni quanto?: "))
sus = (input("cosa "))
print("tra 10s arriverà lo  spam")


time.sleep(10)
while n < m:
    for letter in sus:
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    n = n + 1
    time.sleep(s)
    print (n , "mandati", "ne mancano", m - n)

for letter in "ho finito di spammare :)":
    Keyboard.press(letter)
    Keyboard.release(letter)
Keyboard.press(Key.enter)

Keyboard.release(Key.enter)
print("----------------")
print(" processo finito")
print("----------------")
























