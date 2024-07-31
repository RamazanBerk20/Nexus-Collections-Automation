import pyautogui
import subprocess
from time import sleep

class App():
    def __init__(self, browser: str, download_button: str = "download_button.png", download_start: str = "download_start.png") -> None:
        self.download_button = download_button
        self.download_start = download_start
        self.browser = browser
        pyautogui.FAILSAFE = False

    def locate_download_button(self) -> tuple:
        return pyautogui.locateCenterOnScreen(self.download_button, confidence=0.85, grayscale=True)
    
    def locate_download_start(self) -> tuple:
        return pyautogui.locateCenterOnScreen(self.download_start, confidence=0.85, grayscale=True)

    def click_download_button(self) -> None:
        pyautogui.click(self.locate_download_button())
        print("Download button clicked")

    def close_browser(self) -> None:
        subprocess.run(f'taskkill /f /im {self.browser}', shell=True)

    def is_browser_running(self) -> bool:
        try:
            return self.browser in subprocess.check_output(f'tasklist /FI "IMAGENAME eq {self.browser}"', shell=True, text=True)
        except subprocess.CalledProcessError:
            return False
    
    def wait_for_browser(self) -> None:
        while True:
            try:
                self.locate_download_start()
                sleep(.5)
                print("Download started")

                self.close_browser()
                print(f"{self.browser} closed")
                sleep(1)

                return

            except pyautogui.ImageNotFoundException:
                print("Download not started...")

                if not self.is_browser_running():
                    print(f"{self.browser} is not running")
                    return
    
    def run(self) -> None:
        try:
            self.click_download_button()

            self.wait_for_browser()

        except pyautogui.ImageNotFoundException:
            print("Download button not found...")