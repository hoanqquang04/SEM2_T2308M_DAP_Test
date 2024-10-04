import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="medical_service"
    )  

def add_patient():
    name = input("Enter name: ")
    date = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    connection = connect_to_db()
    cursor = connection.cursor()

    query = "INSERT INTO patients (full_name, date_of_birth, gender, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, date, gender, address, phone, email))

    connection.commit()
    print("Add success")

def add_doctor():
    name = input("Enter name: ")
    specialization = input("Enter specialization: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    year = input("Enter year of experience: ")

    connection = connect_to_db()
    cursor = connection.cursor()

    query = "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, specialization, phone, email, year))

    connection.commit()
    print("Add success")

def add_appointment():
    patient_id = input("Enter patient_id: ")
    doctor_id = input("Enter doctor_id: ")
    appointment_date = input("Enter appointment date: ")
    reason = input("Enter reason: ")
    status = input("Enter status: ")

    connection = connect_to_db()
    cursor = connection.cursor()

    query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (patient_id, doctor_id, appointment_date, reason, status))

    connection.commit()
    print("Add success")

def show_appointments_report():

    connection = connect_to_db()
    cursor = connection.cursor()

    query = "SELECT appointments.appointment_id, patients.full_name, patients.date_of_birth, patients.gender, patients.address, doctors.full_name, appointments.reason FROM ((appointments INNER JOIN patients ON appointments.patient_id = patients.patient_id) INNER JOIN doctors ON appointments.doctor_id = doctors.doctor_id);"
    cursor.execute(query)

    result = cursor.fetchall()

    for i in result:
        print(i)

def show_appointments_details():

    connection = connect_to_db()
    cursor = connection.cursor()

    query = "SELECT appointments.appointment_id, patients.full_name, patients.date_of_birth, patients.gender, doctors.full_name, appointments.status FROM ((appointments INNER JOIN patients ON appointments.patient_id = patients.patient_id) INNER JOIN doctors ON appointments.doctor_id = doctors.doctor_id);"
    cursor.execute(query)

    result = cursor.fetchall()

    for i in result:
        print(i)

def menu():   
        while(True):
                print("1. Add patient")
                print("2. Add doctor")
                print("3. Add appointment")
                print("4. Show appointments reports")
                print("5. Show appointments details")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    add_patient()
                if choice == 2:
                    add_doctor()
                if choice == 3:
                    add_appointment()
                if choice == 4:
                    show_appointments_report()
                if choice == 5:
                    show_appointments_details()



if __name__ == "__main__":
    menu()