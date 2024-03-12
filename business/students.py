from commons.utils import * 
from commons.menus import *
def new_student(file_path):
    id_number = input("Type the id number: ")
    name = input("Type your name: ")
    emergency_contact = input("Type the emergency contact: ")
    cellphone = input("Type the cellphone: ")
    state = "enrolled"

    student = {
        "id_number":id_number,
        "name":name,
        "emergency_contact" : emergency_contact,
        "numbers" :[cellphone],
        "route":"",
        "trainer_id":"",
        "state" : state    
              }
    students = load_json(file_path)
    for data in students:
        if(data["id_number"] == id_number):
            input("This person is already in the list\n Press enter to continue:")
            return
    students.append(student)
    save_json(students,file_path)

def show_students(file_path):
    clean_screen()
    students = load_json(file_path)
    print_card(students)    
    stop()
    
def students_modifications(file_path):
    id = input("Type the id number: ")
    students = load_json(file_path)
    student = search_for_keys(students,"id_number",id)
    if student == []:
        op = yes_or_no_menu("The id is not in the data base\nWant to try another id?")
        if(op == 1):
            clean_screen()
            students_modifications(file_path)
    else:
        student = student[0]
        if(student["state"] == "reprobate"):
            op = yes_or_no_menu("Are you sure you want to modificate a reprobate student?")
            if(op ==2):
                return
        key = key_menu(student)
        new_value = input(f"The last value was '{student[key]}',type the new value: ")
        for data in students:
            if data["id_number"] == id:
                if(isinstance(data[key],str)):
                    data[key] = new_value
                else:
                    new_value = new_value.replace("[","").replace("]","")
                    data[key] = new_value.split(",")
                save_json(students,file_path)
                return

