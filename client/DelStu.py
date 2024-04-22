class DelStu():
    def __init__(self):
        pass

    def execute(self):
        name = input("Enter the student's name to delete: ")
        confirm = input("Confirm to delete (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled deletion.")
            return None
        return name 