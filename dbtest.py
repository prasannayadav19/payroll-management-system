

import sqlite3
conn = sqlite3.connect('pms.db')

cur = conn.cursor()

cur.execute(f"create table emp_details(empid int primary key,empname varchar(30),deptid int,designation varchar(30),email varchar(30),contactnum int,address varchar(30))")
cur.execute(f"create table sal_deatils(deptid int primary key,empid int,acc_num int,PAN varchar(30),base_sal int,FOREIGN KEY (empid) references emp_details(empid))")
cur.execute(f"create table attendance(empid int,deptid int,deptname varchar(30),empname varchar(30),date datetime,timeon datetime,timeout datetime,FOREIGN KEY (empid) references emp_details(empid),FOREIGN KEY (deptid) references sal_details(deptid))")
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
        print(data)
        conn.commit()
        conn.close()


'''from empdetails import Employee
emp = Employee()
emp.attendance(empid = 1,deptid = 11,deptname = 'cs',empname = 'mickey',date = '17-01-2023',timeon = '04:30',timeout = '08:30')'''


#from empdetails import Employee
#emp = Employee()
#emp.sal_details(deptid = 11,empid = 2,acc_num = 53002918765,PAN = 'DERERRFXSD',base_sal = 50000)




import sqlite3
conn = sqlite3.connect('pms.db')
cur = conn.cursor()
cur.execute(f"delete from emp_details")
cur.execute(f"delete from attendance")
cur.execute(f"delete from sal_deatils")
conn.commit()
conn.close()

from empdetails import salarycalculator
sc = salarycalculator()
sc.salarycalculation(eid = 1)