import json

class ModifyStu:
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def execute(self):
        name = input("Please input a student's name: ")       
        self.client_socket.send_command('query', {'name': name})
        response = self.client_socket.wait_response()

        if response['status'] == 'OK':
            current_subjects = list(response['scores'].keys())
            print(f"Current subjects are {current_subjects}")     

        else:
            print(f"{name} does not exist.")
            return 
        subject = input("Please input the subject you want to change: ")
        new_score = input(f"Please input {subject}'s new score of {name}: ")

        parameters = {'name': name, 'scores_dict': {subject: float(new_score)}}
        self.client_socket.send_command('modify', parameters)
        response = self.client_socket.wait_response()

        if response['status'] == 'OK':
            print(f"Modify [{name}, {subject}, {new_score}] success.")
        else:
            print("Failed to modify. Reason:", response.get('reason', 'Unknown'))
