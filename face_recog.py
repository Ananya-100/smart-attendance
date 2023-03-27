from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mc
import cv2
import os
import numpy as np
from traindata import Train


class Face_recognition:
    # ======================== attendance =======================

    def mark_attendance(self, r, n, d):
        with open("attendance-sheet.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtime = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r}, {n}, {d}, {dtime}, {d1}, present\n")

    # ========================== face recognition ================
    def face_recog(self):
        def draw_boundary(img, classifier, scale_factor, min_neighbours, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scale_factor, min_neighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                uid, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - (predict / 300)))
                print(uid)

                conn = mc.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()

                # showing the details while face detection

                my_cursor.execute("select name from student where Roll = " + str(uid))
                print(my_cursor.fetchone())
                n = str(my_cursor.fetchone()[0])
                #n = "".join(str(n))

                my_cursor.execute("select roll from student where Roll = " + str(uid))
                r = str(my_cursor.fetchone()[0])
                #r = "".join(str(r))

                my_cursor.execute("select dep from student where Roll = " + str(uid))
                d = str(my_cursor.fetchone()[0])
                #d = "".join(str(d))

                if confidence > 77:
                    cv2.putText(img, f"Roll : {r}", (x, y - 54), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name : {n}", (x, y - 36), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department : {d}", (x, y - 18), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(r, n, d)
                else:
                    cv2.rectangle(img, int(x, y), int(x + w, y + h), float(0, 255, 0), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 18), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, w, y, h]

            return coord

        def recognize(img, clf, face_cap):
            coord = draw_boundary(img, face_cap, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        face_cap = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face_cap)
            cv2.imshow("Face Recognition", img)
            self.root.after(30000, lambda: self.root.destroy())
            if cv2.waitKey(10) == ord("a"):
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def __init__(self, root):

        self.root = root
        self.root.geometry('1250x750')  # self.root.geometry('1400x800')
        self.root.title("Face recognition")

        title_lbl = Label(self.root, text="FACE RECOGNIZATION", font=("Times", "25", "bold "), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1400, height=35)

        # ============== img 1 =============

        img_top = Image.open(r"Smart Attendance\Image\Face.jpg")
        img_top = img_top.resize((650, 650), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=650)
        
        #============= button ===============
        
        b1_1 = Button(f_lbl, command=self.face_recog, text="FACE RECOGNITION", cursor="hand2", bg="#c4ff6f", relief=RIDGE, font=("Bahnschrift", 12, "bold"))
        b1_1.place(x=200, y=560, width=250, height=50)
        
        # ================ img 2 ==============

        img_bottom = Image.open(r"Smart Attendance\Image\developers.jpg")
        img_bottom = img_bottom.resize((650, 650), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=650, height=650)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
