from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random

w = 1920
h = 1080
name_list = []
asked = []
score = 0


class Menu:
    def __init__(self, parent):
        background_color = "#cc3628"

        self.parent = parent
        self.root = root
        self.original_bg_image = Image.open("Screenshot 2026-05-18 124046.png")
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = Label(parent, image=self.bg_photo)
        self.bg_label.image = self.bg_photo
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)



        #self.image2 = Image.open('Falcon.png')
        #self.phoneix = ImageTk.PhotoImage(self.image2)
        #self.canvas.create_image(150,150,image=self.phoneix)
        #self.image_label = Label(parent, image=self.phoneix, width=420, height = 410, borderwidth=0, border=0)
        #self.image_label.image = self.phoneix
        #self.image_label.place(x=11, y=100)


        # Create button and image
        self.button = PhotoImage(file='button_menu (1).png')
        self.img = Label(parent, borderwidth=0, width=200, bg="#cc3628" ,image=self.button,activebackground="#cc3628", activeforeground="white")
        self.img.place(x=60, y=470)

        self.button2 = PhotoImage(file='button_pita.png')
        self.img2 = Button(parent, borderwidth=0, command=self.sides, width=200, bg="#cc3628", image=self.button2, activebackground="#cc3628", activeforeground="white")
        self.img2.place(x=60, y=540)

        self.button3 = PhotoImage(file='spec.png')
        self.img3 = Button(parent, borderwidth=0, width=200, bg="#cc3628", image=self.button3,
                           activebackground="#cc3628", activeforeground="white")
        self.img3.place(x=60, y=610)

        self.button4 = PhotoImage(file='button_main.png')
        self.img4 = Button(parent, borderwidth=0, width=200, bg="#cc3628", image=self.button4,
                           activebackground="#cc3628", activeforeground="white")
        self.img4.place(x=60, y=680)

        self.button5 = PhotoImage(file='button_sides (1).png')
        self.img5 = Button(parent, borderwidth=0, width=200, bg="#cc3628", image=self.button5,
                           activebackground="#cc3628", activeforeground="white")
        self.img5.place(x=61, y=750)

        self.parent.bind("<Configure>", self.resize_bg)

        self.quiz_frame = Frame(parent, background=background_color)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.quiz_frame, background=background_color)
        self.content_frame.grid()
        self.bg_label.pack()

        self.info = Label(text="hi")

    def resize_bg(self, event):
        if event.widget == self.parent:
            new_image = self.original_bg_image.resize((event.width, event.height))
            self.bg_photo = ImageTk.PhotoImage(new_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo

    #Chicken
    #Pita - Teriyaki

    #Fresh
    #plain
    #pita
    #with shredded chicken, fresh veggies, cheese, and yummy teriyaki sauce.


    def sides(self):
        self.image9 = PhotoImage(file='button.png')
        self.img9 = Label(borderwidth=100, width=200, bg="#cc3628", image=self.image9)
        self.img9.place(x=400, y=400)

        self.image12 = PhotoImage(file='button.png')
        self.img12 = Label(borderwidth=100, width=200, bg="#cc3628", image=self.image12)
        self.img12.place(x=800, y=400)

        self.image42 = PhotoImage(file='button.png')
        self.img42 = Label(borderwidth=100, width=200, bg="#cc3628", image=self.image42)
        self.img42.place(x=1200, y=400)

if __name__ == "__main__":
        root = tk.Tk()
        root.geometry("1920x1080")
        root.minsize(1920,1080)
        root.maxsize(2200,1300)
        root.iconbitmap("Falcon.png")
        root.title("General Knowledge Quiz")
        root.configure(bg="#800517")
        Menu_object = Menu(root)
        root.mainloop()
