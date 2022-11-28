name='QR-Code-Generator'
destination='https://i-omgautam.github.io/QR-Code-Generator/'

from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import Button, PhotoImage, ttk
from tkinter.messagebox import showinfo
from turtle import color
import qrcode
import image 

# root window
root = tk.Tk()
root.geometry("400x250")
root.resizable(False, False)
img = PhotoImage(file="C:\\Users\\omgau\\OneDrive\\Desktop\\Personnel_omg\Projects\\QR_Code_Generator\\Hacker-PNG-High-Quality-Image.png")
root.iconphoto(False, img)
root.title('QR Code Generator')

# store qr text and file name
qrtxt = tk.StringVar()
file_name = tk.StringVar()


def save_clicked():
    img = qrcode.make(qr_entry.get())
    name = filename_entry.get() + ".png"
    img.save(name)
    showinfo(title="Qr Code Generator", message="Qr is saved successfully")
    img.show()

# QR frame
qr = ttk.Frame(root)
qr.pack(padx=20, pady=20, fill='x', expand=False)


# qr
qr_label = ttk.Label(qr, text="Enter QR code text:")
qr_label.pack(fill='x', expand=False)

qr_entry = ttk.Entry(qr, textvariable=qrtxt)
qr_entry.pack(fill='x', expand=False, pady=10)
qr_entry.focus()

# filename
filename_label = ttk.Label(qr, text="Enter File Name:")
filename_label.pack(fill='x', expand=False, pady=10)

filename_entry = ttk.Entry(qr, textvariable=file_name)
filename_entry.pack(fill='x', expand=False)

# save button
button = Button(root, text="Save QR Code", fg="#ffffff", command=save_clicked)
button.config(bg="#800000")
button.config(font="Courier")

button.pack(fill='x', expand=False, pady=15)

root.mainloop()
