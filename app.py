import pyautogui
import subprocess
from time import sleep

class App():
    def __init__(self):
        self.download_button = "download_button.png"
        self.download_start = "download_start.png"
        pyautogui.FAILSAFE = False

    def locate_download_button(self) -> tuple:
        return pyautogui.locateCenterOnScreen(self.download_button, confidence=0.85, grayscale=True)
    
    def locate_download_start(self) -> tuple:
        return pyautogui.locateCenterOnScreen(self.download_start, confidence=0.85, grayscale=True)

    def click_download_button(self) -> None:
        pyautogui.click(self.locate_download_button())
        print("Download button clicked")

    def close_edge(self) -> None:
        subprocess.run('taskkill /f /im msedge.exe', shell=True)

    def is_edge_running(self) -> bool:
        try:
            return "msedge.exe" in subprocess.check_output('tasklist /FI "IMAGENAME eq msedge.exe"', shell=True, text=True)
        except subprocess.CalledProcessError:
            return False
    
    def wait_for_edge(self) -> None:
        while True:
            try:
                self.locate_download_start()
                sleep(.5)
                print("Download started")

                self.close_edge()
                print("Edge closed")
                sleep(1)

                return

            except pyautogui.ImageNotFoundException:
                print("Download not started...")

                if not self.is_edge_running():
                    print("Edge is not running")
                    return
    
    def run(self) -> None:
        try:
            self.click_download_button()

            self.wait_for_edge()

        except pyautogui.ImageNotFoundException:
            print("Download button not found...")