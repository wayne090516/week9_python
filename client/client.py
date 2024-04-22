import socket 
import json
from AddStu import AddStu
from ModifyStu import ModifyStu
from DelStu import DelStu
from PrintAll import PrintAll
from StudentClientHandler import StudentClientHandler

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))

    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters}
        print(f"The client sent data => {send_data}")
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
            data = self.client_socket.recv(BUFFER_SIZE)
            raw_data = data.decode()
            keep_going = True

            if raw_data == "closing":
                keep_going = False
            else:
                raw_data = json.loads(raw_data)
            print(f"The client received data => {raw_data}")
            return keep_going, raw_data

if __name__ == '__main__':
    client = SocketClient(host, port)
    student_dict = {}
    handler = StudentClientHandler(client, student_dict)
    actions = {
        'add': handler.add_student,
        'del': handler.del_student,
        'modify': handler.modify_student,
        'show': handler.show_students,
        'exit': handler.exit_program,
    }

    try:
        while True:
            user_choice = input("\nadd: Add a student's name and score\
                                \ndel: Delete a student\
                                \nmodify: Modify a student's score\
                                \nshow: Print all\
                                \nexit: Exit\
                                \nPlease select: ")
            
            keep_going = actions.get(user_choice, handler.default_behavior)()
            if not keep_going:
                break
    except Exception as e:
        print(f"An error occurred: {e}")