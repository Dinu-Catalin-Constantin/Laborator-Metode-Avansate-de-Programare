import pyautogui
import time
import keyboard
import webbrowser
pozitie_initial_x=550
pozitie_initiala_y=415
pos_fin_x=2320
pos_fin_y=835
dif_x=990-pozitie_initial_x
dif_y=pos_fin_y-pozitie_initiala_y
curent_x=pozitie_initial_x
curent_x=550
curent_y=415
def autoview(curent_x,pos_fin_x,pozitie_initial_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y):
    time.sleep(1)
    while not keyboard.is_pressed('esc'):
        time.sleep(1)
        if curent_x<=pos_fin_x :
            pyautogui.click(curent_x,curent_y)
            print(1,curent_x,curent_y)
            curent_x=curent_x+dif_x
            time.sleep(4.5)
            if pyautogui.locateOnScreen(r'random pics\back.png' , confidence=0.7)!= None:
                #camp_google=pyautogui.locateOnScreen(r'C:\Users\beni\Desktop\python\back.png' , confidence=0.7)
                pyautogui.click(pyautogui.locateOnScreen(r'random pics\back.png' , confidence=0.7))
        else:
            curent_x=pozitie_initial_x
            time.sleep(1)
            pyautogui.move(curent_x,curent_y)
            pyautogui.scroll(-800)
            time.sleep(4)   
webbrowser.open("https://www.youtube.com/")
time.sleep(5)           
autoview(curent_x,pos_fin_x,pozitie_initial_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y)

# Codul a fost modificat pentru un monitor 2560 x 1440