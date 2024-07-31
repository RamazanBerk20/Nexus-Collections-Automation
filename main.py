from app import App
from sys import argv

app = App(browser=argv[1])

print(f"\n\nApp Started for {app.browser}...\n\n")

while True:
    app.Run()