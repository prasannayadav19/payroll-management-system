from empdetails import Employee,salarycalculator

from flask import Flask,render_template,jsonify,request
 
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/employee_signup',methods = ['GET','POST'])
def emp_sigup():
    if request.method=='POST':
      eid = request.form.get('eid')
      ename = request.form.get('ename')
      dptid = request.form.get('dptid')
      designation = request.form.get('designation')
      emailid = request.form.get('emailid')
      contact_no = request.form.get('contact_no')
      address = request.form.get('address')
      print(eid,ename,dptid)
      emp = Employee()
      emp.empinsert(empid=eid,empname=ename,deptid=dptid,designation=designation,email=emailid,contactnum=contact_no,address=address)

      return jsonify({'Message':"Successfully Fetched the data"})
    else:
      return render_template('signup.html')
    
@app.route('/employees',methods = ['GET','POST'])
def show_employees():
  emp = Employee()
  data = emp.show_employees()
  return render_template('show_employee.html',employees = data)

@app.route('/attendance',methods = ['GET','POST'])
def attendance():
   if request.method == 'POST':
      eid = request.form.get('eid')
      dptid = request.form.get('dptid')
      dptname = request.form.get('dptname')
      ename = request.form.get('ename')
      date = request.form.get('date')
      timein = request.form.get('timein')
      timeout = request.form.get('timeout')
      emp = Employee()
      emp.attendance(empid = eid,deptid = dptid,deptname = dptname,empname = ename,date = date,timeon = timein,timeout = timeout)
      return jsonify({'Attendance':"Successfully inserted"})
   return render_template('attendance.html')

@app.route('/salary_details',methods = ['GET','POST'])
def salary_details():
   if request.method == 'POST':
      dptid = request.form.get('dptid')
      eid = request.form.get('eid')
      account_number = request.form.get('account_number')
      pan = request.form.get('pan')
      base_salary = request.form.get('base_salary')
      emp = Employee()
      emp.sal_details(deptid = dptid,empid = eid,acc_num = account_number,PAN = pan,base_sal = base_salary)
      return jsonify({'Salarydetails':"Successfully inserted"})
   return render_template('salarydetails.html')

@app.route('/payroll_release',methods = ['GET','POST'])
def payrollrelease():
    if request.method=='POST':
        eid = request.form.get("empid")
        sc = salarycalculator()
        total_salary = sc.salarycalculation(eid = int(eid))
        context = {'EmployeeID':eid,'TotalSalary':int(total_salary)}
        return render_template('showsalary.html',data = context)
    else:
        return render_template('empid.html')


if __name__ == '__main__':
  app.run(host ='0.0.0.0',port=5050)


#creating object for class:
#emp = Employee()
#calling the function:
#emp.empinsert(empid=1,empname='xyz',deptid=11,designation='manager',email='xyz@gmail.com',contactnum=123547891,address='vsp')
