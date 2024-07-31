from app import App
from sys import argv

app = App(browser=argv[1])

while True:
    app.run()