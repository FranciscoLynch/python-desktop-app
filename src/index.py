from tkinter import Tk, Canvas, Frame, Label, Entry # interfaz
import psycopg2 # driver psql

root = Tk()
root.title('Python & PostgreSQL')

# Canvas 

canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()

frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

label = Label(frame, text='Add a product')
label.grid(row=0, column=1)

label = Label(frame, text='Name')
label.grid(row=1, column=0)

entryname = Entry(frame)
entryname.grid(row=1, column=1)

root.mainloop()