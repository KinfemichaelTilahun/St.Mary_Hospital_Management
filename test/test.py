import sqlite3
from tkinter import messagebox

try:
    # Connect to the database
    conn = sqlite3.connect("../db/database_storage.db")  # Adjust the path as needed
    cursor = conn.cursor()

    # Execute a query to select all data from the existed_patient table
    cursor.execute("SELECT * FROM pharmacist")

    # Fetch all the rows from the result of the query
    rows = cursor.fetchall()

    # Check if any rows were returned
    if rows:
        # Print all rows
        for row in rows:
            print(row)
    else:
        messagebox.showinfo("No Data", "No data found in the existed_patient table.")

    # Close the database connection
    conn.close()

except sqlite3.Error as e:
    messagebox.showerror("Database Error", f"An error occurred: {e}")
