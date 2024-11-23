import os

class FileChecks:
    def __init__(self, file):
        self.file = file
        EXISTS = self.fileExistence(file)
        CONTENTS = self.fileContents(file)
        MATCH = self.expectedContents(file)

    def fileExistence(self, file):
        if os.path.exists(file):
            return True
        else:
            return False

    def fileContents(self, file):
        if os.path.getsize(file) > 0:
            return True
        else:
            return False

    def expectedContents(self, file):
        with open(file, 'r') as r:
            WEB_PATH = f""
            r.read()