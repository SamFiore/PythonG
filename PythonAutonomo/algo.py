import pyautogui as pg
import time

print("Hola")

pg.confirm("¿Seguir?")

pg.hotkey("winleft")
time.sleep(2)
pg.write("cdm")
pg.press("enter")