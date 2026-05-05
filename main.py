from tkinter import *
import tk
from PIL import Image, ImageTk
import random

name_list = []
asked = []
score = 0

class Menu:
    def __init__(self, parent):
        background_color = "#e8f9ff"

        self.parent = parent
        self.original_bg_image = Image.open("engin_akyurt-pizza-2766471_1920.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
        self.bg_label = Label(parent, image=self.bg_photo)
        self.bg_label.image = self.bg_photo
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.parent.bind("<Configure>", self.resize_bg)

        self.quiz_frame = Frame(parent, background=background_color)
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.content_frame = Frame(self.quiz_frame, background=background_color)
        self.content_frame.grid()


    def resize_bg(self, event):
        if event.widget == self.parent:
            new_image = self.original_bg_image.resize((event.width, event.height))
            self.bg_photo = ImageTk.PhotoImage(new_image)
            self.bg_label.config(image=self.bg_photo)
            self.bg_label.image = self.bg_photo




if __name__ == "__main__":
        root = Tk()
        root.minsize(1920,1080)
        root.maxsize(1700,400)
        root.iconbitmap("Falcon.png")
        root.title("General Knowledge Quiz")
        root.geometry("800x700")  # Optional: fixed starting size
        root.configure(bg="#800517")
        quizStarter_object = Menu(root)
        root.mainloop()
