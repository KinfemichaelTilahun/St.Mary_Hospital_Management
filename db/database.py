import sqlite3

def installing_database():
    connection = sqlite3.connect("../db/database_storage.db")
    cursor = connection.cursor()

    #Doctor
    cursor.execute("""CREATE TABLE IF NOT EXISTS doctor (
    name TEXT PRIMARY KEY,
    password TEXT)""")

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

    #Lab Technician
    cursor.execute("""CREATE TABLE IF NOT EXISTS lab_technician (
    name TEXT PRIMARY KEY,
    password TEXT)""")

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
    verification TEXT,
    explanation TEXT,
    current_illness TEXT)""")

    #Admin
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
    name TEXT PRIMARY KEY,
    password TEXT)""")

    connection.commit()
    return connection, cursor