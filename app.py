import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user= "root",
        password = "",
        database = "medical_service"

    )
def add_patients():
    full_name = input("enter name :")
    date_of_birth = int(input("enter date_of_birth :"))
    gender = input("enter gender :")
    address = input("enter address :")
    phone_number = input("enter phone_number :")
    email = input("enter email :")


    connection =  connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO patients (full_name, date_of_birth, gender, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (full_name, date_of_birth, gender, address, phone_number, email))
    connection.commit()
    print(f"add bệnh nhân {full_name} thành công ")
def add_doctors():
    full_name = input("enter name :")
    specialization = int(input("enter specialization :"))
    phone_number = input("enter phone_number :")
    email = input("enter email :")
    years_of_experience = input("enter years_of_experience :")
    

    connection =  connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (full_name, specialization, phone_number, email, years_of_experience))
    connection.commit()
    print(f"add bac si : {full_name} thành công ")
def add_appointments():
    patient_id = input("enter patient_id :")
    doctor_id = int(input("enter doctor_id :"))
    appointment_date = input("enter appointment_date :")
    reason = input("enter reason :")
    connection =  connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (patient_id, doctor_id, appointment_date, reason))
    connection.commit()
    print(f"add cuoc hen thành công ")
def generate_report():
    connection =  connect_to_db()
    cursor = connection.cursor()    
    query = """
    select p.full_name, p.date_of_birth, p.gender, p.address, d.full_name, a.reason, a.appointment_date
    from appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("báo cáo chi tiết :")
    print("No\tPatient Name\tBirthday\tGender\tAddress\tDoctor Name\tReason\tDate")
    for i, row in enumerate(results, 1):
        print(f"{i}\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")
def get_today_appointments():
    connection =  connect_to_db()
    cursor = connection.cursor() 
    query = """
    select p.full_name, p.date_of_birth, p.gender, d.full_name, a.status
    from appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    where DATE(a.appointment_date) = CURDATE()
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("cuộc hẹn hôm nay :")
    print("Patient Name\tBirthday\tGender\tDoctor Name\tStatus")
    for i in results:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")

def menu():
    while True:
        print("1. add_patients")
        print("2. add_doctors")
        print("3. add_appointments")
        print("4. generate_report")
        print("5. get_today_appointments")
        print("6. exit")
        
        choice = input("enter choice: ")

        if choice == "1":
            add_patients()
        elif choice == "2":
            add_doctors()
        elif choice == "3":
            add_appointments()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            get_today_appointments()
        elif choice == "6":
            print("Exiting .")
            break
        else:
            print("eror.")
if __name__ == "__main__":
    
    
    menu()