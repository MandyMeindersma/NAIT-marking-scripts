import zipfile
import os

NAME_OF_STUDENT_ZIP = 'COMP1017.1191.A10.REG-Assignment-3-6805491'

rootDir = 'C:/users/meind/dev/marking-scripts/'+ NAME_OF_STUDENT_ZIP
for dirName, subdirList, fileList in os.walk(rootDir):
    if dirName[-5:] == "file_":
        print(dirName.split("\\")[-1].split("_")[0])
        for fname in fileList:
            print('\t%s' % fname)
            with zipfile.ZipFile(dirName+"/" +fname, 'r') as zip_ref:
                zip_ref.extractall(dirName)
