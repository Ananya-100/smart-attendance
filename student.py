from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD

import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mc



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1270x700')  # self.root.geometry('1400x800')
        self.root.title("Face recognition")

        # variables

        self.var_dep = StringVar()
        self.var_division = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()

        # 1st img
        img1 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img1 = img1.resize((450, 80), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=450, height=80)

        # 2nd img
        img2 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img2 = img2.resize((400, 80), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=400, height=80)

        # 3rd img
        img3 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img3 = img3.resize((450, 80), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=850, y=0, width=450, height=80)
        # bg img
        img4 = Image.open(r"Smart Attendance\Image\StD_BG.jpg")
        img4 = img4.resize((1400, 700), Image.Resampling.LANCZOS)  # 1400x750
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b_img = Label(self.root, image=self.photoimg4)
        b_img.place(x=0, y=80, width=1400, height=700)

        title_lbl = Label(b_img, text="FACE RECOGNITION ATTENDANCE SOFTWARE", font=("Times", "23", "bold "), bg="#F8EDE3",
                          fg="#DC0000")
        title_lbl.place(x=0, y=0, width=1400, height=25)

        main_frame = Frame(b_img, bd=2, bg="white")
        main_frame.place(x=20, y=40, width=1230, height=550)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("Times", 12, "bold "))
        Left_frame.place(x=35, y=10, width=540, height=510)

        img_left = Image.open(r"Smart Attendance\Image\StudentDt.jpg")
        img_left = img_left.resize((520, 80), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=520, height=80)

        # current course
        current_course = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course info",
                                    font=("Times", 12, "bold "))
        current_course.place(x=5, y=88, width=525, height=117)

        # r = 0, c = 1, dept
        d_label = Label(current_course, bd=2, bg="white", relief=RIDGE, text="Department",
                        font=("Times", 12, "bold "))
        d_label.grid(row=0, column=0, padx=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=("Times", 12, "bold "),
                               state="readonly", width=12)
        d_combo["values"] = ("Select dept", "CSE", "IT", "ECE", "EEE", "EE", "ME")
        d_combo.current(0)
        d_combo.grid(row=0, column=1, padx=2, pady=10)

        # r = 0, c = 2, course
        d_label = Label(current_course, bd=2, bg="white", relief=RIDGE, text=" Course ", font=("Times", 12, "bold "))
        d_label.grid(row=0, column=2, padx=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_course, font=("Times", 12, "bold "),
                               state="readonly", width=12)
        d_combo["values"] = ("Select course", "B.Tech", "B.Tech (Hons)")
        d_combo.current(0)
        d_combo.grid(row=0, column=3, padx=2, pady=10)

        # r = 1, c = 1, year
        d_label = Label(current_course, bd=2, bg="white", relief=RIDGE, text="       Year      ",
                        font=("Times", 12, "bold "))
        d_label.grid(row=1, column=0, padx=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_year, font=("Times", 12, "bold "),
                               state="readonly", width=12)
        d_combo["values"] = ("Select year", "1st", "2nd", "3rd", "4th")
        d_combo.current(0)
        d_combo.grid(row=1, column=1, padx=2, pady=10)

        # r = 1, c = 2, sem
        d_label = Label(current_course, bd=2, bg="white", relief=RIDGE, text="Semester", font=("Times", 12, "bold "))
        d_label.grid(row=1, column=2, padx=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_sem, font=("Times", 12, "bold "),
                               state="readonly", width=12)
        d_combo["values"] = ("Select sem", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        d_combo.current(0)
        d_combo.grid(row=1, column=3, padx=2, pady=10)

        # class student info

        class_Student = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="class student info",
                                   font=("Times", 12, "bold "))
        class_Student.place(x=5, y=212, width=525, height=190)

        # roll
        roll_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text="Roll. no",
                           font=("Times", 12, "bold "))
        roll_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        roll_entry = ttk.Entry(class_Student, textvariable=self.var_roll, width=14, font=("Times", 12, "bold "))
        roll_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # name
        name_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text="Name", font=("Times", 12, "bold "))
        name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        name_entry = ttk.Entry(class_Student, textvariable=self.var_name, width=14, font=("Times", 12, "bold "))
        name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # class div
        div_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text=" Divison ",
                          font=("Times", 12, "bold "))
        div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        div_entry = ttk.Entry(class_Student, textvariable=self.var_division, width=14, font=("Times", 12, "bold "))
        div_entry.grid(row=1, column=1, padx=5, sticky=W)

        # gen
        gen_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text=" Gender ", font=("Times", 12, "bold "))
        gen_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        # gen_entry = ttk.Entry(class_Student,textvariable=self.var_gen, width=14,  font=("Times", 12, "bold "))
        # gen_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        gen_combo = ttk.Combobox(class_Student, textvariable=self.var_gen, font=("Times", 12, "bold "),state="readonly", width=12)
        gen_combo["values"] = ("Select gen", "Male", "Female", "Other")
        gen_combo.current(0)
        gen_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # dob
        dob_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text="  D.O.B ", font=("Times", 12, "bold "))
        dob_label.grid(row=2, column=0, padx=5, sticky=W)

        dob_entry = ttk.Entry(class_Student, textvariable=self.var_dob, width=14, font=("Times", 12, "bold "))
        dob_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # ph no
        phno_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text="Phone No. ",
                           font=("Times", 12, "bold "))
        phno_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        phno_entry = ttk.Entry(class_Student, textvariable=self.var_phone, width=14, font=("Times", 12, "bold "))
        phno_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # e mail
        email_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text="E-Mail Id",
                            font=("Times", 12, "bold "))
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student, textvariable=self.var_email, width=14, font=("Times", 12, "bold "))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # addrs
        address_label = Label(class_Student, bd=2, bg="white", relief=RIDGE, text="Address",
                              font=("Times", 12, "bold "))
        address_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student, textvariable=self.var_address, width=14, font=("Times", 12, "bold "))
        address_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # radio buttons 1

        self.var_radio1 = StringVar()
        rad_btn1 = ttk.Radiobutton(class_Student, variable=self.var_radio1, command=self.generate_data,text="Take photo sample", value="Yes")
        rad_btn1.grid(row=4, column=0, padx=10)

        # radio buttons 2

        self.var_radio2 = StringVar()
        rad_btn2 = ttk.Radiobutton(class_Student, variable=self.var_radio1, text="No photo sample", value="No")
        rad_btn2.grid(row=4, column=1, padx=10)

        # #bbuttons frame

        # btn_frame = Frame(class_Student,bd = 2,relief=RIDGE,bg="white")
        # btn_frame.place(x=0,y=210,width=540,height=70)

        # Button-Frame

        class_Save = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, font=("Montserrat", 12, "bold"))
        class_Save.place(x=0, y=418, width=540, height=70)

        b1 = Frame(class_Save, bg="white", relief=RIDGE)
        b1.place(x=0, y=0, width=540, height=35)

        save_btm = Button(b1, command=self.add_data, bd=2, relief=RIDGE, bg="#10A19D", text="Save", width=11,
                          font=("Montserrat", 13, "bold"))
        save_btm.grid(row=0, column=0, padx=2.2)

        update_btm = Button(b1, command=self.update_data, bd=2, relief=RIDGE, bg="#10A19D", text="Update", width=12,
                            font=("Montserrat", 13, "bold"))
        update_btm.grid(row=0, column=1)

        delete_btm = Button(b1, bd=2, relief=RIDGE, bg="#10A19D", text="Delete", width=13, font=("Montserrat", 13, "bold"))
        delete_btm.grid(row=0, column=2)

        reset_btm = Button(b1, command=self.reset_data, bd=2, relief=RIDGE, bg="#10A19D", text="Reset", width=13,
                           font=("Montserrat", 13, "bold"))
        reset_btm.grid(row=0, column=3)

        b2 = Frame(class_Save, bg="white", relief=RIDGE)
        b2.place(x=0, y=35, width=635, height=35)

        photo_btm = Button(b2, bd=2, command=self.generate_data, relief=RIDGE, bg="#7FE9DE", text="Take photo sample", width=26,
                           font=("Montserrat", 13, "bold"))
        photo_btm.grid(row=1, column=0, pady=2)

        update_photo_btm = Button(b2, bd=2, relief=RIDGE, bg="#7FE9DE", text="Update photo sample", width=26,
                                  font=("Montserrat", 13, "bold"))
        update_photo_btm.grid(row=1, column=1)

        # right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Data", font=("Times", 12, "bold "))
        Right_frame.place(x=620, y=10, width=560, height=510)

        img_right = Image.open(r"Smart Attendance\Image\RtImgStD.jpg")
        img_right = img_right.resize((560, 80), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=520, height=80)

        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("Montserrat", 12, "bold"))
        search_frame.place(x=10, y=85, width=540, height=70)

        search_label = Label(search_frame, bd=2, bg="#5CB8E4", relief=RIDGE, text="Search By:",
                             font=("Montserrat", 13, "bold"))
        search_label.grid(row=0, column=0, padx=2.5, pady=2.5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("Montserrat", 12, "bold"), state="readonly", width=10)
        search_combo["values"] = ("Select", "Roll_NO", "Phone_NO")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5)

        search_box = ttk.Entry(search_frame, width=11, font=("Montserrat", 12, "bold"))
        search_box.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search = Button(search_frame, bd=2, relief=RIDGE, bg="#B9FFF8", text="Search", width=8,
                        font=("Montserrat", 12, "bold"))
        search.grid(row=0, column=3, padx=5, pady=5)

        show_all = Button(search_frame, bd=2, relief=RIDGE, bg="#B9FFF8", text="Show All", width=8,
                          font=("Montserrat", 12, "bold"))
        show_all.grid(row=0, column=4, padx=5, pady=5)

        ############## Table Frame ################

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=160, width=540, height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "name", "division", "roll", "gender", "dob", "email", "phone", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("division", text="Division")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("email", text="Email Id")
        self.student_table.heading("phone", text="Phone No.")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    ################Function################
    def add_data(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mc.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_division.get(),
                    self.var_roll.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student deails has been added successfully")
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}")

                # ===========Fetch Data=============

    def fetch_data(self):
        conn = mc.connect(host="localhost", username="root", password="root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student ")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # ============Get Cursor==============

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_name.set(data[4]),
        self.var_division.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gen.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

    # ===========Update function===========
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update current data ?", parent=self.root)
                if Update > 0:
                    conn = mc.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,division=%s,gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,radio1=%s where Roll=%s ",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_name.get(),
                            self.var_division.get(),
                            self.var_gen.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_radio1.get(),
                            int(self.var_roll.get())
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

                # ====================== reset ===============

    def reset_data(self):
        self.var_dep.set("select dept"),
        self.var_course.set("select course"),
        self.var_year.set("select year"),
        self.var_sem.set("select sem"),
        self.var_name.set(""),
        self.var_division.set(""),
        self.var_roll.set(""),
        self.var_gen.set("select gen"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")

    # ================ delete =========================

    def delete_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to delete current data ?", parent=self.root)
                if Update > 0:
                    conn = mc.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from student where roll =")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

        # =============== generate data, set or take photo sample ===================

    def generate_data(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mc.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                uid = 0
                for x in myresult:
                    uid += 1
                my_cursor.execute(
                    "update student set dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,division=%s,gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,radio1=%s where Roll=%s ",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_division.get(),
                        self.var_gen.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        int(self.var_roll.get())
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # =========== load predefined data om face frontals using opencv =======
                face_classifier = cv2.CascadeClassifier(r"C:\python 3.8.0\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # min neighbour = 5 -> 3
                    for (x, y, w, h) in faces:
                        face_img = img[y:y + h, x:x + w]
                        return face_img

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    print(my_frame)
                    print(ret)

                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (600, 600))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = f"data\\{self.var_roll.get()}\\user" + str(uid) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(filename=file_path, img=face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 50:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result", "Generating dataset completed successfully....")

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
