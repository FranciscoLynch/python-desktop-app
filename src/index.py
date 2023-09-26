from tkinter import Tk, Canvas, Frame, Label, Entry, Button # interfaz
import psycopg2 # driver psql

root = Tk()
root.title('Python & PostgreSQL')

def save_new_product(name, price, stock):
    
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='postgres', 
        host='localhost',
        port='5432')
    
    cursor = conn.cursor()
    query = '''INSERT INTO products(name, price, stock) VALUES (%s, %s, %s,)'''
    cursor.execute(query= (name, price, stock))
    print('Data saved')
    conn.commit()
    conn.close()

# Canvas 
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()

frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) 

label = Label(frame, text='Add a product')
label.grid(row=0, column=1)

# Name input
label = Label(frame, text='Name')
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Price input
label = Label(frame, text='Price')
label.grid(row=2, column=0)

entry_price = Entry(frame)
entry_price.grid(row=2, column=1)

# Stock input
label = Label(frame, text='Stock')
label.grid(row=3, column=0)

entry_stock = Entry(frame)
entry_stock.grid(row=3, column=1)

# Button
button = Button(frame, text='Add', command=lambda:save_new_product(
    entry_name.get(),
    entry_price.get(),
    entry_stock.get()
))
button.grid(row=4, column=1, sticky='we')

root.mainloop()