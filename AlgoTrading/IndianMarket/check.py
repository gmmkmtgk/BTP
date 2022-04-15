import os

APP_FOLDER = '/home/keshav/Desktop/Results'
totalDir = 0
totalFiles = 0

for files in os.walk(APP_FOLDER):
    for Files in files:
        totalFiles += 1
print(totalFiles)
s = 'result' + str(totalFiles)
print(s)
