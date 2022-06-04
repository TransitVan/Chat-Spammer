#imports, pyautogui allows us to take control and type with the keyboard via the script and Colorama lets us add some style to our terminal.
import pyautogui
import colorama
from colorama import Fore, Back, Style
import time

#ascii art, purely here for looks and credits.
print(f"{Fore.MAGENTA}                                                                   ")
print(f"{Fore.MAGENTA}  ██╗░░░░░░█████╗░██╗░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███████╗")
print(f"{Fore.MAGENTA}  ██║░░░░░██╔══██╗██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝")
print(f"{Fore.MAGENTA}  ██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░██║░░░░░███████║██║░░╚═╝█████╗░░")
print(f"{Fore.MAGENTA}  ██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░██║░░░░░██╔══██║██║░░██╗██╔══╝░░")
print(f"{Fore.MAGENTA}  ███████╗╚█████╔╝░░╚██╔╝░░███████╗███████╗██║░░██║╚█████╔╝███████╗")
print(f"{Fore.MAGENTA}  ╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝")
print(f"{Fore.MAGENTA}                                                                   ")
print(f"{Fore.MAGENTA}  --------            Made by Transit Van#0393             --------")

#variable setup, here to show what to spam and how long to wait.
print(f"{Fore.MAGENTA}  What Do you want to spam? ")
text = input("")
print(f"{Fore.MAGENTA}  How Long Should We Wait?  ")
wait = int(input(""))
print(f"{Fore.MAGENTA}  How Many Times To Spam?  ")
times = int(input(""))

#main script, here we setup the spammer and make it loop.
time.sleep(4)
for i in range(times):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    time.sleep(wait)
