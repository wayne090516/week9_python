class ModifyStu:
    def __init__(self, student_dict, client):
        self.student_dict = student_dict
        self.client = client

    def execute(self):
        self.client.send_command('show', {})
        keep_going, response = self.client.wait_response()

        if 'status' in response and response['status'] == 'OK':
            self.student_dict.update(response.get('parameters', {}))

            for student_name, student_data in self.student_dict.items():
                if student_data['scores'] is None or len(student_data['scores']) == 0:
                    print(f"There are no subjects registered for {student_name}.")
                    student_data['scores'] = {}

                score_dict = {score_info['subject']: score_info['score'] for score_info in student_data['scores']}
                student_data['scores'] = score_dict

        student_name = input("\nPlease input a student's name or exit: ")

        if student_name.lower() == 'exit':
            return True

        if student_name in self.student_dict:
            if self.student_dict[student_name]['scores'] is None:
                print(f"There are no subjects registered for {student_name}.")
                self.student_dict[student_name]['scores'] = {}

            current_subjects = ', '.join(self.student_dict[student_name]['scores'].keys())
            print(f"Current subjects for {student_name} are: {current_subjects}")

            subject_to_modify = input("Please input the subject you want to change or add: ")

            score_input = input(f"Please input {student_name}'s score for {subject_to_modify} or 'exit' to cancel: ")
            if score_input.lower() == "exit":
                return True

            try:
                score = float(score_input)
                if score < 0:
                    print(f"Subject {subject_to_modify} discarded for {student_name}")
                else:
                    parameters = {'name': student_name, 'subject': subject_to_modify, 'score': score}
                    self.client.send_command('modify', parameters)
                    keep_going, response_data = self.client.wait_response()

                    if response_data.get('status') == 'OK':
                        self.student_dict[student_name]['scores'][subject_to_modify] = score
                        print(
                            f"  {('Modified' if subject_to_modify in self.student_dict[student_name]['scores'] else 'Added')} {student_name}'s score for {subject_to_modify} successfully.")
                        return keep_going
                    else:
                        print(
                            f"Failed to modify {student_name}'s score for {subject_to_modify}: {response_data.get('message', 'Unknown error')}")
                        return keep_going
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
                return True
        else:
            print(f"Student {student_name} not found.")
            return True