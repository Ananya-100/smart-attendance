import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from student import Student
from traindata import Train
from Developer import Developer
from face_recog import Face_recognition
from chatbot import ChatBot
from attendance import Attendance
import cv2
import numpy as np

class face_recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x750')  # self.root.geometry('1400x800')
        self.root.title("Face recognition")

        # 1st img
        img1 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img1 = img1.resize((500, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=100)

        # 2nd img
        img2 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img2 = img2.resize((400, 100), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=400, height=100)

        # 3rd img
        img3 = Image.open(r"Smart Attendance\Image\TopPannel.jpg")
        img3 = img3.resize((500, 100), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=500, height=100)
        
        # bg img
        img4 = Image.open(r"Smart Attendance\Image\BG.jpg")
        img4 = img4.resize((1400, 700), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b_img = Label(self.root, image=self.photoimg4)
        b_img.place(x=0, y=100, width=1400, height=700)

        title_lbl = Label(b_img, text="FACE RECOGNITION ATTENDANCE SOFTWARE", font=("Times", "25", "bold "),bg ="#F8EDE3", fg="#DC0000")
        title_lbl.place(x=0, y=0, width=1400, height=35)

        # student button

        img5 = Image.open(r"Smart Attendance\Image\StudentDetails.jpg")
        img5 = img5.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(b_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=50, width=190, height=190)
        b1_1 = Button(b_img, command=self.student_details, text="Student Details", bg="#FFF6C3", font=("8"), cursor="hand2")
        b1_1.place(x=100, y=220, width=190, height=40)

        # detect face button

        img6 = Image.open(r"Smart Attendance\Image\FaceRecognition.jpg")
        img6 = img6.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b2 = Button(b_img, image=self.photoimg6, cursor="hand2", command=self.face_data)
        b2.place(x=380, y=50, width=190, height=190)
        b2_2 = Button(b_img, command=self.face_data, text="Face Recognition", bg="#FFF6C3", font=("8"), cursor="hand2")
        b2_2.place(x=380, y=220, width=190, height=40)

        # attendance

        img7 = Image.open(r"Smart Attendance\Image\Attendance.jpg")
        img7 = img7.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b3 = Button(b_img, command=self.attend, image=self.photoimg7, cursor="hand2", )
        b3.place(x=660, y=50, width=190, height=190)
        b3_3 = Button(b_img, command=self.attend, text="Attendance", bg="#FFF6C3", font=("8"), cursor="hand2")
        b3_3.place(x=660, y=220, width=190, height=40)

        # help desk

        img8 = Image.open(r"Smart Attendance\Image\HelpDesk.jpg")
        img8 = img8.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b4 = Button(b_img, command=self.chat, image=self.photoimg8, cursor="hand2", )
        b4.place(x=950, y=50, width=190, height=190)
        b4_4 = Button(b_img, command=self.chat, text="Help Desk", bg="#FFF6C3", font=("8"), cursor="hand2")
        b4_4.place(x=950, y=220, width=190, height=40)

        # train data

        img9 = Image.open(r"Smart Attendance\Image\TrainData.jpg")
        img9 = img9.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b5 = Button(b_img, command=self.train_classifier, image=self.photoimg9, cursor="hand2")
        b5.place(x=100, y=320, width=190, height=190)
        b5_5 = Button(b_img, command=self.train_classifier ,text="Train Data", bg="#FFF6C3", font=("8"), cursor="hand2")
        b5_5.place(x=100, y=480, width=190, height=40)

        # photos

        img10 = Image.open(r"Smart Attendance\Image\Photos.jpg")
        img10 = img10.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b6 = Button(b_img, command=self.open_img,image=self.photoimg10, cursor="hand2", )
        b6.place(x=380, y=320, width=190, height=190)
        b6_6 = Button(b_img, command=self.open_img, text="Photos", bg="#FFF6C3", font=("8"), cursor="hand2")
        b6_6.place(x=380, y=480, width=190, height=40)

        # developers

        img11 = Image.open(r"Smart Attendance\Image\developers.jpg")
        img11 = img11.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b7 = Button(b_img, command=self.dev, image=self.photoimg11, cursor="hand2", )
        b7.place(x=660, y=320, width=190, height=190)
        b7_7 = Button(b_img, command=self.dev, text="Developers", bg="#FFF6C3", font=("8"), cursor="hand2")
        b7_7.place(x=660, y=480, width=190, height=40)

        # exit

        img12 = Image.open(r"Smart Attendance\Image\exit.jpg")
        img12 = img12.resize((190, 190), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b8 = Button(b_img, command=self.exit, image=self.photoimg12, cursor="hand2", )
        b8.place(x=950, y=320, width=190, height=190)
        b8_8 = Button(b_img, command=self.exit,text="Exit", bg="#FFF6C3", font=("8"), cursor="hand2")
        b8_8.place(x=950, y=480, width=190, height=40)
        
    def open_img(self):
        os.startfile(r"data")
        
    def exit(self):
        self.exit = messagebox.askyesno("Face Recognition", "Do you want to exit")
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    # funuction buttons

    # =============== student details ============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # ============== face recognition =============

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
    
    # ================== help desk =================
    def chat(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
        
    # ================== developer =================
    def dev(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    # ============== train data =============
    #def train(self):
    #    self.new_window = Toplevel(self.root)
    #    self.app = Train(self.new_window)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        uid = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # gray scale conversion
            imageNp = np.array(img, 'uint8')
            uid = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(uid)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # train the the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed !")
    
    # ============== attendence =============
    def attend(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = face_recognizer(root)
    root.mainloop()
