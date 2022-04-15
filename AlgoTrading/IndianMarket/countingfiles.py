import os
def nfiles():
    APP_FOLDER = '/home/keshav/Desktop/Results'
    totalDir = 0
    totalFiles = 0

    for files in os.walk(APP_FOLDER):
        for Files in files:
            totalFiles += 1
    print(totalFiles)
    s = 'result' + str(totalFiles)
    return s

# for base, dirs, files in os.walk(APP_FOLDER):
#     print('Searching in : ',base)
#     # for directories in dirs:
#     #     totalDir += 1
#     for Files in files:
#         totalFiles += 1
