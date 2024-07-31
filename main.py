from app import App
from sys import argv

app = App(browser=argv[1])

print(f"App Started for {app.browser}...")

while True:
    app.run()