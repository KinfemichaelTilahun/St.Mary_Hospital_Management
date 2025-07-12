import tkinter as tk
import sqlite3
from modules import session

def patient_form(root, panel_left, panel_right):
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

    #Personal info
    def personal_info():
        users = session.current_user
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Personal Info", font=("Open Sans ExtraBold", 30), background="#061e41", fg="#ffffff")
        p_header.place(x=310, y=15)
        user=users["name"]
        conn = sqlite3.connect("../db/database_storage.db")
        cursor = conn.cursor()
        cursor.execute("SELECT patient_id, name, password, gender, phone_number, address FROM existed_patient WHERE name = ?",(user,))
        m_result = cursor.fetchone()
        patient_id = m_result[0]
        name = m_result[1]
        password = m_result[2]
        gender = m_result[3]
        p_no = m_result[4]
        address = m_result[5]
        v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
        v_patient_id.place(x=245, y=130)
        v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_name.place(x=195, y=170)
        v_password = tk.Label(activity_frame, text=password, font=("Open Sans ExtraBold", 20),fg="#ffffff", bg="#061e41")
        v_password.place(x=245, y=210)
        v_gender = tk.Label(activity_frame, text=gender, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_gender.place(x=210, y=250)
        v_p_no = tk.Label(activity_frame, text=p_no, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_p_no.place(x=319, y=290)
        v_address = tk.Label(activity_frame, text=address, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_address.place(x=221, y=330)


        m_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_id.place(x=90, y=130)
        m_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_name.place(x=90, y=170)
        m_password = tk.Label(activity_frame, text="Password -", font=("Open Sans ExtraBold", 20),bg="#061e41", fg="#ffffff")
        m_password.place(x=90, y=210)
        m_gender = tk.Label(activity_frame, text="gender -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_gender.place(x=90, y=250)
        m_p_no = tk.Label(activity_frame, text="Phone Number -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_p_no.place(x=90, y=290)
        m_address = tk.Label(activity_frame, text="address -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_address.place(x=90, y=330)
    personal_info()

    def review_medication():
        users = session.current_user
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Review medication", font=("Open Sans ExtraBold", 30), background="#061e41", fg="#ffffff")
        p_header.place(x=250, y=15)
        user = users["name"]
        conn = sqlite3.connect("../db/database_storage.db")
        cursor = conn.cursor()
        cursor.execute("SELECT patient_id, name, medication, verification, explanation FROM existed_patient WHERE name = ?",(user,))
        m_result = cursor.fetchone()
        patient_id = m_result[0]
        name = m_result[1]
        medication = m_result[2]
        verification = m_result[3]
        explanation = m_result[4]
        v_patient_id = tk.Label(activity_frame, text=patient_id, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
        v_patient_id.place(x=245, y=130)
        v_name = tk.Label(activity_frame, text=name, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_name.place(x=195, y=170)
        v_medication = tk.Label(activity_frame, text=medication, font=("Open Sans ExtraBold", 20), fg="#ffffff",bg="#061e41")
        v_medication.place(x=270, y=210)
        v_verification = tk.Label(activity_frame, text=verification, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_verification.place(x=275, y=250)
        v_explanation = tk.Label(activity_frame, text=explanation, font=("Open Sans ExtraBold", 20), fg="#ffffff", bg="#061e41")
        v_explanation.place(x=279, y=290)

        m_id = tk.Label(activity_frame, text="Patient Id -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_id.place(x=90, y=130)
        m_name = tk.Label(activity_frame, text="Name -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_name.place(x=90, y=170)
        m_medication = tk.Label(activity_frame, text="medication -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_medication.place(x=90, y=210)
        m_verification = tk.Label(activity_frame, text="verification -", font=("Open Sans ExtraBold", 20), bg="#061e41", fg="#ffffff")
        m_verification.place(x=90, y=250)
        m_explanation = tk.Label(activity_frame, text="explanation -", font=("Open Sans ExtraBold", 20), bg="#061e41",fg="#ffffff")
        m_explanation.place(x=90, y=290)


    main_menu_button1 = tk.Button(main_menu_frame, text=f"Personal \n Info", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=personal_info)
    main_menu_button1.place(x=20, y=130)
    main_menu_button2 = tk.Button(main_menu_frame, text=f"Review \n Medication", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=review_medication)
    main_menu_button2.place(x=20, y=270)