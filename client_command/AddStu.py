class AddStu:
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def execute(self):       
        name = input("Please input a student's name: ")
        student_data = {'name': name, 'scores': {}}
        self.socket_client.send_command("query", {'name': name})
        response = self.socket_client.wait_response() 
        if response['status'] == 'Fail':
            while True:                   
                subject = input("Please input a subject name or exit for ending: ")
                if subject == 'exit':
                    break
                try:
                    score = float(input(f"Please input {name}'s {subject} score or < 0 for discarding the subject: "))
                    if score >= 0:
                        student_data['scores'][subject] = score
                except ValueError:
                    print("Invalid score input. Please try again.")
        else:
            print("The name is already exist.")
            return 0
        self.socket_client.send_command('add', student_data)
        response = self.socket_client.wait_response()

        if response and response['status'] == 'OK':
            print(f"Add name {name}, scores {student_data['scores']} success.")
        else:
            print(f"name {name} , scores {student_data['scores']} fail.")

        return response
