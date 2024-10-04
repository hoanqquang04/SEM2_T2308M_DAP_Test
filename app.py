# Clear code previous
import os
os.system("cls")
from tabulate import tabulate

import mysql.connector
import datetime

def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "medical_service"
)

def add_patients():
    try:
        full_name = input("Enter fullname patient: ")
        while True:
            try:
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
            except ValueError:
                print("Incorrect date format, should be YYYY-MM-DD")
            else:
                break

        gender = input("Enter gender patient: ")
        address = input("Enter address patient: ")
        while True:
            try:
                phone_number = int(input("Enter phone number patient: "))
            except ValueError:
                print("Please enter your integer of phone number!!!")
            else:
                break
        email = input("Enter email patient: ")
        
        connection = connect_to_db()
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO `patients`(`full_name`, `date_of_birth`, `gender`, `address`, `phone_number`, `email`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (full_name, date_of_birth, gender, address, phone_number, email))
        
        connection.commit()
        print(f"\nAdd patient {full_name} successfully !")
        
        connection.close()
        
    except Exception as error:
        print(error)

def add_doctors():
    try:
        full_name = input("Enter fullname doctor: ")
        specialization = input("Enter specialization: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        years_of_experience = int(input("Enter years of experience: "))

        connection = connect_to_db()
        cursor = connection.cursor()

        insert_query = "INSERT INTO `doctors`(`full_name`, `specialization`, `phone_number`, `email`, `years_of_experience`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (full_name, specialization, phone_number, email, years_of_experience))

        connection.commit()
        print(f"\nAdd doctor {full_name} successfully !")

        connection.close()

    except Exception as error:
        print(error)

def add_appointments():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        for i in range(3):
            patient_id = int(input(f"Enter patient ID for appointment {i+1}: "))
            doctor_id = int(input(f"Enter doctor ID for appointment {i+1}: "))
            appointment_date = input(f"Enter appointment date (YYYY-MM-DD HH:MM:SS) for appointment {i+1}: ")
            reason = input(f"Enter reason for appointment {i+1}: ")

            insert_query = "INSERT INTO `appointments`(`patient_id`, `doctor_id`, `appointment_date`, `reason`) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (patient_id, doctor_id, appointment_date, reason))

        connection.commit()
        print("Appointments added successfully !")

        connection.close()

    except Exception as error:
        print(error)

def get_patient_report():
    connection = connect_to_db()
    cursor = connection.cursor()

    select_query = """
    SELECT p.patient_id, p.full_name, p.date_of_birth, p.gender, p.address, d.full_name as doctor_name, a.reason, a.appointment_date
    FROM patients p
    JOIN appointments a ON p.patient_id = a.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    """
    cursor.execute(select_query)
    patient_report = cursor.fetchall()
    headers = ["No", "Patient name", "Birthday ", "Gender", "Address", "Doctor name", "Reason", "Date"]
    print(tabulate(patient_report, headers=headers))

    connection.close()

if __name__ == "__main__":
    get_patient_report()