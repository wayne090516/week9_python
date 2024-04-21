from Commands.AddStu import AddStu
from Commands.DelStu import DelStu
from Commands.ModifyStu import ModifyStu
from Commands.PrintAll import PrintAll
from Commands.QueryStu import QueryStu
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer

DBConnection.db_file_path = "student_data.db"
DBInitializer().execute()
para = {'name': 'test', 'scores': {'English': 99.0, 'Chinese': 88.0}}
AddStu(para).execute()
# print(PrintAll().execute())
# print(DelStu({'name': 'test'}).execute())
