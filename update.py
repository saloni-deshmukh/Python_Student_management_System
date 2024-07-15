
import sqlite3

class updatedata :
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def updatestudent(self, n, sid, sname, email, city):
        self.cur.execute(f'''
                            UPDATE STUDENT SET
                                std = "{sid}",
                                sname = "{sname}",
                                email = "{email}",
                                city = "{city}"
                                WHERE std = {n}
                        ''')
        self.conn.commit()
        print("--- Data updated successfully ---")

    def updatecourse(self,n, course, coursename, price):
        self.cur.execute(f'''
                            UPDATE COURSE SET
                            course = "{course}",
                            coursename = "{coursename}",
                            price = "{price}"
                            WHERE sid = {n}
                        ''')
        self.conn.commit()
        print("---Data updated successfully---")

    def updatetrans(self,n,tid,course,method):
        self.cur.execute(f'''
                            UPDATE TRANS SET
                            tid = "{tid}",
                            course = "{course}",
                            method = "{method}"
                            WHERE sid = {n}
                            
                         ''')
        self.conn.commit()
        print("----DATA UPDATED SUCCESSFULLY----")
        

