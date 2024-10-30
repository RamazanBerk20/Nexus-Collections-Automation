import psutil
import pyautogui
from time import sleep
from sys import argv

download_button = "./Images/download_button.png"
download_start = "./Images/download_start.png"

BROWSERSAFE = 3
VORTEXSAFE = 5

def locate(image):
    return pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=.85)

def click(pos):
    pyautogui.click(pos)

def closeProcess(process):
    try:
        for proc in psutil.process_iter():
            if proc.name() == process:
                proc.kill()

        return
    except psutil.NoSuchProcess:
        if isBrowserRunning(process):
            closeProcess(process)
        
        return

def isBrowserRunning(browser):
    try:
        for proc in psutil.process_iter():
            if proc.name() == browser:
                return True
        return False
    except psutil.NoSuchProcess:
        return False

def waitBrowser(browser):
    while True:
        try:
            locate(download_start)
            break
        except pyautogui.ImageNotFoundException:
            pass

    sleep(BROWSERSAFE)
    print("download started!")

    closeProcess(browser)
    print(f"{browser} closed")
    sleep(VORTEXSAFE)
    return

def run(browser):
    while True:
        try:
            pos = locate(download_button)
            click(pos)
            print("download button clicked!")
            break

        except pyautogui.ImageNotFoundException:
            print("download button not found!")

    if not isBrowserRunning(browser):
        sleep(1)
        return

    waitBrowser(browser)

while True:
    run(argv[1])