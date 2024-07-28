import pyautogui
import os
from time import sleep

class App():
    def __init__(self):
        self.download_button = "download_button.png"
        self.download_start = "download_start.png"
        pyautogui.FAILSAFE = False

    def clickDownloadButton(self):
        download_button_location = pyautogui.locateCenterOnScreen(self.download_button, confidence=0.85)
        pyautogui.click(download_button_location)

        print("Download button clicked")

    def waitUntilEdgeIsClosed(self):
        PROCNAME = "msedge.exe"
        while True:
            try:
                pyautogui.locateCenterOnScreen(self.download_start, confidence=0.85)
                sleep(.5)

                os.system(f"taskkill /f /im {PROCNAME}")
                sleep(1)
                
                break

            except pyautogui.ImageNotFoundException:
                print("Download hasn't started yet...")
        
    def run(self):
        try:
            self.clickDownloadButton()
            self.waitUntilEdgeIsClosed()

        except pyautogui.ImageNotFoundException:
            print("Button not found")
            sleep(.5)