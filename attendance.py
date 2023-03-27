from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from turtle import bgcolor, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mc
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:      
    
    #fetch data
    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"), ("All file", "*.*")), parent=self.root)        
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data ","No data found",parent=self.root)
                return False
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"), ("All file", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as mf:
                exp_write = csv.writer(mf, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Successfully Exported...")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to:{str(es)}", parent=self.root)
             
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]
        self.var_a_roll.set(row[0])
        self.var_a_name.set(row[1])
        self.var_a_dep.set(row[2])
        self.var_a_time.set(row[3])
        self.var_a_date.set(row[4])
        self.var_a_attend.set(row[5])
    
    def reset_data(self):
        self.var_a_roll.set("")
        self.var_a_name.set("")
        self.var_a_dep.set("")
        self.var_a_time.set("")
        self.var_a_date.set("")
        self.var_a_attend.set("")
        
                        
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x700')  # self.root.geometry('1400x800')
        self.root.title("Face recognition")

       # ============= vaariables =============
        self.var_a_roll = StringVar()
        self.var_a_name = StringVar()
        self.var_a_dep = StringVar()
        self.var_a_time = StringVar()
        self.var_a_date = StringVar()
        self.var_a_attend = StringVar()
       
        # 1st img
        img1 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img1 = img1.resize((500, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=200)

        # 2nd img
        img2 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img2 = img2.resize((400, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=400, height=200)

        # 3rd img
        img3 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img3 = img3.resize((500, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=500, height=200)

        # bg img
        img4 = Image.open(r"Smart Attendance\Image\StD_BG.jpg")
        img4 = img4.resize((1400, 600), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b_img = Label(self.root, image=self.photoimg4)
        b_img.place(x=0, y=200, width=1400, height=700)

        title_lbl = Label(b_img, text="FACE RECOGNITION ATTENDANCE", font=("Times", "25", "bold "), bg="#F8EDE3",fg="#DC0000")
        title_lbl.place(x=0, y=0, width=1400, height=50)

        main_frame = Frame(b_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1200, height=550)

        Left_frame = LabelFrame(main_frame, bd=2, bg="#F8EDE3", relief=RIDGE, text="Student Attendance Details", font=("Times", 12, "bold "))
        Left_frame.place(x=35, y=20, width=540, height=420)

        img_left = Image.open(r"Smart Attendance\Image\StD_BG.jpg")
        img_left = img_left.resize((520, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=520, height=90)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=100, width=525, height=280)

        # roll 
        roll_label = Label(left_inside_frame, bd=2, bg="#F8EDE3", relief=RIDGE, text="Roll No.", font=("Times", 15, "bold "))
        roll_label.grid(row=0, column=0, padx=5, pady=20, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_a_roll, font=("Times", 12, "bold "))
        roll_entry.grid(row=0, column=1, padx=5, pady=20, sticky=W)

        # name
        name_label = Label(left_inside_frame, bd=2, bg="#F8EDE3", relief=RIDGE, text="Name", font=("Times", 15, "bold "))
        name_label.grid(row=1, column=0, padx=5, pady=20, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_a_name, font=("Times", 15, "bold "))
        name_entry.grid(row=1, column=1, padx=5, pady=20, sticky=W)

        # department
        dep_label = Label(left_inside_frame, bd=2, bg="#F8EDE3",
                          relief=RIDGE, text="Department", font=("Times", 15, "bold "))
        dep_label.grid(row=2, column=0, padx=5, pady=20, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_a_dep, font=("Times", 15, "bold "))
        dep_entry.grid(row=2, column=1, padx=5, pady=20, sticky=W)
        
        # time 
        time_label = Label(left_inside_frame, bd=2, bg="#F8EDE3", relief=RIDGE, text="Time:", font=("Times", 15, "bold "))
        time_label.grid(row=0, column=2, padx=4, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_a_time, font=("Times", 15, "bold "))
        time_entry.grid(row=0, column=3, padx=4, pady=5, sticky=W)

        # date
        date_label = Label(left_inside_frame, bd=2, bg="#F8EDE3", relief=RIDGE, text="Date:", font=("Times", 15, "bold "))
        date_label.grid(row=1, column=2, padx=4, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_a_date, font=("Times", 15, "bold "))
        date_entry.grid(row=1, column=3, padx=4, pady=5, sticky=W)

        # attendance
        attendanceLabel = Label(left_inside_frame, bd=2, text="Attendance\nStatus", bg="#F8EDE3", font=("Times", 14, "bold "))
        attendanceLabel.grid(row=2, column=2)

        self.atten_status = ttk.Combobox(left_inside_frame, width=10, textvariable=self.var_a_attend, font=("Times", 13, "bold "), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=2, column=3, pady=5)
        self.atten_status.current(0)

        # ====== button frame ===========        
        b1 = Frame(left_inside_frame, bg="#F8EDE3", relief=RIDGE)
        b1.place(x=0, y=240, width=520, height=35)

        save_btm = Button(b1, bd=2, relief=RIDGE, bg="#10A19D", command=self.importCsv, text="Import csv", width=11,font=("Montserrat", 13, "bold"))
        save_btm.grid(row=0, column=0, padx=2.2)

        update_btm = Button(b1, bd=2, relief=RIDGE, bg="#10A19D", command=self.exportCsv, text="Export csv", width=12,font=("Montserrat", 13, "bold"))
        update_btm.grid(row=0, column=1)

        delete_btm = Button(b1, bd=2, relief=RIDGE, bg="#10A19D", text="Update", width=13, font=("Montserrat", 13, "bold"))
        delete_btm.grid(row=0, column=2)

        reset_btm = Button(b1, bd=2, relief=RIDGE, bg="#10A19D", command=self.reset_data, text="Reset", width=13, font=("Montserrat", 13, "bold"))
        reset_btm.grid(row=0, column=3)

        Right_frame = LabelFrame(main_frame, bd=2, bg="#F8EDE3", relief=RIDGE, text="Attendance Details", font=("Times", 12, "bold "))
        Right_frame.place(x=600, y=20, width=560, height=420)

        Table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="#F8EDE3")
        Table_frame.place(x=5, y=5, width=545, height=390)

        # =============scroll bar====================
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, column=("roll", "name", "dep", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("date", text="Name")
        self.student_table.heading("attendance", text="Attendance Status")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("time", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("attendance", width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()