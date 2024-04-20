import socket 
import json
from AddStu import AddStu
from ModifyStu import Modify
from PrintAll import PrintAll
from Del import DelStu

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

action_list = {
    "add": AddStu, 
    "show": PrintAll,
    "modify" : Modify,
    "del" : DelStu
}

class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters }
        print(send_data)
        self.client_socket.send(json.dumps(send_data).encode())


    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print(raw_data)

        if raw_data == "closing":
            return raw_data
        
        return raw_data

def print_menu():
    print("add: Add a student's name and score")
    print("modify: Modify a student's scores")
    print("del: Delete a student's information")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")
    return selection

if __name__ == '__main__':
    client = SocketClient(host, port)

    select_result = "initial"
    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
        except Exception as e:
            print(e)
    
    
