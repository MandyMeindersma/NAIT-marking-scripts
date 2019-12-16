import zipfile
import os

NAME_OF_STUDENT_ZIP = 'COMP1017.1191.A10.REG-Assignment-7-6805497'
NAME_OF_ASSIGN = "assign-4"

rootDir = 'C:/users/meind/dev/marking-scripts/'+ NAME_OF_STUDENT_ZIP
number_of_students_marked = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    if NAME_OF_ASSIGN in dirName and "\\css" not in dirName and "\\img" not in dirName and "\\js" not in dirName and "_MACOSX" not in dirName:
        number_of_students_marked +=1
        print(str(number_of_students_marked) + " " + dirName.split("\\")[-2].split("_")[0])
        for fname in fileList:
            if fname == "index.html":
                file = open(dirName + "\\" + fname, "r")
                #print(file.read())
                print('\t%s' % fname)
