import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_project_streamlit")

cursor=db.cursor()
attendence_table="CREATE TABLE attendance(id INT  AUTO_INCREMENT PRIMARY KEY , student_id INT REFERENCES students(id),attendance_date DATE)"

try:
    cursor.execute(attendence_table)
    print("table created successfully")
    db.commit()

except Exception as e :

    print(e)
    db.rollback()