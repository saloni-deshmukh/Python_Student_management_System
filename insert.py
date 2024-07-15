

import sqlite3

class insertdata :

    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def insertstudent(self, sid, sname, email, city):
        self.cur.execute(f'''
                            INSERT INTO STUDENT VALUES (
                                {sid},
                                "{sname}",
                                "{email}",
                                "{city}"
                            )
                        ''')
        self.conn.commit()
        print("---Data added successfully---")

    def insertcourse(self, course, coursename, sid, price):
        self.cur.execute(f'''
                            INSERT INTO COURSE VALUES (
                            {course},
                            "{coursename}",
                            {sid},
                            {price}
                             )
                        ''')
        self.conn.commit()
        print("---Data added successfully---")

    def inserttransaction(self, tid, sid, course, method) :
        self.cur.execute(f'''
                             INSERT INTO TRANS VALUES (
                             {tid},
                             {sid},
                             {course},
                             "{method}"
                             )
                        ''')
        self.conn.commit()
        print("---Data added successfully---")
        

