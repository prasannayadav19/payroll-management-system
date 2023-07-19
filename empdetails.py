import sqlite3

conn = sqlite3.connect("pms.db")

cur = conn.cursor()

class Employee:

    def empinsert(self,**k):
        conn = sqlite3.connect("pms.db")
        cur = conn.cursor()
        cur.execute(f'''insert into emp_details values(
                   {k['empid']},"{k['empname']}",{k['deptid']},"{k['designation']}",
                   "{k['email']}",{k['contactnum']},"{k['address']}")''')
        conn.commit()
        print("Data has been inserted successfully")
    def show_employees(self):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute('select * from emp_details')
        data = []
        for i in cur.fetchall():
            context = {}
            context['eid'] = i[0]
            context['ename'] = i[1]
            context['deptid'] = i[2]
            context['designation'] = i[3]
            context['email'] = i[4]
            context['contactnum'] = i[5]
            context['address'] = i[6]
            data.append(context)
        return(data)
    def attendance(self,**k):
        conn = sqlite3.connect("pms.db")
        cur = conn.cursor()
        cur.execute(f'''insert into attendance values(
                   {k['empid']},{k['deptid']},"{k['deptname']}","{k['empname']}",
                   "{k['date']}","{k['timeon']}","{k['timeout']}")''')
        conn.commit()
    def sal_details(self,**k):
        conn = sqlite3.connect("pms.db")
        cur = conn.cursor()
        cur.execute(f'''insert into sal_deatils values(
                   {k['deptid']},{k['empid']},
                   {k['acc_num']},"{k['PAN']}",{k['base_sal']})''')
        print("data has been inserted successfully.")
        conn.commit()
