import pymysql 

db=pymysql.connect(host="localhost",user="root",password="",database="sakshi_project_streamlit")
cursor=db.cursor()

stud_table="CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(25) NOT NULL , UNIQUE KEY name_unique(name)) "


try:
    cursor.execute(stud_table)    
    print("table created successfully")
    db.commit()

except Exception as e :
    print(e)
    db.rollback()


