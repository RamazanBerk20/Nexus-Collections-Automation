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
    
    def isProcessRunning(self, process_name: str) -> bool:
        try:
            os.system(f"tasklist /FI \"IMAGENAME eq {process_name}\" | findstr {process_name}")
            return True
        except:
            return False

    def waitUntilEdgeIsClosed(self) -> None:
        PROCNAME = "msedge.exe"

        # Check if Edge is started after clicking button, if not, wait a second to be opened, if still not opened, return nothing
        sleep(1)
        if not self.isProcessRunning(PROCNAME):
            return

        # Wait until download started, then close the app
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
            sleep(.25)