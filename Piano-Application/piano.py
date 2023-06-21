from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pygame

class Piano:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x300')
        self.root.title("Piano")
        self.root.maxsize(700, 300)
        self.root.minsize(700, 300)
        self.root.configure(bg="white")
        self.create_piano()

        pygame.mixer.init()

    def create_piano(self):
        icon = ImageTk.PhotoImage(Image.open('C:\\Users\\rocks\\OneDrive\\Desktop\\GUI Projects\\Piano-Application\\piano.png'))
        icon_label = Label(self.root, image=icon)
        icon_label.place(x=295, y=10)

        frame1 = Frame(self.root, width=700, height=198, bg="black")
        frame1.place(x=0, y=100)

        for i in range(1, 24):
            if i % 2 != 0:
                button = Button(frame1, padx=10, pady=100, bg="black", fg="white", relief=RAISED,
                                borderwidth=3, cursor="hand2")
            else:
                button = Button(frame1, padx=10, pady=100, bg="white", fg="black", relief=RAISED,
                                borderwidth=2, cursor="hand2")

            button.grid(row=0, column=i)
            button.configure(command=lambda index=i: self.play_sound(index))

    def play_sound(self, index):
        file_path = f'C:\\Users\\rocks\\OneDrive\\Desktop\\GUI Projects\\Piano-Application\\Piano{index}.mp3'
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

if __name__ == '__main__':
    root = tk.Tk()
    piano = Piano(root)
    root.mainloop()