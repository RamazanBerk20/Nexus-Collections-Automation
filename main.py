from app import App
from sys import argv

app = App(browser=argv[0])

while True:
    app.run()