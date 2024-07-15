
import sqlite3

class readdata :
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def readstudent(self, sid):
        self.cur.execute(f'''
                            SELECT * FROM STUDENT
                            WHERE std = {sid}
                        ''')
        student = self.cur.fetchone()  # Use fetchall() if you expect multiple rows
        self.conn.commit()
        if student:
            print(f'Name : {student[1]}\nEmail : {student[2]}\nCity : {student[3]}\n')
            print("--- Data retrieved successfully ---")
        else:
            print("--- No student found with the provided SID ---")
            print("--- Data read successfully ---")


