import tkinter as tk
from tkinter import messagebox
import sqlite3

def patient_form(root, panel_left, panel_right,name):
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
        clear_the_activity_frame()
        p_header = tk.Label(activity_frame, text="Personal Info", font=("Open Sans ExtraBold", 30),background="#061e41", fg="#ffffff")
        p_header.place(x=300, y=15)







    main_menu_button1 = tk.Button(main_menu_frame, text=f"Personal \n Info", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0, command=personal_info)
    main_menu_button1.place(x=20, y=130)
    main_menu_button2 = tk.Button(main_menu_frame, text=f"Order \n Medication", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0)
    main_menu_button2.place(x=20, y=270)
    main_menu_button3 = tk.Button(main_menu_frame, text=f"Order \n Lab Test", font=("Open Sans ExtraBold", 25),width=root.winfo_screenwidth() // 93, fg="#061e41", bg="#ffffff",activeforeground="#ffffff", activebackground="#061e41", highlightthickness=0, bd=0)
    main_menu_button3.place(x=20, y=410)