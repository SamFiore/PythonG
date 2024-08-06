import pyautogui as pg
import time

print ("Holis!! Gracias por activarme.")

time.sleep(3)

print("Estamos preparando todo, por favor espere...")

contador = 0
    
time.sleep(2)

print ("...")

time.sleep(1)

print ("Comencemos!!")

pg.hotkey("winleft")
pg.write("chrome")
pg.press("enter")
time.sleep(3)
pg.moveTo(934, 601, duration=0.5)
pg.click()
pg.click()
time.sleep(3)
pg.moveTo(389, 49 , duration=0.1)
pg.click()
pg.write("https://web.whatsapp.com/")
pg.press("enter")
time.sleep(16)
pg.moveTo(353, 292, duration=2)
pg.click()
pg.write("juan")
time.sleep(0.5)
pg.confirm("¿Quiere seguir?")
pg.moveTo(299, 419, duration=1)
pg.click()
time.sleep(2)
pg.confirm("¿Quieres seguir?")

while contador < 3:
    pg.moveTo(792, 960, duration=0.5)
    pg.write("Hola")
    pg.press("enter")
    time.sleep(10)
    contador += 1



