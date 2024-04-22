from AddStu import AddStu
from ModifyStu import ModifyStu
from DelStu import DelStu
from PrintAll import PrintAll

class StudentClientHandler:
    def __init__(self, client, student_dict):
        self.client = client
        self.student_dict = student_dict
        
    def add_student(self):
        parameters = AddStu(self.client).execute()
        self.client.send_command('add', parameters)
        keep_going, response_data = self.client.wait_response()  
        return keep_going

    def del_student(self):
        student_info = DelStu().execute()
        
        if student_info is None:
            return True
        self.client.send_command('del', {'name': student_info})

        keep_going, response_data = self.client.wait_response()
        if response_data['status'] == 'OK':
            print(f'Student {student_info} has been deleted successfully.')
        else:
            print(f"Student {student_info} not found.")
        return keep_going
    
    def modify_student(self):
        keep_going = ModifyStu(self.student_dict, self.client).execute()
        return keep_going

    def show_students(self):
        self.client.send_command('show', {})
        keep_going, response = self.client.wait_response()
        PrintAll(response).execute()
        return keep_going

    def exit_program(self):
        return False

    def default_behavior(self):
        print("Unknown selection.")
        return True