class AddStu:
    def __init__(self, client):
        self.client = client

    def execute(self):
        student_name = input("\nPlease input a student's name or exit: ")

        if student_name.lower() == 'exit':
            return {}

        # 先查詢學生是否已經存在
        self.client.send_command('query', {'name': student_name})
        keep_going, response = self.client.wait_response()

        if response.get('status') == 'OK':
            # 學生已經存在
            print(f"Student {student_name} already exists.")
            return {}

        scores = {}
        while True:
            subject = input("Please input a subject name or exit for ending: ")
            if subject.lower() == 'exit':
                break

            score_input = input(f"Please input {student_name}'s {subject} score or < 0 for discarding the subject: ")
            try:
                score = float(score_input)
                if score < 0:
                    print(f"Discarded {student_name}'s {subject} score.")
                else:
                    scores[subject] = score
                    print(f"Add {student_name}'s {subject} score: {score}")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
                continue

        if scores:
            print(f"Add {student_name}'s scores successfully.")
            return {'name': student_name, 'scores': scores}
        else:
            print(f"No scores added for {student_name}.")
            return {}