class Modify:
    def __init__(self, client):
        self.client = client

    def execute(self):
        name = input("Please input a student's name: ")
        self.client.send_command("query", {'name': name})
        response = eval(self.client.wait_response())
        print(f"  The client received data => {response}")
        
        if response["status"] != "OK":
            print(f"Add [{name}, {subject}, {new_score}] failed")
            return 0

        subject = input("Please input a subject you want to change: ")
        new_score = input(f"Add a new subject for {name}. Please input {subject} score or '< 0' to discard the subject: ")
        try:
            new_score = float(new_score)
        except ValueError:
            print("Invalid score. Please input a valid number.")
            return 0

        scores_dict = {subject: new_score}
        self.client.send_command("modify", {'name': name, 'scores_dict': scores_dict})
        response = eval(self.client.wait_response())
        print(f"  The client received data => {response}")

        if response["status"] == "OK":
            print(f"Add [{name}, {subject}, {new_score}] success")
        else:
            print(f"Add [{name}, {subject}, {new_score}] failed")
        return 0