from commons.utils import *
from commons.menus import *
from business.students import *
from business.trainers import *
from business.classrooms import *
from business.report import *
from business.test import *
from business.routes import *
from business.tuitions import *
import os
import json
# Generate students
students = create_students()
json_students = json.dumps(students, indent=4)# Convert the list of students to JSON format
script_directory = os.path.dirname(os.path.abspath(__file__))# Determine the script directory

# Generate file paths for various JSON files
file_paths = {
    "students": file_path_generator(script_directory, "data", "students.json"),
    "trainers": file_path_generator(script_directory, "data", "trainers.json"),
    "tuitions": file_path_generator(script_directory, "data", "tuitions.json"),
    "classrooms": file_path_generator(script_directory, "data", "classrooms.json"),
    "notes": file_path_generator(script_directory, "data", "notes.json"),
    "routes": file_path_generator(script_directory, "data", "routes.json")
}

file_path_students = file_paths["students"]# Initial path Json students

file_path_trainers = file_paths["trainers"]# Initial path Json trainers

file_path_tuitions = file_paths["tuitions"]# Initial path Json tuitions

file_path_classrooms = file_paths["classrooms"]# Initial path Json classrooms

file_path_notes = file_paths["notes"]# Initial path Json notes

file_path_routes = file_paths["routes"]# Initial path Json routes

# Generate trainers
trainers = create_trainers()

#6 a.m. a 9 p.m 10 a.m. a 1 p.m. 2 p.m. a 5 p.m. 6 p.m a 10 p.m
classrooms = [
  {
    "name": "apolo",
    "schedule": "morning 6 a.m. a 9 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NodeJs"
  },
  {
    "name": "apolo",
    "schedule": "morning 10 a.m. a 1 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NodeJs"
  },
  {
    "name": "apolo",
    "schedule": "afternoon 2 p.m. a 5 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NodeJs"
  },
  {
    "name": "apolo",
    "schedule": "afternoon 6 p.m a 10 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NodeJs"
  },
  {
    "name": "artemis",
    "schedule": "morning 6 a.m. a 9 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "Java"
  },
  {
    "name": "artemis",
    "schedule": "morning 10 a.m. a 1 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "Java"
  },
  {
    "name": "artemis",
    "schedule": "afternoon 2 p.m. a 5 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "Java"
  },
  {
    "name": "artemis",
    "schedule": "afternoon 6 p.m. a 10 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "Java"
  },
  {
    "name": "sputnik",
    "schedule": "morning 6 a.m. a 9 p.m. ",
    "trainer_id": "",
    "students_id": [],
    "route": "NetCore"
  },
  {
    "name": "sputnik",
    "schedule": "morning 10 a.m. a 1 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NetCore"
  },
  {
    "name": "sputnik",
    "schedule": "afternoon 2 p.m. a 5 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NetCore"
  },
  {
    "name": "sputnik",
    "schedule": "afternoon 6 p.m. a 10 p.m.",
    "trainer_id": "",
    "students_id": [],
    "route": "NetCore"
  }
]
routes = [
  {
    "name": "NodeJS",
    "fundaments_of_programming": [
      "Introduction to algoritms",
      "PSeint",
      "Python"
    ],
    "web_programming": [
      "HTML",
      "CSS",
      "Bootsrap"
    ],
    "formal_programming": [
      "JavaScript",
    ],
    "databases": [
      "MongoDb",
      "Postgresql"
    ],
    "backend": [
      "NodeJS",
      "Express"
    ]
  },
  {
    "name": "NetCore",
    "fundaments_of_programming": [
      "Introduction to algoritms",
      "PSeint",
      "Python"
    ],
    "web_programming": [
      "HTML",
      "CSS"
    ],
    "formal_programming": [
      "C#"
    ],
    "databases": [
      "Mysql",
      "MongoDb"
    ],
    "backend": [
      "NetCore"
    ]
  },
  {
    "name": "Java",
    "fundaments_of_programming": [
      "Introduction to algoritms",
      "PSeint",
      "Python"
    ],
    "web_programming": [
      "HTML",
      "CSS"
    ],
    "formal_programming": [
      "Java"
    ],
    "databases": [
      "MongoDbl",
      "Postgresql"
    ],
    "backend": [
      "Spring Boot"
    ]
  }
]

while (True):
    op = main_menu()
    if op == 1:
        try:
            while(True):
                op = students_menu()
                if(op == 1):
                    new_student(file_path_students)
                elif(op == 2):
                    show_students(file_path_students)
                elif(op == 3):
                    students_modifications(file_path_students)
                elif(op == 4):
                    break
        except Exception as e:
            print(f"estudiante menu has the next error {e}")
    elif op == 2:
        try:
            while(True):
                op = trainers_menu()
                if(op == 1):
                    new_trainer(file_path_trainers)
                elif(op == 2):
                    search_trainer(file_path_trainers)
                elif(op == 3):
                    trainers_modifications(file_path_trainers)
                elif(op == 4):
                    break
        except Exception as e:
            print(f"trainer menu has the next error: {e}")
    elif op == 3:
        try:
            while(True):
                op = routes_menu()
                if(op == 1):
                    new_route(file_path_routes)
                elif(op == 2):
                    show_routes(file_path_routes)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"routes menu has the next error: {e}")
    elif op == 4:
        try:
            while(True):
                op = tuition_menu()
                if(op == 1):
                    new_tuition(file_path_students,file_path_classrooms,file_path_trainers,file_path_routes,file_path_tuitions)
                elif(op == 2):
                    show_tuition(file_path_tuitions)
                elif(op == 3):
                    tuition_modification(file_path_routes,file_path_students,file_path_trainers,file_path_classrooms,file_path_tuitions)
                elif(op == 4):
                    break
        except Exception as e:
            print(f"tuition menu has the next error: {e}")
    elif op == 5:
        try:
            while(True):
                op = classroom_menu()
                if(op == 1):
                    new_classroom(file_path_classrooms)
                elif(op == 2):
                    search_classroom(file_path_classrooms)
                elif(op == 3):
                    Classroom_modification(file_path_students,file_path_trainers,file_path_classrooms)
                elif(op == 4):
                    break
        except Exception as e:
            print(f"classroom menu has the next error: {e}")
    elif op == 6:
        try:
            while(True):
                op = report_menu()
                if(op == 1):
                    show_enrolled(file_path_students)
                elif(op == 2):
                    show_approved(file_path_students)
                elif(op == 3):
                    show_risk(file_path_students,file_path_notes)
                elif(op == 4):
                    show_trainers(file_path_trainers)
                elif(op == 5):
                    break
        except Exception as e:
            print(f"report menu has the next error: {e}")
    elif op == 7:
        try: 
            while(True):
                op = test_menu()
                if(op == 1):
                    entrance_test(file_path_students)
                elif(op == 2):
                    filter_test(file_path_students,file_path_notes)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"test menu has the next error: {e}")
    elif op == 8:
        print("thank you for using this program（‐＾▽＾‐）!")
        break

