from argparse import FileType
from tkinter import *
from tkinter import filedialog
import tkinter
from PIL import Image, ImageTk

#create window object
mainWindow = Tk()

#set window title
mainWindow.title("EZLoad")

#set window size
mainWindow.geometry('1024x576')



#TODO: Create an image loading routine
def upload_file():
    global img
    pngType = [('PNG (*.png)', '*.png')] #sets the filetype
    filename = filedialog.askopenfilename(filetypes=pngType) #opens a dialogue
    pil_image = Image.open(filename).resize((624,360)) # sets the images source size
    img = ImageTk.PhotoImage(pil_image)
    b2 =tkinter.Label(mainWindow,image=img) #draws the image as a label
    b2.pack()

#creates a button bound to the upload_file function
uploadButton = tkinter.Button(mainWindow, text="Upload", command=upload_file)
uploadButton.config(width=20, height=2)

#packs widgets and creates a main loop
uploadButton.pack()
mainWindow.mainloop()