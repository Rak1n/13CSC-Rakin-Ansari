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
        self.original_bg_image = Image.open("engin_akyurt-pizza-2766471_1920.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = Label(parent, image=self.bg_photo, width=1920,height=300)
        self.bg_label.image = self.bg_photo
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.header_frame = Label(parent, bg="#153c7d" , width=1920, height=5, borderwidth=10, padx=5)
        self.header_frame.place(y=304)

        #self.image2 = Image.open('Falcon.png')
        #self.phoneix = ImageTk.PhotoImage(self.image2)
        #self.canvas.create_image(150,150,image=self.phoneix)
        #self.image_label = Label(parent, image=self.phoneix, width=420, height = 410, borderwidth=0, border=0)
        #self.image_label.image = self.phoneix
        #self.image_label.place(x=11, y=100)


        # Create button and image
        self.img = Button(parent, borderwidth=0, width=100)
        self.img.place(x=11, y=100)


        self.parent.bind("<Configure>", self.resize_bg)

        self.quiz_frame = Frame(parent, background=background_color)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.quiz_frame, background=background_color)
        self.content_frame.grid()
        self.bg_label.pack()


    def resize_bg(self, event):
        if event.widget == self.parent:
            new_image = self.original_bg_image.resize((event.width, event.height))
            self.bg_photo = ImageTk.PhotoImage(new_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo


if __name__ == "__main__":
        root = tk.Tk()
        root.geometry("400x400")

        root.minsize(1920,1080)
        root.maxsize(2200,1300)
        root.iconbitmap("Falcon.png")
        root.title("General Knowledge Quiz")
        root.geometry("800x700")  # Optional: fixed starting size
        root.configure(bg="#800517")
        Menu_object = Menu(root)
        root.mainloop()
