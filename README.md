# Auto Marker Suite
Scripts to unzip students files, validate their html and check their outlines.


### Requirements
* python3
* familiarity with command line

### To Get Environment running:
* `pip install requirements.txt` in the command line
* save a class list (csv file) in the same directory of this repository
* save required zips from moodle in the same directory of this repository
* Unzip the big file with all the students (but not the actual students files themselves - that's what the script is for)
* change the all caps variables in the python file

# Scripts:
1. Unzip all students files
    - This is a tool for teachers to better use the files from moodle
    - To run the unzipper: `python ./unzipper.py`

2. HTML validator Auto marker IF STUDENTS HAVE UPLOADED TO dmitstudent
    - This is a tool for teachers who would like to run multiple assignments through the [w3 schools validator](https://validator.w3.org/nu/)
    - To run auto marker: `python ./html-validator.py`

3. Html validator Auto marker that goes through files
    - This will go through the unzipped files (make sure to run `unzipper.py` first) and output their validator rules
    - To run auto marker: `python ./html-validator-files.py`
