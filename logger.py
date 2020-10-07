from datetime import datetime

class Logger:

    file = None

    def __init__(self, fileName):
        self.file = open(fileName, "a")

    def log(self, logLevel, message):
        now = str(datetime.now())
        self.file.write("[" + now + "] " + logLevel + ": " + message + " \n")
        print("\n [" + now + "] " + logLevel + ": " + message + " \n")

    def closeFile(self):
        self.file.close()