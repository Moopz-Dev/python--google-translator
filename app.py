# Translator Desktop App

# imports
from cgitb import text
from tkinter import *
from googletrans import Translator

# commands


def _translate():
    message = text1.get('1.0', 'end-1c')
    translator = Translator()
    output = translator.translate(text=message, src="en", dest="th")
    text2.delete('1.0', 'end')
    text2.insert('end', output.text)


def _clear():
    text1.delete('1.0', 'end')
    text2.delete('1.0', 'end')
    print("Texts cleared")


    # instantiation of main window
root = Tk()
root.title("Google Translator (EN -TH)")
root.geometry("530x300")
root.maxsize(530, 300)
root.minsize(530, 300)

# widgets
label = Label(text="English - Thai", font=('Arial', 24, 'bold'))
label.place(x=150, y=20)

# storing English String
text1 = Text(root, width=30, height=10)
text1.place(x=30, y=70)

# storing Thai String
text2 = Text(root, width=30, height=10)
text2.place(x=260, y=70)

# buttons
btn_translate = Button(root, text="แปลภาษา", command=_translate)
btn_translate.place(x=180, y=250)

btn_clear = Button(root, text="Clear", command=_clear)
btn_clear.place(x=280, y=250)


# mainloop
root.mainloop()
