import time
import pyautogui
import keyboard

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen("random pics\The.png", confidence=0.7):
        camp_google = pyautogui.locateOnScreen("random pics\The.png", confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://youtube.com")
        pyautogui.press("enter")
        cautare_youtube()
    else:
        print("Imaginea nu este pe ecran")

def cautare_youtube():
    time.sleep(5)
    if pyautogui.locateOnScreen("random pics\YT.png", confidence=0.8):
        camp_yt = pyautogui.locateOnScreen("random pics\YT.png", confidence=0.8)
        pyautogui.click(camp_yt)
        time.sleep(1)
        pyautogui.write("Tom Scott")
        pyautogui.press("enter")
        abonare()
    else:
        print("Nu s-a putut cauta")

def abonare():
    time.sleep(5)
    if pyautogui.locateOnScreen("random pics\Tom 2.png", confidence=0.8):
        canal = pyautogui.locateOnScreen("random pics\Tom 2.png", confidence=0.8)
        pyautogui.click(canal)
        time.sleep(5)
        subscribe = pyautogui.locateOnScreen("random pics\sub.png", confidence = 0.8)
        pyautogui.click(subscribe)
    else:
        print("Tom Scott nu a fost gasit")


#cautare_google()
#while not keyboard.is_pressed("esc"):
#    if keyboard.is_pressed("alt"):
#        print(pyautogui.position())
#        time.sleep(0.1)

# Browser folosit: Mozilla Firefox