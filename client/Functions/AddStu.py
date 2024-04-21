class AddStu:

    def __init__(self, client):
        self.client = client

    def execute(self):      
        name = input("  Please input a student's name or exit: ")
        if name=="exit":
            return False
        
        self.client.send_command("query", {'name': name})
        response = eval(self.client.wait_response())

        if response["status"] == 'OK':
            print(f"  {name} already exists")
            return False
        
        scores_dict=dict()
        subject = input("  Please input a subject name or exit for ending: ")  
        while subject != "exit":
            score = ""
            while score == "":   
                score = input(f"  Please input {name}'s {subject} score or < 0 for discarding the subject: ")
                try:
                    score = float(score)
                    if score >= 0:
                        scores_dict[subject] = score
                except ValueError as e:  
                    print(f'    Wrong format with reason: {e}, try again')
                    score = ""

            subject = input("  Please input a subject name or exit for ending: ")

        parameters = {'name': name, 'scores': scores_dict}
        self.client.send_command('add', parameters)

        if eval(self.client.wait_response())["status"] == 'OK':
            print(f"    Add {parameters} success")
        else:
            print(f"    Add {parameters} failed")
