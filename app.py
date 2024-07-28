import pyautogui
import subprocess
from time import sleep

class App():
    def __init__(self):
        self.download_button = "download_button.png"
        self.download_start = "download_start.png"
        pyautogui.FAILSAFE = False


    def clickDownloadButton(self) -> None:
        download_button_location = pyautogui.locateCenterOnScreen(self.download_button, confidence=0.85)
        pyautogui.click(download_button_location)

        print("Download button clicked")

    
    def isProcessRunning(self, process_name: str) -> bool:
        try:
            return "msedge.exe" in subprocess.check_output('tasklist /FI "IMAGENAME eq msedge.exe"', shell=True, text=True)
        except subprocess.CalledProcessError:
            return False
        

    def waitUntilEdgeIsClosed(self) -> None:
        PROCNAME = "msedge.exe"

        while True:
            try:
                pyautogui.locateCenterOnScreen(self.download_start, confidence=0.85)
                print("Download started...")
                
                subprocess.run("taskkill /f /im msedge.exe", shell=True)
                subprocess.run("taskkill /f /im msedgewebview2.exe", shell=True)
                sleep(1)
                break

            except pyautogui.ImageNotFoundException:
                print("Download hasn't started yet...")

                if not self.isProcessRunning(PROCNAME):
                    print("Edge is not running...")
                    return
                
        
    def run(self) -> None:
        try:
            self.clickDownloadButton()
            sleep(.5)
            self.waitUntilEdgeIsClosed()

        except pyautogui.ImageNotFoundException:
            print("Button not found...")