import mysql.connector
from datetime import date

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="medical_service"        
    )

mydb = connect_to_db()
cursor = mydb.cursor()

def insert_patients(name, birthday, gender, address, phone_number, email):
    sql = "INSERT INTO patients (full_name, date_of_birth, gender, `address`, phone_number, email) VALUES  (%s, %s, %s, %s, %s, %s)"
    values = (name, birthday, gender, address, phone_number, email)
    cursor.execute(sql, values)
    
    mydb.commit()
    print("inserted a patient")
def insert_doctors(name, specialization, phone_number, email, years_of_experience):
    sql = "INSERT INTO doctors (full_name, specialization, phone_number, `email`, years_of_experience) VALUES  (%s, %s, %s, %s, %s)"
    values = (name, specialization, phone_number, email, years_of_experience)
    cursor.execute(sql, values)
    
    mydb.commit()
    print("inserted a doctor")
def insert_appointments(patient_id, doctor_id, appointment_date, reason, status):
    sql = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason, `status`) VALUES  (%s, %s, %s, %s, %s)"
    values = (patient_id, doctor_id, appointment_date, reason, status)
    cursor.execute(sql, values)
    
    mydb.commit()
    print("inserted a appointment")
def get_all_patients():
    sql = "SELECT patients.full_name, patients.date_of_birth, patients.gender, patients.address , doctors.full_name, appointments.reason, appointments.status FROM patients INNER JOIN appointments ON patients.patient_id = appointments.patient_id INNER JOIN doctors ON doctors.doctor_id = appointments.doctor_id"
    cursor.execute(sql)
    students = cursor.fetchall()
    for s in students:
        print(s)
def get_all_appointment_today(date_time):
    sql = "SELECT patients.full_name, patients.date_of_birth, patients.gender, patients.address , doctors.full_name, appointments.status FROM patients INNER JOIN appointments ON patients.patient_id = appointments.patient_id INNER JOIN doctors ON doctors.doctor_id = appointments.doctor_id WHERE appointments.appointment_date = ?"
    cursor.execute(sql, (date_time, ))   
    appointment_date_today = cursor.fetchall()
    for a in appointment_date_today:
        print(a)
def main():
    print("-------Menu--------")
    print("1. Insert a patient")
    print("2. Insert a doctor")
    print("3. Create a appointment")
    print("4. Get all patients")
    print("5. Get all appointments today")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter patient's name: ")
        birthday = input("Enter patient's birthday (YYYY-MM-DD): ")
        gender = input("Enter patient's gender: ")
        address = input("Enter patient's address: ")
        phone_number = input("Enter patient's phone number: ")
        email = input("Enter patient's email: ")
        insert_patients(name, birthday, gender, address, phone_number, email)
    elif choice == 2:
        name = input("Enter doctor's name: ")
        specialization = input("Enter doctor's specialization: ")
        phone_number = input("Enter doctor's phone number: ")
        email = input("Enter doctor's email: ")
        experience = input("Enter doctor's year of experience: ")
        insert_doctors(name, specialization, phone_number, email, experience)
    elif choice == 3:
        patient_id = int(input("Enter patient's id: "))
        doctor_id = int(input("Enter doctor's id: "))
        appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
        reason = input("Enter reason: ")
        status = input("Enter status: ")
        insert_appointments(patient_id, doctor_id, appointment_date, reason, status)
    elif choice == 4:
        get_all_patients()
    elif choice == 5:
        date = str(date.today())
        get_all_appointment_today(date)
        
if __name__ == "__main__":
    main()