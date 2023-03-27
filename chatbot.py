from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("chat bot")
        self.root.geometry("520x472")
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root, bd=4, bg="#F3EFE0", width=490)
        main_frame.pack()

        img_chat = Image.open(r"Smart Attendance\Image\chatbotimg.jpg")
        img_chat = img_chat.resize((60, 50), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=520, compound=LEFT, image=self.photoimg, text="       Query Counter", font=("Bodoni MT Black", 26), bg="#434242", fg='white')
        title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=14, bd=3, relief=RAISED, font=("arial", 15), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=1, bg="#222222", width=490)
        btn_frame.pack()

        label = Label(btn_frame, text="     Type    ", font=("arial", 13, "bold"), bg="#B3FFAE", fg="#247881")
        label.grid(row=0, column=0, padx=1, sticky=W)

        self.entry=StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry,width=29,font=('arial',14,'bold'))
        self.entry1.grid(row=0, column=1, padx=1, sticky=W)

        self.send = Button(btn_frame, text=" send▶ ", command=self.send, font=('arial', 12, 'bold'),bg="#FFD4B2",fg="#3D5656")
        self.send.grid(row=0, column=2, padx=2, sticky=W)

        self.clear = Button(btn_frame,command=self.clear, text="clear 🗑️", font=('arial', 12, 'bold'),width=8,bg="#E0144C",fg='white')
        self.clear.grid(row=1, column=0, padx=2, sticky=W)

        self.message = ""
        self.msg_lbl = Label(btn_frame, text=self.message, font=("arial", 13, "bold"), bg="#222222", fg="#247881")
        self.msg_lbl.grid(row=1, column=1, padx=1, sticky=W)

    #=============== function dec ==============

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        self.text.yview(END)
        if self.entry.get() == '':
            self.message = "Please enter something"
            self.msg_lbl.config(text=self.message, fg="#E0144C")
        else:
            self.message = ""
            self.msg_lbl.config(text=self.message, fg="#E0144C")
            data = '\t' * 2 + 'You : ' + self.entry.get()
            self.text.insert(END, '\n' + data)
        greetings = ["hi", "hello", "hey", "hey there", "whats up", "yo", "excuse me"]
        if self.entry.get() in greetings:
            self.text.insert(END, '\n\n Sonic : ' + "Hey there, how can I help you?")


        else:
            self.text.insert(END, '\n\n Sonic : ' + "Sorry I didn't get it")


if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
