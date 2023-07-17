

import sqlite3
conn = sqlite3.connect('pms.db')

cur = conn.cursor()

cur.execute(f"create table emp_details(empid int primary key,empname varchar(30),deptid int,designation varchar(30),email varchar(30),contactnum int,address varchar(30))")
cur.execute(f"create table sal_deatils(deptid int primary key,empid int,acc_num int,PAN varchar(30),base_sal int,FOREIGN KEY (empid) references emp_details(empid))")
cur.execute(f"create table attendance(empid int,deptid int,deptname varchar(30),empname varchar(30),date datetime,timeon datetime,timeout datetime,FOREIGN KEY (empid) references emp_details(empid),FOREIGN KEY (deptid) references sal_details(deptid))")
conn.commit()
conn.close()