import pyautogui
import subprocess
from time import sleep

class App():
    def __init__(self):
        self.download_button = "download_button.png"
        self.download_start = "download_start.png"
        pyautogui.FAILSAFE = False

    def locate_download_button(self) -> tuple:
        return pyautogui.locateCenterOnScreen(self.download_button)

    def click_download_button(self) -> None:
        pyautogui.click(self.locate_download_button())
        print("Download button clicked")

    def closeEdge(self) -> None:
        subprocess.run('taskkill /f /im msedge.exe', shell=True)

    def isEdgeRunning(self) -> bool:
        try:
            return "msedge.exe" in subprocess.check_output('tasklist /FI "IMAGENAME eq msedge.exe"', shell=True, text=True)
        except subprocess.CalledProcessError:
            return False
    
    def waitForEdge(self):
        try:
            pyautogui.locateCenterOnScreen(self.download_start)
            sleep(.5)
            print("Download started")

            self.closeEdge()

        except pyautogui.ImageNotFoundException:
            print("Download not started...")

            if not self.isEdgeRunning():
                print("Edge is not running")
                return
        
    def run(self):
        try:
            self.click_download_button()

            self.waitForEdge()

        except pyautogui.ImageNotFoundException:
            print("Download button not found...")