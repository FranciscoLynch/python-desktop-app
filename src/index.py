from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END # interfaz
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
    cursor.execute(query, (name, price, stock))
    
    print('Data saved')
    
    conn.commit()
    conn.close()

    display_products()

def display_products(): 
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='postgres', 
        host='localhost',
        port='5432')
    
    cursor = conn.cursor() 
    query = '''SELECT * FROM products'''
    cursor.execute(query)
    
    row = cursor.fetchall()
    
    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row: 
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def search_data(id):
    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='postgres', 
        host='localhost',
        port='5432')
    
    cursor = conn.cursor() 
    query = '''SELECT * FROM products WHERE id=%s'''
    cursor.execute(query, (id))
    
    row = cursor.fetchone()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    display_search_result(row)
    
    conn.commit()
    conn.close() 

def display_search_result(row): 
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, row)


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
button.grid(row=4, column=1, sticky=W+E)

# Search

label = Label(frame, text='Search data')
label.grid(row=5, column=0)

label = Label(frame, text='Search by ID')
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

# Button for search
button = Button(frame, text='Search', command=lambda:search_data(id_search.get()))
button.grid(row=6, column=2, sticky=W+E)


display_products()

root.mainloop()