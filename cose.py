from lazyme.string import color_print
import time
import tkinter as tk
import requests
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from lazyme.string import color_print
import tqdm
from colorama import Fore, Back, Style

lel=print ("starting")
from tqdm import tqdm, trange
from time import sleep

with tqdm(total = 1000) as progressbar:
	for i in range(100):
		sleep(0.1)
		progressbar.update(10)

print ("print a number")
print ("1) fortnite")
print ("2) lol")
print ("3) password")
print ('4) when nukes fail (loic) [troll]')
print ("5) ashii downloader")
print ("6) prog per divertirsi")
print ("7) prog per divertirsi")
print ("#) codici di errore e restart")
print("else = restart")



lol = input()

if lol == "2":
  print ("lololololol")
  lel
elif lol == "3":
    _author_ = 'michele'

    print("insert password")
    user_name = input()

    if user_name == "password1!":
        print("passwords"
              ""
              ""
              ""
              ""
              ""
              "")
        lel

    elif user_name == "hacker":
        while 3 > 2:
            print("don't touch this program " + user_name)
    else:
        print(user_name + " wrong password")
    lel

elif lol == "4":
 print('its only a troll',)
 time.sleep(1)
 print("3")
 time.sleep(1)
 print("2")
 time.sleep(1)
 print("2")
 contatore = 0
 hotel = 10
 n = 0

 print("insert url if you readed the text before")
 user_name = input()
 user_input = input()

 while n == 0:
     print("package sent to ", user_name, + contatore, )
     contatore = contatore + 1
 if user_input == (1):
     n += 1
 lel

elif lol == "5":
    from tkinter import messagebox

    window = tk.Tk()
    window.geometry("900x550")
    window.title("ASCII ART DOWNLOADER")
    window.grid_columnconfigure(0, weight=1)


    def download_ascii():
        if text_input.get():
            user_input = text_input.get()
            payload = {"text": user_input}
            response = requests.get("http://artii.herokuapp.com/make",
                                    params=payload)
            text_response = response.text
        else:
            text_response = "Aggiungi una parola o una frase al campo input!"

        textwidget = tk.Text()
        textwidget.insert(tk.END, text_response)
        textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

        credits_label = tk.Label(window, text="ascii art by artii.herokuapp.com")
        credits_label.grid(row=4, column=0, sticky="S", pady=10)


    welcome_label = tk.Label(window,
                             text="Welcome! Aggiungi una parola o una frase da scaricare:",
                             font=("Helvetica", 15))
    welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

    text_input = tk.Entry()
    text_input.grid(row=1, column=0, sticky="WE", padx=10)

    download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
    download_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)

    if __name__ == "__main__":
        window.mainloop()
        lel

elif lol == "6":
    import random
    import tkinter as tk
    import glob, os

    window = tk.Tk()
    window.geometry("1900x1080")
    window.title("divertiti!")
    window.resizable(False, False)
    window.configure(background="blue")


    def first_print():
        text = (random.choice(["sasso   ", "carta   ", "forbice"]))
        text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 23), bg="blue")
        text_output.grid(row=1, column=2, sticky="W")


    def second_function():
        text = "schiaccia la x"
        text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
        text_output.grid(row=2, column=2, padx=50, sticky="W")


    def third_function():
        text = "00100101010100111000101011010110101011010101010101010101010101010101010101010"

        text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))


    def fourth_function():
        while 2 < 3:
            text = "11"


    def fourth_function():
        while 3 > 2:
            text = "schiaccia la x for download youtube videos"
        text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
        text_output.grid(row=5, column=2, padx=50, sticky="W")


    first_button = tk.Button(text="sasso carta forbice", command=first_print)
    first_button.grid(row=1, column=1, sticky="W")

    second_button = tk.Button(text="exit", command=second_function)
    second_button.grid(row=2, column=1, pady=20, sticky="W")

    third_button = tk.Button(text="im hacker", command=third_function)
    third_button.grid(row=3, column=1, pady=20, sticky="W")

    fourth_button = tk.Button(text="crash", command=fourth_function)
    fourth_button.grid(row=4, column=1, pady=20, sticky="W")
    if __name__ == "__main__":

        window.mainloop()
        lel


elif lol == "#":
    print("1")
    print("2")
    print("3")
    print("restart", color='red')

else:
    lel


lil = input()


if lil == ("restart"):
    lel
elif lil == ("1"):
    print("processo non riuscito")
    lel
elif lil == ("2"):
    print("boh")
    lel
elif lil == ("3"):
    print("spegni e riavvia funziona sempre")
    lel


print ("starting")
from tqdm import tqdm, trange
from time import sleep

with tqdm(total = 100) as progressbar:
	for i in range(10):
		sleep(0.1)
		progressbar.update(10)

print (Fore.GREEN + "print a number")
print (Fore.GREEN + "1) fortnite")
print (Fore.GREEN + "2) lol")
print (Fore.GREEN + "3) password")
print (Fore.GREEN + '4) when nukes fail (loic) [troll]')
print (Fore.GREEN + "5) ashii downloader")
print (Fore.GREEN + "6) prog per divertirsi")
print (Fore.GREEN + "7) prog per divertirsi")
print (Fore.GREEN + "#) codici di errore e restart")

lol = input()

if lol == "2":
  print ("lololololol")
  lel
elif lol == "3":
    _author_ = 'michele'

    print("insert password")
    user_name = input()

    if user_name == "password1!":
        print("passwords"
              ""
              ""
              ""
              ""
              ""
              "")

    elif user_name == "hacker":
        while 3 > 2:
            print("don't touch this program " + user_name)
    else:
        print(user_name + " wrong password")
    lel

elif lol == "4":
 print('its only a troll', color='red')
 time.sleep(1)
 print("3")
 time.sleep(1)
 print("2")
 time.sleep(1)
 print("2")
 contatore = 0
 hotel = 10
 n = 0


 print("insert url if you readed the text before")
 user_name = input()
 user_input = input()

 while n == 0:
     print("package sent to ", user_name, + contatore, )
     contatore = contatore + 1
 if user_input == (1):
     n += 1
 lel

elif lol == "5":
    from tkinter import messagebox

    window = tk.Tk()
    window.geometry("900x550")
    window.title("ASCII ART DOWNLOADER")
    window.grid_columnconfigure(0, weight=1)


    def download_ascii():
        if text_input.get():
            user_input = text_input.get()
            payload = {"text": user_input}
            response = requests.get("http://artii.herokuapp.com/make",
                                    params=payload)
            text_response = response.text
        else:
            text_response = "Aggiungi una parola o una frase al campo input!"

        textwidget = tk.Text()
        textwidget.insert(tk.END, text_response)
        textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

        credits_label = tk.Label(window, text="ascii art by artii.herokuapp.com")
        credits_label.grid(row=4, column=0, sticky="S", pady=10)


    welcome_label = tk.Label(window,
                             text="Welcome! Aggiungi una parola o una frase da scaricare:",
                             font=("Helvetica", 15))
    welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

    text_input = tk.Entry()
    text_input.grid(row=1, column=0, sticky="WE", padx=10)

    download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
    download_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)

    if __name__ == "__main__":
        window.mainloop()
        lel

elif lol == "6":
    import random
    import tkinter as tk
    import glob, os

    window = tk.Tk()
    window.geometry("1900x1080")
    window.title("divertiti!")
    window.resizable(False, False)
    window.configure(background="blue")


    def first_print():
        text = (random.choice(["sasso   ", "carta   ", "forbice"]))
        text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 23), bg="blue")
        text_output.grid(row=1, column=2, sticky="W")


    def second_function():
        text = "schiaccia la x"
        text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
        text_output.grid(row=2, column=2, padx=50, sticky="W")


    def third_function():
        text = "00100101010100111000101011010110101011010101010101010101010101010101010101010"

        text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))


    def fourth_function():
        while 2 < 3:
            text = "11"


    def fourth_function():
        while 3 > 2:
            text = "schiaccia la x for download youtube videos"
        text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
        text_output.grid(row=5, column=2, padx=50, sticky="W")


    first_button = tk.Button(text="sasso carta forbice", command=first_print)
    first_button.grid(row=1, column=1, sticky="W")

    second_button = tk.Button(text="exit", command=second_function)
    second_button.grid(row=2, column=1, pady=20, sticky="W")

    third_button = tk.Button(text="im hacker", command=third_function)
    third_button.grid(row=3, column=1, pady=20, sticky="W")

    fourth_button = tk.Button(text="crash", command=fourth_function)
    fourth_button.grid(row=4, column=1, pady=20, sticky="W")
    if __name__ == "__main__":

        window.mainloop()
        lel




elif lol == "#":
    print("1")
    print("2")
    print("3")
    print("restart", color='red')

else:
    lel

lil = input()


if lil == ("restart"):
    lel
elif lil == ("1"):
    print("processo non riuscito")
    lel
elif lil == ("2"):
    print("boh")
    lel
elif lil == ("3"):
    print("spegni e riavvia funziona sempre")
    lel