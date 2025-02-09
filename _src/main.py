#Modules
import sqlite3
import tkinter as tk
from PIL import Image, ImageTk
from db import database
from tkinter import messagebox
from modules.new_patient import new_patient_form
from modules.lab_technician import lab_technician_form

#Installing connection
connection, cursor = database.installing_database()
#Main Windows
root = tk.Tk()

def patient():
    from modules import patient
    panel_left.pack_forget()
    panel_right.pack_forget()

def doctor():
    from modules import doctor
    panel_left.pack_forget()
    panel_right.pack_forget()

def pharmacist():
    from modules import pharmacist
    panel_left.pack_forget()
    panel_right.pack_forget()

def lab_technician():
    lab_technician_form(root, panel_left, panel_right)

def admin():
    from modules import admin
    panel_left.pack_forget()
    panel_right.pack_forget()

def new_patient_handler():
    new_patient_form(root, panel_left, panel_right)
#Title Heading
root.title("St.Mary Hospital")
root.iconbitmap('../media/image/ico_icon/1.ico')

#Size of the windows
root.state('zoomed')

#Login panel
panel_left = tk.Frame(root, bg="#061e41", width=root.winfo_screenwidth() // 2)
panel_left.pack(side= 'left', fill='y')
panel_right = tk.Frame(root, bg="#ffffff", width=root.winfo_screenwidth() // 2)
panel_right.pack(side= 'right', fill='y')

#Login image
login_img = Image.open("../media/image/illustration/1.png")
resize_login_img = login_img.resize((672, 471))
photo_login_img = ImageTk.PhotoImage(resize_login_img)

label_login_img = tk.Label(panel_right, image=photo_login_img)
label_login_img.image = photo_login_img
label_login_img.pack(side='top', padx=20, pady=150)

#Login Elements
panel_width = root.winfo_screenwidth() // 2
panel_height = root.winfo_height()
#Login label
login_label = tk.Label(panel_left, text='LogIn', font=('Open Sans ExtraBold',100), fg="#ffffff", bg="#061e41")
login_label.place(x=0,y=-250, width=panel_width, height=panel_height)
#Login entry
name_placeholder = "    Enter Your Username"
password_placeholder = "    Enter Your Password"

login_name_entry = tk.Entry(panel_left, bg="#ffffff", fg="grey", relief='flat',font=('Open Sans ExtraBold', 25))
login_name_entry.insert(0, name_placeholder,)

def name_click(event):
    if login_name_entry.get() == name_placeholder:
        login_name_entry.delete(0, tk.END)
        login_name_entry.config(fg="#061e41")

def name_focusout(event):
    if login_name_entry.get() == "":
        login_name_entry.insert(0, name_placeholder)
        login_name_entry.config(fg="grey")

login_name_entry.bind("<FocusIn>", name_click)
login_name_entry.bind("<FocusOut>", name_focusout)
login_name_entry.place(x=panel_width//5.65, y=250, height=70 , width=panel_width// 2 + 100)


login_password_entry = tk.Entry(panel_left, bg="#ffffff", fg="grey", relief='flat', font=("Open Sans ExtraBold", 25))
login_password_entry.insert(0, password_placeholder)
def password_click(event):
    if login_password_entry.get() == password_placeholder:
        login_password_entry.delete(0, tk.END)
        login_password_entry.config(fg="#061e41")

def password_focusout(event):
    if login_password_entry.get() == "":
        login_password_entry.insert(0, password_placeholder)
        login_password_entry.config(fg="grey")

login_password_entry.bind("<FocusIn>", password_click)
login_password_entry.bind("<FocusOut>", password_focusout)
login_password_entry.place(x=panel_width//5.65, y=360, height=70 , width=panel_width//2 + 100)

def submit_login_data(name, password):
    conn = sqlite3.connect("../db/database_storage.db")
    cursor = conn.cursor()
    user_name_input = login_name_entry.get()
    user_password_input = login_password_entry.get()
    user_type_table=["doctor","pharmacist","lab_technician","existed_patient","admin"]
    for table in user_type_table:
        cursor.execute(f"SELECT * FROM {table} WHERE name = ? AND password = ?", (name, password))
        user = cursor.fetchone()
        if user:
            conn.close()
            return table, user
    conn.close()
    return None, None

def handel_login():
    name = login_name_entry.get()
    password = login_password_entry.get()

    if not name or name == name_placeholder or not password or password == password_placeholder:
        messagebox.showwarning("Input Error", "Please fill in both fields.")
        return


    user_type, user_info = submit_login_data(name, password)

    if user_type:
        #doctor check login
        cursor.execute("SELECT name FROM doctor WHERE name = ? AND password = ?", (name, password))
        doctor_check_login = cursor.fetchone()
        if doctor_check_login:
            doctor()
        #pharmacist check login
        cursor.execute("SELECT name FROM pharmacist WHERE name = ? AND password = ?", (name, password))
        pharmacist_check_login = cursor.fetchone()
        if pharmacist_check_login:
            pharmacist()
        #lab_technician check login
        cursor.execute("SELECT name FROM lab_technician WHERE name = ? AND password = ?", (name, password))
        lab_technician_check_login=cursor.fetchone()
        if lab_technician_check_login:
            lab_technician()
        #existed_patient check login
        cursor.execute("SELECT name FROM existed_patient WHERE name = ? AND password = ?", (name, password))
        existed_patient_check_login=cursor.fetchone()
        if existed_patient_check_login:
            patient()
        #admin check login
        cursor.execute("SELECT name FROM admin WHERE name = ? AND password = ?", (name, password))
        admin_check_login=cursor.fetchone()
        if admin_check_login:
            admin()
    else:
        messagebox.showerror("Login failed","Login Unsuccessful! ")
#Login buttons
login_submit_button = tk.Button(panel_left, text='Submit', relief='flat', font=('Open Sans ExtraBold',20), bd=0, bg="#ffffff", fg="#061e41", activebackground="#061e41", activeforeground="#ffffff", highlightthickness=0, padx=20, command=handel_login)
login_submit_button.place(x=panel_width//2.6, y= 470)
Login_anchor_button = tk.Button(panel_left, text='New Patient? Create an account here', font=("open sans ExtraBold", 20), bd=0, bg="#061e41", fg="#ffffff", activebackground="#061e41", activeforeground="#ffffff", highlightthickness=0, command=new_patient_handler)
Login_anchor_button.place(x=panel_width//8, y= 580)

#Tkinter Loop
root.mainloop()

#Close The Connection
connection.close()