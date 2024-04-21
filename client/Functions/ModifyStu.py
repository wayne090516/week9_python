class ModifyStu:

    def __init__(self, client):
        self.client = client

    def execute(self):
        name = input("  Please input a student's name or exit: ")
        if name=="exit":
            return False
        
        self.client.send_command("query", {'name': name})
        response = eval(self.client.wait_response())

        if response["status"] == 'Fail':
            print(f"    The name {name} is not found")
            return False
        elif response["status"] == 'OK':
            print(f"  current subjects are {', '.join(subject for subject in response['scores'])}\n")
            subject = input("  Please input a subject you want to change: ")
            new_score = input(f"  Please input {subject}'s new score of {name} or enter sth else to discard the subject: ")
            try:
                new_score = float(new_score)
                score = {subject: new_score}
                self.client.send_command("modify", {'name': name, 'scores': score})
                response = eval(self.client.wait_response())

                if response["status"] == "OK":
                    print(f"    Modify [{name}, {subject}, {new_score}] success")
                else:
                    print(f"    Modify [{name}, {subject}, {new_score}] failed")

            except ValueError:
                return False
