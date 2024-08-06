from re import A
from tkinter import Y
from turtle import position
import pyautogui,sys

print("apretar 'ctrl + c' para finalizar.")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end="")
        print("\b" * len(positionStr), end=" ", flush=True)

except KeyboardInterrupt:
    print("/n")
