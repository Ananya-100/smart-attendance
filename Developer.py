from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import bgcolor, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mc
import cv2
class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1131x736') #self.root.geometry('1400x800')
        self.root.title("Face recognition")

        title_lbl=Label(self.root,text="Developer🧑‍💻\t\t",font=("times new roman",35,"bold"),bg ="#E7F6F2", fg="#205295")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"Smart Attendance\Image\Devs.png")
        img_top = img_top.resize((1131, 640), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1131, height=736)

        # frame

        


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()