import requests
from bs4 import BeautifulSoup
import csv

PATH_TO_STUDENT_CSV = "students.csv"
COLUMN_STUDENT_EMAILS_IN = 2 # zero indexing
BOOLEAN_OF_COLUMN_HEADERS = False #if you have column headers (which you most likely will) I will skip the first row
STRING_OF_ASSIGNMENT = "vertical-menu" #the hash of the url with no slashes



with open(PATH_TO_STUDENT_CSV) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0 and BOOLEAN_OF_COLUMN_HEADERS:
            line_count += 1
        else:

            student_username = row[COLUMN_STUDENT_EMAILS_IN].split("@")[0]
            response = requests.get("https://validator.w3.org/nu/?doc=http%3A%2F%2F"+ student_username +".dmitstudent.ca%2F" + STRING_OF_ASSIGNMENT)
            soup = BeautifulSoup(response.text, "html.parser")

            orderedLists = soup.ol
            if orderedLists != None:
                children = orderedLists.findChildren("li" , recursive=False)
            else:
                children = []

            print(f'\t{student_username} {" "*(14 - len(student_username))}had {len(children)} errors in this assignment.')
            line_count += 1
    print(f'Marked {line_count - 1 if BOOLEAN_OF_COLUMN_HEADERS else line_count} students.')
