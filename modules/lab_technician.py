import tkinter as tk
from tkinter import messagebox
import sqlite3

def lab_technician_form(root, panel_left, panel_right):
    panel_left.pack_forget()
    panel_right.pack_forget()

    main_frame = tk.Frame(root, bg="#ffffff", width=root.winfo_screenwidth())
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Main Frame Elements
    big_label = tk.Label(main_frame, text="St. Mary Hospital", font=("Open Sans ExtraBold", 55), fg="#061e41", bg="#ffffff")
    big_label.place(x=(root.winfo_screenwidth()//2.57), y=8)
    def logout():
        main_frame.pack_forget()
        panel_left.pack(side= 'left', fill='y')
        panel_right.pack(side= 'right', fill='y')

    log_out = tk.Button(main_frame, text="Log Out", font=("Open Sans ExtraBold", 25), width=root.winfo_screenwidth() // 85, height=1, relief="flat", fg="#ffffff", bg="#061e41", bd=0, activeforeground="#061e41", activebackground="#ffffff", highlightthickness=0, command=logout)
    log_out.place(x=0, y=621)

    #Activity frame
    activity_frame = tk.Frame(main_frame, width=root.winfo_screenwidth()//1.5, height=480, bg="#061e41")
    activity_frame.place(y=125, x=(root.winfo_screenwidth()//3.43))
    #Main menu frame
    main_menu_frame = tk.Frame(main_frame, width=root.winfo_screenwidth() // 4, height=605 , bg="#061e41")
    main_menu_frame.place(y=0, x=0)


    #Main menu elements
    main_menu_label = tk.Label(main_menu_frame, text="Main Menu", font=("Open Sans ExtraBold", 35), fg="#ffffff", bg="#061e41")
    main_menu_label.place(y=30, x=30)

    #access patient record elements
    def clear_the_activity_frame():
        for usages in activity_frame.winfo_children():
            usages.place_forget()
            usages.destroy()

    def personal_info_of_the_patient():
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Personal Info Of the Patient", font=("Open Sans ExtraBold", 30), background="#061e41", fg="#ffffff")
        p_header.place(x=158, y=15)
        enter_text=tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25), bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=65)
        enter_id_placeholder="         Patient Id"

        enter_id=tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
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
        enter_id.place(width= root.winfo_screenwidth()//4, x=260, y=120)
        def grab_submit():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, gender, phone_number, address FROM existed_patient WHERE patient_id = ?", (id_no,))
            p_result = cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return 
            if p_result:
                patient_id = p_result[0]
                name = p_result[1]
                gender = p_result[2]
                phone_number = p_result[3]
                address = p_result[4]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_patient_id.place(x=245, y=180)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_name.place(x=195, y=220)
                v_gender = tk.Label(activity_frame, text=gender, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_gender.place(x=213, y=260)
                v_phone_number = tk.Label(activity_frame, text=phone_number, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_phone_number.place(x=320, y=300)
                v_address = tk.Label(activity_frame, text=address, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_address.place(x=222, y=340)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        enter_submit= tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41", activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0, relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=120, width=50, height=51)
        p_id=tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        p_id.place(x=90, y=180)
        p_name=tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        p_name.place(x=90, y=220)
        p_gender=tk.Label(activity_frame, text="Gender -", font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        p_gender.place(x=90,y=260)
        p_ph = tk.Label(activity_frame, text="Phone Number -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        p_ph.place(x=90, y=300)
        p_address = tk.Label(activity_frame, text="Address -", font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        p_address.place(x=90, y=340)
        p_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20), width=root.winfo_screenwidth()//85, fg="#061e41", bg="#ffffff", activebackground="#061e41", activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0, command=access_patient_records)
        p_back.place(x=60, y=390)

    def medication_history():
        clear_the_activity_frame()
        m_header = tk.Label(activity_frame, text="Medication History", font=("Open Sans ExtraBold", 30), background="#061e41", fg="#ffffff")
        m_header.place(x=255, y=15)
        enter_text=tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25), bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=75)
        enter_id_placeholder="         Patient Id"

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
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=130)
        def grab_submit():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, medication FROM existed_patient WHERE patient_id = ?", (id_no,))
            m_result = cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if m_result:
                patient_id = m_result[0]
                name = m_result[1]
                gender = m_result[2]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_patient_id.place(x=245, y=190)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_name.place(x=195, y=230)
                v_medication = tk.Label(activity_frame, text=gender, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_medication.place(x=269, y=270)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        enter_submit= tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41", activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0, relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=130, width=50, height=51)
        m_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_id.place(x=90, y=190)
        m_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_name.place(x=90, y=230)
        m_medication = tk.Label(activity_frame, text="Medication -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_medication.place(x=90, y=270)
        m_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0, command=access_patient_records)
        m_back.place(x=60, y=390)

    def past_health_history():
        clear_the_activity_frame()
        m_header = tk.Label(activity_frame, text="Past Health History", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        m_header.place(x=245, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=75)
        enter_id_placeholder = "         Patient Id"

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
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=130)
        def grab_submit():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, previous_illnesses, surgeries FROM existed_patient WHERE patient_id=?", (id_no,))
            pa_result=cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if pa_result:
                patient_id = pa_result[0]
                name = pa_result[1]
                previous_illnesses = pa_result[2]
                surgeries = pa_result[3]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_patient_id.place(x=245, y=190)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_name.place(x=195, y=230)
                v_previous_illnesses = tk.Label(activity_frame, text=previous_illnesses, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_previous_illnesses.place(x=360, y=270)
                v_surgeries = tk.Label(activity_frame, text=surgeries, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_surgeries.place(x=246, y=310)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        enter_submit = tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0, relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=130, width=50, height=51)
        pa_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        pa_id.place(x=90, y=190)
        pa_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        pa_name.place(x=90, y=230)
        pa_previous_illnesses= tk.Label(activity_frame, text="Previous Illnesses -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        pa_previous_illnesses.place(x=90, y=270)
        pa_surgeries = tk.Label(activity_frame, text="Surgeries -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        pa_surgeries.place(x=90, y=310)
        p_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20), width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41", activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0, command=access_patient_records)
        p_back.place(x=60, y=390)

        enter_submit = tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41", activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=130, width=50, height=51)

    def lab_test_results():
        clear_the_activity_frame()
        m_header = tk.Label(activity_frame, text="Lab Test Result", font=("Open Sans ExtraBold", 30), bg="#061e41", fg="#ffffff")
        m_header.place(x=295, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25), bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=75)
        enter_id_placeholder = "         Patient Id"

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
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=130)

        def grab_submit():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, lab_test_result FROM existed_patient WHERE patient_id = ?", (id_no,))
            ltr=cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if ltr:
                patient_id = ltr[0]
                name = ltr[1]
                lab_result = ltr[2]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_patient_id.place(x=245, y=190)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_name.place(x=195, y=230)
                v_lab_result = tk.Label(activity_frame, text=lab_result, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_lab_result.place(x=255, y=270)
        lrt_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        lrt_id.place(x=90, y=190)
        lrt_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        lrt_name.place(x=90, y=230)
        lrt_lab_result = tk.Label(activity_frame, text="Lab Result -", font=("Open Sans ExtraBold", 20),bg="#061e41", fg="#ffffff")
        lrt_lab_result.place(x=90, y=270)
        lrt_back = tk.Button(activity_frame, text="Back", font=("Open Sans ExtraBold", 20), width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=access_patient_records)
        lrt_back.place(x=60, y=390)


        enter_submit = tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=130, width=50, height=51)

    #Main Access patient record buttons place
    def access_patient_records():
        clear_the_activity_frame()
        a_header = tk.Label(activity_frame, text="Access patient records", font=("Open Sans ExtraBold", 30), background="#061e41", fg="#ffffff")
        a_header.place(x=216, y=15)
        a_button1 = tk.Button(activity_frame, text="Personal Info of The Patient", font=("Open Sans ExtraBold", 20), fg="#061e41", bg="#ffffff", width=48, activebackground="#061e41", activeforeground="#ffffff", bd=0, highlightthickness=0, command=personal_info_of_the_patient)
        centering_x = root.winfo_screenwidth() // 1.5
        centered_x = (centering_x - a_button1.winfo_width()) // 20
        a_button1.place(x=centered_x, y=110)
        a_button2 = tk.Button(activity_frame, text="Medication History", font=("Open Sans ExtraBold", 20), fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", width=48, bd=0, highlightthickness=0, command=medication_history)
        a_button2.place(x=centered_x, y=200)
        a_button3 = tk.Button(activity_frame, text="Past Health History", font=("Open Sans ExtraBold", 20), fg="#061e41", bg="#ffffff", activebackground="#061e41", activeforeground="#ffffff", width=48, bd=0, highlightthickness=0, command=past_health_history)
        a_button3.place(x=centered_x, y=290)
        a_button4 = tk.Button(activity_frame, text="Lab Test Results", font=("Open Sans ExtraBold", 20), fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", width=48, bd=0, highlightthickness=0, command=lab_test_results)
        a_button4.place(x=centered_x, y=380)
    access_patient_records()

    #Main Update patient lab
    def update_patient_lab_result():
        clear_the_activity_frame()
        u_header = tk.Label(activity_frame, text="Update Patient Lab Result", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        u_header.place(relx=0.5, y=40, anchor="center")
        enter_text = tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25), bg="#061e41", fg="#ffffff")
        enter_text.place(relx=0.5, y=100, anchor="center")
        enter_id_placeholder = "         Patient Id"
        enter_id = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id.insert(0, enter_id_placeholder)

        def grab_submit():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, gender, lab_test_result FROM existed_patient WHERE patient_id = ?", (id_no,))
            p_result = cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if p_result:
                patient_id = p_result[0]
                name = p_result[1]
                gender = p_result[2]
                lab_test_result = p_result[3]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_patient_id.place(x=225, y=250)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_name.place(x=175, y=290)
                v_gender = tk.Label(activity_frame, text=gender, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_gender.place(x=193, y=330)
                v_phone_number = tk.Label(activity_frame, text=lab_test_result, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_phone_number.place(x=237, y=370)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        enter_submit= tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41", activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0, relief='flat', command=grab_submit)
        enter_submit.place(x=635, y=145, width=50, height=51)

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

        enter_id.place(width=root.winfo_screenwidth() // 4, relx=0.5, y=170, anchor="center")
        label = tk.Label(activity_frame, text="Current result", font=("Open Sans ExtraBold", 23), bg="#061e41",fg="#ffffff")
        label.place(x=70, y=200)
        p_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        p_id.place(x=70, y=250)
        p_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        p_name.place(x=70, y=290)
        p_gender = tk.Label(activity_frame, text="Gender -", font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
        p_gender.place(x=70, y=330)
        p_ph = tk.Label(activity_frame, text="Lab Result -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        p_ph.place(x=70, y=370)
        label = tk.Label(activity_frame, text="Update The Result", font=("Open Sans ExtraBold", 23), bg="#061e41",fg="#ffffff")
        label.place(x=550, y=200)
        entry=tk.Entry(activity_frame, font=("Open Sans ExtraBold",25), relief='flat', fg="Grey")
        entry.place(x=550, y=250, width=root.winfo_screenwidth() // 4)
        entry_placeholder = "         New Result"
        entry.insert(0, entry_placeholder)

        def entry_click(event):
            if entry.get() == entry_placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="#061e41")

        def entry_non_click(event):
            if entry.get() == "":
                entry.insert(0, entry_placeholder)
                entry.config(fg="grey")

        entry.bind("<FocusIn>", entry_click)
        entry.bind("<FocusOut>", entry_non_click)

        def submit_new_result():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT patient_id, name, gender, phone_number, address FROM existed_patient WHERE patient_id = ?",
                (id_no,))
            p_result = cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if p_result:
                patient_id = p_result[0]
                name = p_result[1]
                gender = p_result[2]
                phone_number = p_result[3]
                address = p_result[4]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",
                                        bg="#061e41")
                v_patient_id.place(x=245, y=180)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff",
                                  bg="#061e41")
                v_name.place(x=195, y=220)
                v_gender = tk.Label(activity_frame, text=gender, font=("Open Sans ExtraBold", 20), fg="#ffffff",
                                    bg="#061e41")
                v_gender.place(x=213, y=260)
                v_phone_number = tk.Label(activity_frame, text=phone_number, font=("Open Sans ExtraBold", 20),
                                          fg="#ffffff", bg="#061e41")
                v_phone_number.place(x=320, y=300)
                v_address = tk.Label(activity_frame, text=address, font=("Open Sans ExtraBold", 20), fg="#ffffff",
                                     bg="#061e41")
                v_address.place(x=222, y=340)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        submit_button = tk.Button(activity_frame, text="Submit", font=("Open Sans ExtraBold", 20), width=root.winfo_screenwidth()//85, fg="#061e41", bg="#ffffff", activebackground="#061e41", activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0, command= submit_new_result)
        submit_button.place(x=585, y=320)

    main_menu_button1 = tk.Button(main_menu_frame, text=f"Access patient \n records", font=("Open Sans ExtraBold", 25), width=root.winfo_screenwidth()//93, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=access_patient_records)
    main_menu_button1.place(x=20, y=130)
    main_menu_button2 = tk.Button(main_menu_frame, text=f"Update Patient \n lab result", font=("Open Sans ExtraBold", 25), width=root.winfo_screenwidth()//93, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=update_patient_lab_result)
    main_menu_button2.place(x=20, y=270)