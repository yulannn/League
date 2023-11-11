from tkinter import *
from tkinter import ttk
import subprocess
import time
import pyautogui
import sys
import os

emails = []
password = []
pseudos = []

if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "logoriot.ico")
else:
    icon_path = "logoriot.ico"

root = Tk()
root.geometry("200x200")
root.resizable(False, False)
root.iconbitmap(default=icon_path)

lol_executable_path = r'C:\Riot Games\League of Legends\LeagueClient.exe'
def startCompte():
    indiceCompte = pseudos.index(compteSelect.get())
    mail = emails[indiceCompte]
    pseudo = pseudos[indiceCompte]
    mdp = password[indiceCompte]

    subprocess.Popen([lol_executable_path])

    time.sleep(8)

    pyautogui.write(mail)
    pyautogui.press('tab')
    pyautogui.write(mdp)
    pyautogui.press('enter')

    time.sleep(6)

    x , y = 200 , 340

    pyautogui.click(x , y)

    b , v = 200, 350

    time.sleep(3)

    pyautogui.click(b , v)

compteSelect = StringVar()

combobox = ttk.Combobox(root, textvariable=compteSelect, values=pseudos)
combobox.pack()
combobox.place(x=10, y=40)

button = Button(root, text="Valider", command=startCompte)
button.pack()
button.place(x=60, y=70)


root.mainloop()