class DelStu:

    def __init__(self, client):
        self.client = client

    def execute(self):
        name = input("  Please input a student's name or exit: ")
        if name=="exit":
            return False
        
        self.client.send_command("query", {'name': name})
        response = eval(self.client.wait_response())

        if response["status"] == 'Fail':
            print(f"  {name} does not exists")
            return False
        
        elif response["status"] == 'OK':
            confirm = input("  Confirm to delete (y/n): ")
            if confirm.lower() == 'y':
                self.client.send_command('del', {'name': name})
                response = eval(self.client.wait_response())
                if response["status"] == 'OK':
                    print(f"    Delete {name} success")
                else:
                    print(f"    Delete {name} failed")
            else:
                pass
