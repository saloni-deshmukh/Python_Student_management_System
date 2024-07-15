import sqlite3

class deletedata :
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def deletestudent(self, sid):
        self.cur.execute(f'''
                            DELETE FROM STUDENT
                            WHERE std = {sid}
                        ''')
        self.conn.commit()
        print("--- Data deleted successfully ---")