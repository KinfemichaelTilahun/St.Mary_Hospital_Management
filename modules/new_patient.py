import tkinter as tk
from PIL import Image, ImageTk
from db import database
from tkinter import messagebox

connection, cursor = database.installing_database()

def new_patient_form(root, panel_left, panel_right):
    #Forgtting the main frames
    panel_left.pack_forget()
    panel_right.pack_forget()

    #Adding Frames in new_patient.py
    panel_left_np=tk.Frame(root, bg="#061e41", width=root.winfo_screenwidth() // 2)
    panel_left_np.pack(side= 'left', fill='y')
    panel_left_np_block_1=tk.Frame(panel_left_np, bg="#ffffff", width=root.winfo_screenwidth() // 2, height="50")
    panel_left_np_block_1.pack()
    panel_left_np_block_2=tk.Frame(panel_left_np, bg="#ffffff", width=root.winfo_screenwidth() // 2, height="50")
    panel_left_np_block_2.pack(side='bottom')
    panel_right_np=tk.Frame(root, bg="#ffffff", width=root.winfo_screenwidth() // 2)
    panel_right_np.pack(side='right', fill='y')

    #elements of panel_left_np
    panel_left_np_label=tk.Label(panel_left_np, text='Register', font=('Open Sans ExtraBold', 65), fg="#ffffff", bg="#061e41")
    panel_left_np_label.pack()

    panel_left_np_name_placeholder = "                                  Name"
    panel_left_np_password_placeholder = "                              Password"
    panel_left_np_gender_placeholder = "                                Gender"
    panel_left_np_phone_placeholder = "                                 Phone"
    panel_left_np_address_placeholder = "                               Address"

    panel_left_np_entry_name = tk.Entry(panel_left_np, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 20))
    panel_left_np_entry_name.insert(0, panel_left_np_name_placeholder)
    def panel_left_np_name_click(event):
        if panel_left_np_entry_name.get() == panel_left_np_name_placeholder:
            panel_left_np_entry_name.delete(0, tk.END)
            panel_left_np_entry_name.config(fg="#061e41")
    def panel_left_np_name_focusout(event):
        if panel_left_np_entry_name.get() == "":
            panel_left_np_entry_name.insert(0, panel_left_np_name_placeholder)
            panel_left_np_entry_name.config(fg="grey")
    panel_left_np_entry_name.bind("<FocusIn>", panel_left_np_name_click)
    panel_left_np_entry_name.bind("<FocusOut>", panel_left_np_name_focusout)
    panel_left_np_entry_name.place(x=root.winfo_screenwidth() // 20, y=200, width=root.winfo_screenwidth() // 2.5, height=50)

    panel_left_np_entry_password = tk.Entry(panel_left_np, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 20))
    panel_left_np_entry_password.insert(0, panel_left_np_password_placeholder)
    def panel_left_np_password_click(event):
        if panel_left_np_entry_password.get() == panel_left_np_password_placeholder:
            panel_left_np_entry_password.delete(0, tk.END)
            panel_left_np_entry_password.config(fg="#061e41")
    def panel_left_np_password_focusout(event):
        if panel_left_np_entry_password.get() == "":
            panel_left_np_entry_password.insert(0, panel_left_np_password_placeholder)
            panel_left_np_entry_password.config(fg="grey")
    panel_left_np_entry_password.bind("<FocusIn>", panel_left_np_password_click)
    panel_left_np_entry_password.bind("<FocusOut>", panel_left_np_password_focusout)
    panel_left_np_entry_password.place(x=root.winfo_screenwidth() // 20, y=270, width=root.winfo_screenwidth() // 2.5, height=50)

    panel_left_np_entry_gender = tk.Entry(panel_left_np, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 20))
    panel_left_np_entry_gender.insert(0, panel_left_np_gender_placeholder)
    def panel_left_np_gender_click(event):
        if panel_left_np_entry_gender.get() == panel_left_np_gender_placeholder:
            panel_left_np_entry_gender.delete(0, tk.END)
            panel_left_np_entry_gender.config(fg="#061e41")
    def panel_left_np_gender_focusout(event):
        if panel_left_np_entry_gender.get() == "":
            panel_left_np_entry_gender.insert(0, panel_left_np_gender_placeholder)
            panel_left_np_entry_gender.config(fg="grey")
    panel_left_np_entry_gender.bind("<FocusIn>", panel_left_np_gender_click)
    panel_left_np_entry_gender.bind("<FocusOut>", panel_left_np_gender_focusout)
    panel_left_np_entry_gender.place(x=root.winfo_screenwidth() // 20, y=340, width=root.winfo_screenwidth() // 2.5, height=50)

    panel_left_np_entry_phone = tk.Entry(panel_left_np, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 20))
    panel_left_np_entry_phone.insert(0, panel_left_np_phone_placeholder)
    def panel_left_np_phone_click(event):
        if panel_left_np_entry_phone.get() == panel_left_np_phone_placeholder:
            panel_left_np_entry_phone.delete(0, tk.END)
            panel_left_np_entry_phone.config(fg="#061e41")
    def panel_left_np_phone_focusout(event):
        if panel_left_np_entry_phone.get() == "":
            panel_left_np_entry_phone.insert(0, panel_left_np_phone_placeholder)
            panel_left_np_entry_phone.config(fg="grey")
    panel_left_np_entry_phone.bind("<FocusIn>", panel_left_np_phone_click)
    panel_left_np_entry_phone.bind("<FocusOut>", panel_left_np_phone_focusout)
    panel_left_np_entry_phone.place(x=root.winfo_screenwidth() // 20, y=410, width=root.winfo_screenwidth() // 2.5, height=50)

    panel_left_np_entry_address = tk.Entry(panel_left_np, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 20))
    panel_left_np_entry_address.insert(0, panel_left_np_address_placeholder)
    def panel_left_np_address_click(event):
        if panel_left_np_entry_address.get() == panel_left_np_address_placeholder:
            panel_left_np_entry_address.delete(0, tk.END)
            panel_left_np_entry_address.config(fg="#061e41")
    def panel_left_np_address_focusout(event):
        if panel_left_np_entry_address.get() == "":
            panel_left_np_entry_address.insert(0, panel_left_np_address_placeholder)
            panel_left_np_entry_address.config(fg="grey")
    panel_left_np_entry_address.bind("<FocusIn>", panel_left_np_address_click)
    panel_left_np_entry_address.bind("<FocusOut>", panel_left_np_address_focusout)
    panel_left_np_entry_address.place(x=root.winfo_screenwidth() // 20, y=480, width=root.winfo_screenwidth() // 2.5, height=50)

    def done():
        panel_left_np.pack_forget()
        panel_right_np.pack_forget()
        panel_left_np_block_1.pack_forget()
        panel_left_np_block_2.pack_forget()
        panel_left.pack(side= 'left', fill='y')
        panel_right.pack(side='right', fill='y')

    def insert_new_patient():
        name = panel_left_np_entry_name.get()
        password = panel_left_np_entry_password.get()
        gender = panel_left_np_entry_gender.get()
        phone = panel_left_np_entry_phone.get()
        address = panel_left_np_entry_address.get()

        if not name or name == panel_left_np_name_placeholder or not password or password == panel_left_np_password_placeholder or not gender or gender == panel_left_np_gender_placeholder or not phone or phone == panel_left_np_phone_placeholder or not address or address == panel_left_np_address_placeholder:
            messagebox.showwarning("Error", "Please fill all the fields!")
            return

        cursor.execute("""INSERT INTO existed_patient(name, password, gender, phone_number, address) VALUES (?, ?, ?, ?, ?)""", (name, password, gender, phone, address))
        connection.commit()
        messagebox.showinfo("Successful", "User registration completed successfully.")
        done()

    panel_left_np_submit_button = tk.Button(panel_left_np, text="Submit", relief="flat", font=("Open Sans ExtraBold", 25), bd=0, fg="#061e41", bg="#ffffff", activebackground="#061e41", activeforeground="#ffffff", highlightthickness=0, padx=100, command=insert_new_patient)
    panel_left_np_submit_button.place(y=555, x=root.winfo_screenwidth() // 8)

    #adding panel_right elements
    image = Image.open("../media/image/illustration/2.png")
    image_size = image.resize((712, 468))
    image_photo = ImageTk.PhotoImage(image_size)
    labeled_image = tk.Label(panel_right_np, image=image_photo)
    labeled_image.image = image_photo
    labeled_image.pack(side="top", padx=20, pady=150)

    def back():
        panel_left_np.pack_forget()
        panel_right_np.pack_forget()
        panel_left_np_block_1.pack_forget()
        panel_left_np_block_2.pack_forget()
        panel_left.pack(side= 'left', fill='y')
        panel_right.pack(side='right', fill='y')

    back_button = tk.Button(panel_right_np, text="Back To Login", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff", relief="flat", highlightthickness=0, bd=0, activebackground="#ffffff", activeforeground="#061e41", padx=210, command=back)
    back_button.place(y=593, x=root.winfo_screenwidth() // 49.5)