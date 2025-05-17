import sqlite3

def installing_database():
    connection = sqlite3.connect("../db/database_storage.db")
    cursor = connection.cursor()

    #Doctor
    cursor.execute("""CREATE TABLE IF NOT EXISTS doctor (
    name TEXT PRIMARY KEY,
    password TEXT)""")

    #cursor.execute("INSERT INTO doctor (name, password) VALUES (?,?)", ("Dr.Abebe","12345"))
    #Appointments
    cursor.execute("""CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT,
    patient_name TEXT,
    time TEXT,
    date TEXT)""")

    #Pharmacist
    cursor.execute("""CREATE TABLE IF NOT EXISTS pharmacist (
    name TEXT PRIMARY KEY,
    password TEXT)""")
    #cursor.execute("INSERT INTO pharmacist (name, password) VALUES (?,?)", ("1","1"))

    #Lab Technician
    cursor.execute("""CREATE TABLE IF NOT EXISTS lab_technician (
    name TEXT PRIMARY KEY,
    password TEXT)""")
    #cursor.execute("INSERT INTO lab_technician (name,password) VALUES (?,?)", ("Kebede","12345"))

    #Existed Patient
    cursor.execute("""CREATE TABLE IF NOT EXISTS existed_patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    password TEXT,
    gender TEXT,
    phone_number TEXT,
    address TEXT,
    previous_illnesses TEXT,
    surgeries TEXT,
    medication TEXT,
    lab_test_result TEXT,
    waiting_lab_test TEXT,
    referral_hospital_name TEXT,
    verification TEXT,
    explanation TEXT,
    current_illness TEXT,
    patients_explanation TEXT)""")
    #cursor.execute("UPDATE existed_patient SET verification = ? WHERE patient_id = ?", ("TEST", 15))
    #Admin
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
    name TEXT PRIMARY KEY,
    password TEXT)""")
    #cursor.execute("INSERT INTO admin (name,password) VALUES (?,?)", ("2","2"))


    connection.commit()
    return connection, cursor

