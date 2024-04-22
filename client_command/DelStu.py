import json

class DelStu:
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def execute(self):
        name = input("Please input a student's name: ")
        parameters = {'name': name}

        self.client_socket.send_command('query', parameters)
        response = self.client_socket.wait_response()

        if response['status'] == 'OK':

            confirm_delete = input("Confirm to delete (y/n): ")

            if confirm_delete.lower() == 'y':
                
                self.client_socket.send_command('del', parameters)
                self.client_socket.wait_response()
                response = self.client_socket.wait_response()

                if response['status'] == 'OK':
                    print("Delete success.")
                else:
                    print("Failed to delete student.")
            else:
                print("Deletion canceled.")
        else:
            print(f"Student {name} not found.")
