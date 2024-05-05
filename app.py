import pyautogui
import wmi
from time import sleep

class App():
    def __init__(self):
        self.download_button = "download_button.png"
        pyautogui.FAILSAFE = False

    def clickDownloadButton(self):
        download_button_location = pyautogui.locateCenterOnScreen(self.download_button, confidence=0.85)
        pyautogui.click(download_button_location)

        print("Download button clicked")

    def waitUntilFirefoxIsClosed(self):
        c = wmi.WMI()
        while 1:
            firefox = c.Win32_Process(name="firefox.exe")
            if not firefox:
                pyautogui.moveTo(10, 10)
                sleep(1)
                break
        
    def run(self):
        try:
            self.clickDownloadButton()
            sleep(.5)
            self.waitUntilFirefoxIsClosed()

        except pyautogui.ImageNotFoundException:
            print("Button not found")
            sleep(.5)