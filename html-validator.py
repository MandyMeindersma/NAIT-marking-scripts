import requests
from bs4 import BeautifulSoup
import csv

PATH_TO_STUDENT_CSV = "students.csv"
COLUMN_STUDENT_EMAILS_IN = 2 # zero indexing
BOOLEAN_OF_COLUMN_HEADERS = False #if you have column headers (which you most likely will) I will skip the first row
STRING_OF_ASSIGNMENT = "vertical-menu" #the hash of the url with no slashes
SHOW_ERROR_REASONS = True #if you want to see a short description of the error in the terminal.


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

            error_count, warning_count, other_count = 0,0,0
            for item in children:
                message_type = str(item.p.text).split(":")[0]
                if "Error" in message_type:
                    error_count += 1
                elif "Warning" in message_type:
                    warning_count += 1
                else:
                    other_count += 1

            print(f'\t{student_username} {" "*(14 - len(student_username))}had {error_count} errors and {warning_count} warnings in this assignment.')
            if other_count > 0:
                print(f'\t\tThere were also {other_count} other messages that you should look into manually')

            if SHOW_ERROR_REASONS:
                for item in children:
                    paragraph = item.p.text
                    print(f'\t\t\t{paragraph[:100] + "..." if len(paragraph) > 100 else paragraph}')
            line_count += 1

    print(f'Marked {line_count - 1 if BOOLEAN_OF_COLUMN_HEADERS else line_count} students.')
