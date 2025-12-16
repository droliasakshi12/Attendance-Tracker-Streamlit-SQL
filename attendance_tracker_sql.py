import pymysql


class attendance:
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="",database ="Student_db")
        self.cursor=self.db.cursor()

    def insert_students(self,name):       
        self.insert_query="INSERT INTO students(name) VALUES(%s)"

        try:
            self.cursor.execute(self.insert_query,(name))
            print("student recorded")
            self.db.commit()
      
        except Exception as e:
            print(e)
            self.db.rollback()


    def mark_attendance(self,name):
         self.check_student = "SELECT * FROM students WHERE name=%s"

         try:
             self.cursor.execute(self.check_student,(name))
             self.db.commit()
             student=self.cursor.fetchone()
             print(student)

             if not student:
                print("student does not exists")
            

             self.mark_attendance="INSERT INTO attendance(student_id , attendance_date) VALUES(%s,(CURDATE()))"
             self.cursor.execute(self.mark_attendance,(student[0]))

         except Exception as e :
             print(e)
             self.db.rollback()


    def view_student_attendance(self,name):
         self.stud="SELECT * FROM students WHERE name=%s"
         try:
            self.cursor.execute(self.stud,name)
            self.db.commit()
            student=self.cursor.fetchone()
            

            if not student:
                print("student does not exists")
            
            self.view_attendance="SELECT attendance_date FROM attendance WHERE student_id = %s"
            self.cursor.execute(self.view_attendance,(student[0]))
            attendance=self.cursor.fetchone()

            print(attendance,"\n")

            if not attendance:
                 print("student does not exists")
            
         except Exception as e :
              print(e)
              self.db.rollback()



    def fetchall(self):
         self.all="SELECT students.id, students.name,attendance.attendance_date FROM students JOIN attendance WHERE  students.id = attendance.student_id"

         try:
              self.cursor.execute(self.all)
              self.db.commit()
              record=self.cursor.fetchall()

              if not record:
                   print('not record found')
              
              for row in record:
                   print(row)
                   print("")
              
         except Exception as e :
              print(e)
              self.db.rollback()


while True:
    obj=attendance()
    a=int(input("1.INSERT NEW STUDENT\n2.MARK ATTENDANCE\n3.VIEW STUDENTS ATENDANCES\n4.DISPLAY ATTENDANCE OF ALL STUDENTS\n"))

    if (a==1):
            name=input("enter the name of student:")
            obj.insert_students(name)
    elif(a==2):
            name=input("enter the name of student:")
            obj.mark_attendance(name)
    elif(a==3):
        name=input("enter the name of student:")
        obj.view_student_attendance(name)
    elif(a==4):
        obj.fetchall()
    else:
        print("enter the valid number")