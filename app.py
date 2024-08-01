import pyautogui
import subprocess
from time import sleep

class App:
    def __init__(self, browser: str, download_button: str = "download_button.png", download_start: str = "download_start.png") -> None:
        self.download_button = download_button
        self.download_start = download_start
        self.browser = browser
        pyautogui.FAILSAFE = False

    def Locate(slf, image: str) -> tuple:
        return pyautogui.locateCenterOnScreen(image, confidence=0.85, grayscale=True)

    def Locate_Download_Button(self) -> tuple:
        return self.Locate(self.download_button)
    
    def Locate_Download_Start(self) -> tuple:
        return self.Locate(self.download_start)

    def Click_Download_Button(self) -> None:
        pyautogui.click(self.Locate_Download_Button())
        print("Download button clicked")

    def Close_Browser(self) -> None:
        subprocess.run(f'taskkill /f /im {self.browser}', shell=True)

    def Is_Browser_Running(self) -> bool:
        try:
            return self.browser in subprocess.check_output(f'tasklist /FI "IMAGENAME eq {self.browser}"', shell=True, text=True)
        except subprocess.CalledProcessError:
            return False
    
    def Wait_For_Browser(self) -> None:
        while True:
            try:
                self.Locate_Download_Start()
                sleep(1)
                print("Download started")

                self.Close_Browser()
                print(f"{self.browser} closed")
                sleep(.5)

                return

            except pyautogui.ImageNotFoundException:
                print("Download not started...")

                if not self.Is_Browser_Running():
                    print(f"{self.browser} is not running")
                    return
    
    def Run(self) -> None:
        try:
            self.Click_Download_Button()

            self.Wait_For_Browser()

        except pyautogui.ImageNotFoundException:
            print("Download button not found...")