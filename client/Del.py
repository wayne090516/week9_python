class DelStu:
    def __init__(self, client):
        self.client = client

    def execute(self):
        name = input("Please input a student's name: ")
        self.client.send_command("query", {'name': name})
        response = eval(self.client.wait_response())
        print(f"  The client received data => {response}")
        
        if response["status"] != "OK":
            print("Student does not exist.")
            return 0

        confirm = input("Confirm to delete (y/n): ")
        if confirm.lower() == 'y':
            self.client.send_command("del", {'name': name})
            response = eval(self.client.wait_response())
            print(f"  The client received data => {response}")

            if response["status"] == "OK":
                print("Delete success")
            else:
                print("Delete failed")
        else:
            print("Delete cancelled")
        return 0
