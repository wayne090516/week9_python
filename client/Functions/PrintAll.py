class PrintAll:

    def __init__(self, client):
        self.client = client

    def execute(self):
        self.client.send_command('show',{})
        received_data = eval(self.client.wait_response()) 
        student_dict = (received_data)["parameters"]

        print("\n==== student list ====\n")
        for key, value in student_dict.items():
            print(f"Name: {key}")
            for subject, score in value['scores'].items():
                print(f"  subject: {subject}, score: {float(score)}")
            print()
        print("\n======================")
