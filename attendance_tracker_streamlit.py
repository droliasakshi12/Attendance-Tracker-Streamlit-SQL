import streamlit as st
import pymysql

class attendance:

    def __init__(self):
        self.db=pymysql.connect(host='localhost',user='root',password='',database='Student_db')
        self.cursor=self.db.cursor()


    def insert_stud(self,name):
        self.name=name
        if self.name=="":
            st.error("Please enter the name")
            return

        self.insert_query="INSERT INTO students(name)VALUES(%s)"

        try:
           self.cursor.execute(self.insert_query,(self.name))
           self.db.commit()
           st.success("student details recorded")

           
        except Exception as e:
            if e.args[0]==1062:
                st.error(f"Duplicate entry")
            else:
                st.error(f"{e}")
                
            self.db.rollback()


    def mark_attendance(self,name):
        self.name=name
        self.stud="SELECT * FROM students WHERE name=%s"

        try:
            self.cursor.execute(self.stud,(self.name))
            self.db.commit()
            student=self.cursor.fetchone()
            if self.name=="":
                st.error=("enter student name")
            else:
                if not student:
                    st.error("student not found")
                    
                else:
                    st.success("student found")

                    self.mark="INSERT INTO attendance(student_id,attendance_date) VALUES(%s,CURDATE())"
                    self.cursor.execute(self.mark,(student[0]))
                    self.db.commit()

                    if self.mark=="":
                        st.error("error in marking attendance")
                        
                    else:
                        st.success("And attendance marked")
                        
        except Exception as e:
            print(e)
            self.db.rollback()



    def view_student_attendance(self,name):
        self.name=name
        self.stud="SELECT * FROM students WHERE name=%s"
        
        try:
            
            self.cursor.execute(self.stud,(self.name))
            self.db.commit()
            student=self.cursor.fetchone()

            self.view_attend="SELECT * FROM attendance WHERE student_id=%s"
            self.cursor.execute(self.view_attend,(student[0]))
            attendance=self.cursor.fetchall()

            if self.name=='':
                st.error="please enter student name"
            
            else:
                if not attendance:
                    st.error("student attendance not found ")

                else:                    
                    st.success("attendance found")
                    for j in attendance:
                        st.write(j)
                        st.write("\n")
        
        except Exception as e:
            print(e)
            self.db.rollback()


    def view_all(self):
        self.view_allstud="SELECT students.id , students.name , attendance.attendance_date  FROM attendance join students on attendance.student_id = students.id"
        
        
        try:
            self.cursor.execute(self.view_allstud)
            self.db.commit()
            records=self.cursor.fetchall()

            if not records:
                st.error("no attendance found")
            else:
                for i in records:
                    st.write(i)
                    st.write("\n")
                    
        except Exception as e :
            print(e)
            self.db.rollback()

        
        
a=st.number_input(label="Enter your choice: ",placeholder="1.Enter a new student.\n2. Mark Students attendance\n3.To view student attendance\n4.view all student attendance")

if not a:
    st.error("No Option selected")
else:
        obj=attendance()
        if(a==1):
            name=st.text_input(label='enter students name:')
            obj.insert_stud(name)
        elif(a==2):
            name=st.text_input(label="enter student name:")
            obj.mark_attendance(name)
        elif(a==3):
            name=st.text_input(label="enter student name:")
            obj.view_student_attendance(name)
        elif(a==4):
            obj.view_all()
        else:
            st.write("please enter the valid number")


