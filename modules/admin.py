import tkinter as tk
from tkinter import messagebox
import sqlite3

def admin_form(root, panel_left, panel_right):
    panel_left.pack_forget()
    panel_right.pack_forget()

    main_frame = tk.Frame(root, bg="#ffffff", width=root.winfo_screenwidth())
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Main Frame Elements
    big_label = tk.Label(main_frame, text="St. Mary Hospital", font=("Open Sans ExtraBold", 55), fg="#061e41",bg="#ffffff")
    big_label.place(x=(root.winfo_screenwidth() // 2.57), y=8)

    def logout():
        main_frame.pack_forget()
        panel_left.pack(side='left', fill='y')
        panel_right.pack(side='right', fill='y')

    log_out = tk.Button(main_frame, text="Log Out", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 85, height=1, relief="flat", fg="#ffffff", bg="#061e41", bd=0,activeforeground="#061e41", activebackground="#ffffff", highlightthickness=0, command=logout)
    log_out.place(x=0, y=621)

    # Activity frame
    activity_frame = tk.Frame(main_frame, width=root.winfo_screenwidth() // 1.5, height=480, bg="#061e41")
    activity_frame.place(y=125, x=(root.winfo_screenwidth() // 3.43))
    # Main menu frame
    main_menu_frame = tk.Frame(main_frame, width=root.winfo_screenwidth() // 4, height=605, bg="#061e41")
    main_menu_frame.place(y=0, x=0)

    # Main menu elements
    main_menu_label = tk.Label(main_menu_frame, text="Main Menu", font=("Open Sans ExtraBold", 35), fg="#ffffff",bg="#061e41")
    main_menu_label.place(y=30, x=30)

    def clear_the_activity_frame():
        for usages in activity_frame.winfo_children():
            usages.place_forget()
            usages.destroy()

    def add_doctor():
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Add A Doctor", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        p_header.place(x=295, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the doctor's name", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=225, y=65)
        enter_id_placeholder = "     Doctor's name"

        enter_id = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id.insert(0, enter_id_placeholder)

        def enter_id_click(event):
            if enter_id.get() == enter_id_placeholder:
                enter_id.delete(0, tk.END)
                enter_id.config(fg="#061e41")

        def enter_id_non_click(event):
            if enter_id.get() == "":
                enter_id.insert(0, enter_id_placeholder)
                enter_id.config(fg="grey")

        enter_id.bind("<FocusIn>", enter_id_click)
        enter_id.bind("<FocusOut>", enter_id_non_click)
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=120)

        enter_text2 = tk.Label(activity_frame, text="Enter the doctor's password", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text2.place(x=190, y=200)
        enter_id2_placeholder = " Doctor's password"

        enter_id2 = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id2.insert(0, enter_id2_placeholder)

        def enter_id2_click(event):
            if enter_id2.get() == enter_id2_placeholder:
                enter_id2.delete(0, tk.END)
                enter_id2.config(fg="#061e41")

        def enter_id2_non_click(event):
            if enter_id2.get() == "":
                enter_id2.insert(0, enter_id2_placeholder)
                enter_id2.config(fg="grey")

        enter_id2.bind("<FocusIn>", enter_id2_click)
        enter_id2.bind("<FocusOut>", enter_id2_non_click)
        enter_id2.place(width=root.winfo_screenwidth() // 4, x=260, y=255)

        def add_doc():
            name = enter_id.get()
            password = enter_id2.get()
            if name == "" or name == enter_id_placeholder or password == "" or password == enter_id2_placeholder:
                messagebox.showwarning("Warning", "Please fill the required information!")
                return
            response = messagebox.askyesno("Are you sure?",f"do you want to add {name} as a Doctor?")
            if response:
                conn = sqlite3.connect("../db/database_storage.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO doctor (name, password) VALUES (?, ?)", (name, password))
                conn.commit()
                conn.close()
                enter_id.delete(0, tk.END)
                enter_id2.delete(0, tk.END)
            else:
                enter_id.delete(0, tk.END)
                enter_id2.delete(0, tk.END)

        enter_submit = tk.Button(activity_frame, text="Add", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=add_doc)
        enter_submit.place(x=360, y=340, width=150, height=51)

        p_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=manage_doctors)
        p_back.place(x=600, y=390)

    def remove_doctor():
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Remove A Doctor", font=("Open Sans ExtraBold", 30), background="#061e41",fg="#ffffff")
        p_header.place(x=255, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the doctor's name", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=225, y=65)
        enter_id_placeholder = "     Doctor's name"

        enter_id = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id.insert(0, enter_id_placeholder)

        def enter_id_click(event):
            if enter_id.get() == enter_id_placeholder:
                enter_id.delete(0, tk.END)
                enter_id.config(fg="#061e41")

        def enter_id_non_click(event):
            if enter_id.get() == "":
                enter_id.insert(0, enter_id_placeholder)
                enter_id.config(fg="grey")

        enter_id.bind("<FocusIn>", enter_id_click)
        enter_id.bind("<FocusOut>", enter_id_non_click)
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=120)

        def remove_doc():
            name = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            if name == "" or name == enter_id_placeholder:
                messagebox.showwarning("Warning!", "Please fill the required information!")
                return
            cursor.execute("SELECT name FROM doctor WHERE name = ?", (name,))
            result = cursor.fetchall()
            if result:
                response = messagebox.askyesno("Are you sure?", f"do you want to remove {name}")
                if response:
                    cursor.execute("DELETE FROM doctor WHERE name = ?", (name,))
                    conn.commit()
                    enter_id.delete(0, tk.END)
                else:
                    enter_id.delete(0, tk.END)
            else:
                messagebox.showwarning("Not Found!","the doctor's name that you have specified is not found!")
                enter_id.delete(0, tk.END)
                conn.close()
        enter_submit = tk.Button(activity_frame, text="remove", font=("Open Sans ExtraBold", 30), bg="#ffffff",fg="#061e41", activeforeground="#ffffff", activebackground="#061e41", bd=0,highlightthickness=0, relief='flat', command=remove_doc)
        enter_submit.place(x=325, y=190, width=200, height=51)
        p_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=manage_doctors)
        p_back.place(x=600, y=390)

    def manage_doctors():
        clear_the_activity_frame()
        a_header = tk.Label(activity_frame, text="Manage Doctors", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        a_header.place(x=280, y=15)
        a_button1 = tk.Button(activity_frame, text="Add a doctor", font=("Open Sans ExtraBold", 20),fg="#061e41", bg="#ffffff", width=48, activebackground="#061e41",activeforeground="#ffffff", bd=0, highlightthickness=0, command=add_doctor)
        centering_x = root.winfo_screenwidth() // 1.5
        centered_x = (centering_x - a_button1.winfo_width()) // 20
        a_button1.place(x=centered_x, y=110)
        a_button2 = tk.Button(activity_frame, text="Remove a doctor", font=("Open Sans ExtraBold", 20), fg="#061e41",bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", width=48, bd=0,highlightthickness=0, command=remove_doctor)
        a_button2.place(x=centered_x, y=200)
    manage_doctors()

    def add_pharmacist():
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Add A Pharmacist", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        p_header.place(x=255, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the Pharmacist's name", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=175, y=65)
        enter_id_placeholder = " Pharmacist's name"

        enter_id = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id.insert(0, enter_id_placeholder)

        def enter_id_click(event):
            if enter_id.get() == enter_id_placeholder:
                enter_id.delete(0, tk.END)
                enter_id.config(fg="#061e41")

        def enter_id_non_click(event):
            if enter_id.get() == "":
                enter_id.insert(0, enter_id_placeholder)
                enter_id.config(fg="grey")

        enter_id.bind("<FocusIn>", enter_id_click)
        enter_id.bind("<FocusOut>", enter_id_non_click)
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=120)

        enter_text2 = tk.Label(activity_frame, text="Enter the Pharmacist's password", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text2.place(x=150, y=200)
        enter_id2_placeholder = "pharmacist's password"

        enter_id2 = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id2.insert(0, enter_id2_placeholder)

        def enter_id2_click(event):
            if enter_id2.get() == enter_id2_placeholder:
                enter_id2.delete(0, tk.END)
                enter_id2.config(fg="#061e41")

        def enter_id2_non_click(event):
            if enter_id2.get() == "":
                enter_id2.insert(0, enter_id2_placeholder)
                enter_id2.config(fg="grey")

        enter_id2.bind("<FocusIn>", enter_id2_click)
        enter_id2.bind("<FocusOut>", enter_id2_non_click)
        enter_id2.place(width=root.winfo_screenwidth() // 4, x=260, y=255)

        def add_ph():
            name = enter_id.get()
            password = enter_id2.get()
            if name == "" or name == enter_id_placeholder or password == "" or password == enter_id2_placeholder:
                messagebox.showwarning("Warning", "Please fill the required information!")
                return
            response = messagebox.askyesno("Are you sure?",f"do you want to add {name} as a Pharmacist?")
            if response:
                conn = sqlite3.connect("../db/database_storage.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO pharmacist (name, password) VALUES (?, ?)", (name, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("pharmacist added successfully", f"pharmacist {name} has been registered in the system, and the provided password has been securely stored.")
                enter_id.delete(0, tk.END)
                enter_id2.delete(0, tk.END)
            else:
                enter_id.delete(0, tk.END)
                enter_id2.delete(0, tk.END)

        enter_submit = tk.Button(activity_frame, text="Add", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=add_ph)
        enter_submit.place(x=360, y=340, width=150, height=51)

        p_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=manage_pharmacist)
        p_back.place(x=600, y=390)

    def remove_pharmacist():
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Remove A Pharmacist", font=("Open Sans ExtraBold", 30), background="#061e41",fg="#ffffff")
        p_header.place(x=200, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the Pharmacist's name", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=180, y=65)
        enter_id_placeholder = "Pharmacist's name"

        enter_id = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id.insert(0, enter_id_placeholder)

        def enter_id_click(event):
            if enter_id.get() == enter_id_placeholder:
                enter_id.delete(0, tk.END)
                enter_id.config(fg="#061e41")

        def enter_id_non_click(event):
            if enter_id.get() == "":
                enter_id.insert(0, enter_id_placeholder)
                enter_id.config(fg="grey")

        enter_id.bind("<FocusIn>", enter_id_click)
        enter_id.bind("<FocusOut>", enter_id_non_click)
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=120)

        def remove_ph():
            name = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            if name == "" or name == enter_id_placeholder:
                messagebox.showwarning("Warning!", "Please fill the required information!")
                return
            cursor.execute("SELECT name FROM pharmacist WHERE name = ?", (name,))
            result = cursor.fetchall()
            if result:
                response = messagebox.askyesno("Are you sure?", f"do you want to remove {name}")
                if response:
                    cursor.execute("DELETE FROM pharmacist WHERE name = ?", (name,))
                    conn.commit()
                    conn.close()
                    enter_id.delete(0, tk.END)
                else:
                    enter_id.delete(0, tk.END)
            else:
                messagebox.showwarning("Not Found!","the pharmacist's name that you have specified is not found!")
                enter_id.delete(0, tk.END)
                conn.close()
        enter_submit = tk.Button(activity_frame, text="remove", font=("Open Sans ExtraBold", 30), bg="#ffffff",fg="#061e41", activeforeground="#ffffff", activebackground="#061e41", bd=0,highlightthickness=0, relief='flat', command=remove_ph)
        enter_submit.place(x=325, y=190, width=200, height=51)
        p_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=manage_pharmacist)
        p_back.place(x=600, y=390)

    def manage_pharmacist():
        clear_the_activity_frame()
        a_header = tk.Label(activity_frame, text="Manage Pharmacist", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        a_header.place(x=250, y=15)
        a_button1 = tk.Button(activity_frame, text="Add a Pharmacist", font=("Open Sans ExtraBold", 20),fg="#061e41", bg="#ffffff", width=48, activebackground="#061e41",activeforeground="#ffffff", bd=0, highlightthickness=0, command=add_pharmacist)
        centering_x = root.winfo_screenwidth() // 1.5
        centered_x = (centering_x - a_button1.winfo_width()) // 20
        a_button1.place(x=centered_x, y=110)
        a_button2 = tk.Button(activity_frame, text="Remove a Pharmacist", font=("Open Sans ExtraBold", 20), fg="#061e41",bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", width=48, bd=0,highlightthickness=0, command=remove_pharmacist)
        a_button2.place(x=centered_x, y=200)

    main_menu_button1 = tk.Button(main_menu_frame, text=f"Manage \n doctors", font=("Open Sans ExtraBold", 25), width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=manage_doctors)
    main_menu_button1.place(x=20, y=130)
    main_menu_button2 = tk.Button(main_menu_frame, text=f"Manage \n pharmacist", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=manage_pharmacist)
    main_menu_button2.place(x=20, y=270)
    main_menu_button3 = tk.Button(main_menu_frame, text=f"Manage \n lab technician", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0)
    main_menu_button3.place(x=20, y=410)
    main_menu_button4 = tk.Button(main_menu_frame, text=f"Manage \n patient", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0,)

    def next_fun():
        main_menu_button_back.place(x=31, y=130)
        main_menu_button4.place(x=20, y=204)
        main_menu_button1.place_forget()
        main_menu_button2.place_forget()
        main_menu_button3.place_forget()
        main_menu_button_next.place_forget()

    def back_fun():
        main_menu_button_back.place_forget()
        main_menu_button4.place_forget()
        main_menu_button1.place(x=20, y=130)
        main_menu_button2.place(x=20, y=270)
        main_menu_button3.place(x=20, y=410)
        main_menu_button_next.place(x=31, y=540)

    main_menu_button_next = tk.Button(main_menu_frame, text=f"Next", font=("Open Sans ExtraBold", 19),width=root.winfo_screenwidth() // 80, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0,bd=0, command=next_fun)
    main_menu_button_next.place(x=31, y=540)
    main_menu_button_back = tk.Button(main_menu_frame, text=f"Back", font=("Open Sans ExtraBold", 19),width=root.winfo_screenwidth() // 80, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0,bd=0, command=back_fun)
