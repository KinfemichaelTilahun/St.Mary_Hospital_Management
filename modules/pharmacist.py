import tkinter as tk
from tkinter import messagebox
import sqlite3

def pharmacist_form(root, panel_left, panel_right):
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

    #Verify Work Space
    def verify_medication():
        clear_the_activity_frame()
        m_header = tk.Label(activity_frame, text="Verify Medication", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        m_header.place(x=255, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=73)
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
        enter_id.place(width=root.winfo_screenwidth() // 4, x=260, y=128)

        def grab_submit():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, medication, current_illness, verification FROM existed_patient WHERE patient_id = ?", (id_no,))
            m_result = cursor.fetchone()
            if id_no == enter_id_placeholder or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if m_result:
                patient_id = m_result[0]
                name = m_result[1]
                medication = m_result[2]
                current_illness= m_result[3]
                verification= m_result[4]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_patient_id.place(x=245, y=180)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_name.place(x=195, y=220)
                v_current_illness = tk.Label(activity_frame, text=current_illness, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_current_illness.place(x=319, y=260)
                v_medication = tk.Label(activity_frame, text=medication, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_medication.place(x=269, y=300)
                v_verification = tk.Label(activity_frame, text=verification, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
                v_verification.place(x=275, y=340)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        enter_submit = tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=128, width=50, height=51)
        m_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_id.place(x=90, y=180)
        m_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_name.place(x=90, y=220)
        m_current_illness = tk.Label(activity_frame, text="Current Illness -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_current_illness.place(x=90, y=260)
        m_medication = tk.Label(activity_frame, text="Medication -", font=("Open Sans ExtraBold", 20),bg="#061e41", fg="#ffffff")
        m_medication.place(x=90, y=300)
        m_verification = tk.Label(activity_frame, text="Verification -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_verification.place(x=90, y=340)

        def verified():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE existed_patient SET verification = ? WHERE patient_id = ?", ("Verified", id_no))
            conn.commit()
            conn.close()

        def not_verified():
            id_no = enter_id.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE existed_patient SET verification = ? WHERE patient_id = ?", ("Not Verified", id_no))
            conn.commit()
            conn.close()


        m_verified = tk.Button(activity_frame, text="Verified", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=verified)
        m_verified.place(x=100, y=390)
        m_not_verified = tk.Button(activity_frame, text="Not Verified", font=("Open Sans ExtraBold", 20), width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff", activebackground="#061e41",activeforeground="#ffffff", relief="flat", bd=0, highlightthickness=0,command=not_verified)
        m_not_verified.place(x=400, y=390)

    def explain_medication():
        clear_the_activity_frame()
        m_header = tk.Label(activity_frame, text="Explain Medication", font=("Open Sans ExtraBold", 30), bg="#061e41",fg="#ffffff")
        m_header.place(x=255, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=75)
        enter_id_placeholder1 = "         Patient Id"

        enter_id1 = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id1.insert(0, enter_id_placeholder1)

        def enter_id_click1(event):
            if enter_id1.get() == enter_id_placeholder1:
                enter_id1.delete(0, tk.END)
                enter_id1.config(fg="#061e41")

        def enter_id_non_click1(event):
            if enter_id1.get() == "":
                enter_id1.insert(0, enter_id_placeholder1)
                enter_id1.config(fg="grey")

        enter_id1.bind("<FocusIn>", enter_id_click1)
        enter_id1.bind("<FocusOut>", enter_id_non_click1)
        enter_id1.place(width=root.winfo_screenwidth() // 4, x=285, y=130)

        enter_text = tk.Label(activity_frame, text="Enter the Explanation", font=("Open Sans ExtraBold", 25), bg="#061e41", fg="#ffffff")
        enter_text.place(x=268, y=185)

        enter_id_placeholder = "                                      Explanation"

        enter_id = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 20))
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
        enter_id.place(width=root.winfo_screenwidth() // 2, height=130 ,x=(root.winfo_screenwidth()//1.5)//8, y=240)

        def submit():
            try:
                patient_id=enter_id1.get()
                explanation=enter_id.get()

                if patient_id == "" or patient_id == enter_id_placeholder1 or explanation == "" or explanation == enter_id_placeholder:
                    messagebox.showwarning("Missing Information","All fields must be filled in completely.")
                    return

                conn = sqlite3.connect("../db/database_storage.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM existed_patient WHERE patient_id = ?",(patient_id,))
                result = cursor.fetchone()

                if result is None:
                    messagebox.showwarning("Invalid ID","The Patient Id you entered does not exist!")
                    return

                cursor.execute("UPDATE existed_patient SET explanation = ? WHERE patient_id = ?", (explanation, patient_id))
                messagebox.showinfo("Sent!", "The explanation has been sent successfully!")
                conn.commit()
                conn.close()

            except Exception as e:
                messagebox.showwarning("Error", f"{e}")

        submit = tk.Button(activity_frame, text="submit", font=("Open Sans ExtraBold", 20),width=root.winfo_screenwidth() // 85, fg="#061e41", bg="#ffffff",activebackground="#061e41", activeforeground="#ffffff", relief="flat", bd=0,highlightthickness=0, command=submit)
        submit.place(x=300, y=390)

    def update_medicine():
        clear_the_activity_frame()
        m_header = tk.Label(activity_frame, text="Update Medicine", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        m_header.place(x=275, y=15)
        enter_text = tk.Label(activity_frame, text="Enter the patient id", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text.place(x=285, y=73)
        enter_id_placeholder1 = "         Patient Id"

        enter_id1 = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_id1.insert(0, enter_id_placeholder1)

        def enter_id_click1(event):
            if enter_id1.get() == enter_id_placeholder1:
                enter_id1.delete(0, tk.END)
                enter_id1.config(fg="#061e41")

        def enter_id_non_click1(event):
            if enter_id1.get() == "":
                enter_id1.insert(0, enter_id_placeholder1)
                enter_id1.config(fg="grey")

        enter_id1.bind("<FocusIn>", enter_id_click1)
        enter_id1.bind("<FocusOut>", enter_id_non_click1)
        enter_id1.place(width=root.winfo_screenwidth() // 4, x=260, y=128)

        def grab_submit():
            id_no = enter_id1.get()
            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT patient_id, name, medication, current_illness, verification FROM existed_patient WHERE patient_id = ?", (id_no,))
            m_result = cursor.fetchone()
            if id_no == enter_id_placeholder1 or id_no == "":
                messagebox.showwarning("Input Error", "Please enter ID number.")
                return
            if m_result:
                patient_id = m_result[0]
                name = m_result[1]
                medication = m_result[2]
                v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_patient_id.place(x=245, y=200)
                v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_name.place(x=195, y=240)
                v_medication = tk.Label(activity_frame, text=medication, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
                v_medication.place(x=385, y=280)
            else:
                messagebox.showwarning("Error", "Please provide a valid ID number.")

        enter_submit = tk.Button(activity_frame, text="➜", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=grab_submit)
        enter_submit.place(x=610, y=128, width=50, height=51)

        m_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_id.place(x=90, y=200)
        m_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_name.place(x=90, y=240)
        m_medication = tk.Label(activity_frame, text="Current Medication -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_medication.place(x=90, y=280)

        enter_text2 = tk.Label(activity_frame, text="Enter the new medication", font=("Open Sans ExtraBold", 25),bg="#061e41", fg="#ffffff")
        enter_text2.place(x=230, y=335)
        enter_med_placeholder = "    New Medication"

        enter_med = tk.Entry(activity_frame, bg="#ffffff", fg="grey", relief="flat", font=("Open Sans ExtraBold", 25))
        enter_med.insert(0, enter_med_placeholder)

        def enter_med_click(event):
            if enter_med.get() == enter_med_placeholder:
                enter_med.delete(0, tk.END)
                enter_med.config(fg="#061e41")

        def enter_med_non_click(event):
            if enter_med.get() == "":
                enter_med.insert(0, enter_med_placeholder)
                enter_med.config(fg="grey")

        enter_med.bind("<FocusIn>", enter_med_click)
        enter_med.bind("<FocusOut>", enter_med_non_click)
        enter_med.place(width=root.winfo_screenwidth() // 4, x=200, y=390)

        def update():
            id_no = enter_id1.get()

            if id_no == "" or id_no == enter_id_placeholder1:
                messagebox.showwarning("Missing Information", "Please check the current medication before you update!")
                return

            medication = enter_med.get()

            if medication == "" or medication == enter_med_placeholder:
                messagebox.showwarning("Missing Information", "Please enter the new medication!")
                return

            conn = sqlite3.connect("../db/database_storage.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM existed_patient WHERE patient_id = ?", (id_no,))
            result = cursor.fetchone()

            if result is None:
                messagebox.showwarning("Invalid ID", "The Patient Id you entered does not exist!")
                return

            cursor.execute("UPDATE existed_patient SET medication = ? WHERE patient_id = ?", (medication, id_no))
            messagebox.showinfo("Update!", "The medication has been updated successfully!")
            conn.commit()
            conn.close()

        update_submit = tk.Button(activity_frame, text="Update", font=("Open Sans ExtraBold", 30), bg="#ffffff", fg="#061e41",activeforeground="#ffffff", activebackground="#061e41", bd=0, highlightthickness=0,relief='flat', command=update)
        update_submit.place(x=550, y=390, width=160, height=51)

    main_menu_button1 = tk.Button(main_menu_frame, text=f"Access patient \n records", font=("Open Sans ExtraBold", 25), width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=access_patient_records)
    main_menu_button1.place(x=20, y=130)
    main_menu_button2 = tk.Button(main_menu_frame, text=f"Verify \n medication", font=("Open Sans ExtraBold", 25), width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=verify_medication)
    main_menu_button2.place(x=20, y=270)
    main_menu_button3 = tk.Button(main_menu_frame, text=f"Explain \n medication", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff", activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=explain_medication)
    main_menu_button3.place(x=20, y=410)
    main_menu_button4 = tk.Button(main_menu_frame, text=f"Update \n medicine", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0,command=update_medicine)

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

    main_menu_button_next = tk.Button(main_menu_frame, text=f"Next", font=("Open Sans ExtraBold", 19),width=root.winfo_screenwidth() // 80, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0,bd=0, command=next_fun)
    main_menu_button_next.place(x=31, y=540)
    main_menu_button_back = tk.Button(main_menu_frame, text=f"Back", font=("Open Sans ExtraBold", 19),width=root.winfo_screenwidth() // 80, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0,bd=0, command=back_fun)
