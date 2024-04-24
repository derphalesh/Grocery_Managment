import mysql.connector as connector
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
import databaseConnector as dbc
from datetime import date


def login():
    user = username.get()
    pas = password.get()

    if user == "admin" and pas == "admin":
        windows_root1.destroy()
        page2()
    elif user == "" and pas == "":
        messagebox.showerror("Invalid", "Please enter Username and Password")
    elif user == "":
        messagebox.showerror("Invalid", "Username is required")
    elif pas == "":
        messagebox.showerror("Invalid", "Password is required")
    elif user != "admin" and pas != "admin":
        messagebox.showerror(
            "Invalid", "Please enter valid Username and Password")
    elif user != "admin":
        messagebox.showerror(
            "Invalid", "Please enter valid Username ")
    elif pas != "admin":
        messagebox.showerror(
            "Invalid", "Please enter valid Password")


def main_screen():
    global windows_root1
    global username
    global password

    windows_root1 = Tk()
    windows_root1.geometry("700x434")
    windows_root1.configure(bg="burlywood1")
    windows_root1.title("DBMS COURSE PROJECT")

    label1 = Label(text="Grocery Management System",
                   font=("arial", 25, "bold"), fg="black", bg="burlywood1")
    label1.pack(pady=50)

    Login = Frame(windows_root1, bg="burlywood4")
    Login.pack()

    subFrame = Frame(Login, width=650, height=234, bg="burlywood3")
    subFrame.pack(padx=10, pady=10)

    Label(Login, text="Username", font=("arial", 15),
          bg="burlywood3").place(x=200, y=50)
    Label(Login, text="Password", font=(
        "arial", 15), bg="burlywood3").place(x=200, y=120)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(subFrame, textvariable=username,
                           width=14, bd=1, font=("arial", 18))
    entry_username.place(x=320, y=40)
    entry_password = Entry(subFrame, textvariable=password,
                           width=14, bd=1, font=("arial", 18), show="*")
    entry_password.place(x=320, y=110)

    Button(subFrame, text="Login", height="2",
           width=23, command=login, bg="#1F92FF", font=("verdana", 9, "bold")).place(x=260, y=180)

    windows_root1.mainloop()


def page2():
    global root2
    root2 = Tk()
    root2.configure(bg="burlywood1")
    root2.geometry("700x434")
    root2.title("DBMS COURSE PROJECT")

    label1 = Label(text="Grocery Management System",
                   font=("arial", 25, "bold"), fg="black", bg="burlywood1")
    label1.pack(pady=40)

    frame1 = Frame(root2, bg="burlywood4")
    frame1.pack()

    subFrame = Frame(frame1, width=650, height=250, bg="burlywood3")
    subFrame.pack(padx=10, pady=10)
    button1 = Button(subFrame, text="Add a New Lot", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=page3).place(x=230, y=0)
    button2 = Button(subFrame, text="Check my Stoke", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=myStock).place(x=230, y=50)
    button3 = Button(subFrame, text="Make a Bill", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=page4).place(x=230, y=100)
    button4 = Button(subFrame, text="Manage my stock", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=manageMyStock).place(x=230, y=150)
    button5 = Button(subFrame, text="Logout", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=initialBack).place(x=230, y=200)

    root2.mainloop()


def manageMyStock():
    try:
        root2.destroy()
    except:
        print("root not exist")

    global root5
    root5 = Tk()
    root5.configure(bg="burlywood1")
    root5.geometry("700x434")
    root5.title("DBMS COURSE PROJECT")

    label1 = Label(text="Manage Grocery Stock",
                   font=("arial", 25, "bold"), fg="black", bg="burlywood1")
    label1.pack(pady=50)

    frame1 = Frame(root5, bg="burlywood1")
    frame1.pack()

    subFrame = Frame(frame1, width=650, height=250, bg="burlywood1")
    subFrame.pack(padx=10, pady=10)

    button1 = Button(subFrame, text="Delete Item", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=deleteItem).place(x=230, y=0)
    button2 = Button(subFrame, text="Expired Products", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=expiredProducts).place(x=230, y=50)
    button3 = Button(subFrame, text="Limiting Products", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=limitingProducts).place(x=230, y=100)
    button4 = Button(subFrame, text="Transaction History", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=transactionHistory).place(x=230, y=150)
    button5 = Button(subFrame, text="Back", height=2,
                     width=25, bd=2, bg="#1F92FF", font=("verdana", 9, "bold"), command=back0).place(x=230, y=200)

    root5.mainloop()


def transactionHistory():
    today = date.today()
    conn = connector.connect(
        host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')
    query = f"select date,productName,quantity,totalAmount from my_schema.customerentry"

    cur = conn.cursor()
    cur.execute(query)
    win2 = Tk()
    win2.geometry("805x425")
    win2.title("Left Stock")
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win2, column=(
        "DATE", "PRODUCT", "QUANTITY", "TOTAL AMOUNT"), show='headings', height=20)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="DATE")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="PRODUCT")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="QUANTITY")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="TOTAL AMOUNT")
    for i in cur:
        tree.insert('', 'end', text="1", values=i)

    tree.pack()

    win2.mainloop()


def limitingProducts():
    today = date.today()
    conn = connector.connect(
        host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')
    query = f"select productName,mfg,exp,price,quantity from my_schema.grocery where quantity<limitingquantity"

    cur = conn.cursor()
    cur.execute(query)
    win3 = Tk()
    win3.geometry("1005x430")
    win3.title("Left Stock")
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win3, column=(
        "Product", "MFG", "EXP", "Price", "Quantity"), show='headings', height=20)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Product")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="MFG")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="EXP")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Price")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Quantity")
    for i in cur:
        tree.insert('', 'end', text="1", values=i)

    tree.pack()

    win3.mainloop()


def expiredProducts():
    today = date.today()
    conn = connector.connect(
        host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')
    query = f"select productName,mfg,exp,price,quantity from my_schema.grocery where exp<'{today}'"

    cur = conn.cursor()
    cur.execute(query)
    win2 = Tk()
    win2.geometry("1005x430")
    win2.title("Left Stock")
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win2, column=(
        "Product", "MFG", "EXP", "Price", "Quantity"), show='headings', height=20)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Product")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="MFG")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="EXP")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Price")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Quantity")
    for i in cur:
        tree.insert('', 'end', text="1", values=i)

    tree.pack()

    win2.mainloop()


def deleteItem():
    root5.destroy()
    global product_name_delete
    global root6
    root6 = Tk()
    root6.configure(bg="burlywood1")
    root6.geometry("450x284")
    root6.title("DBMS COURSE PROJECT")

    label1 = Label(root6, text="Delete Item",
                   font=("arial", 25, "bold"), fg="black", bg="burlywood1")
    label1.pack(pady=20)

    Login = Frame(root6, bg="burlywood1")
    Login.pack()

    subFrame = Frame(Login, width=650, height=234, bg="burlywood1")
    subFrame.pack(padx=10, pady=10)

    Label(Login, text="Product Name", font=(
        "arial", 15), bg="burlywood1").place(x=50, y=30)

    product_name_delete = StringVar()

    entry_username = Entry(subFrame, textvariable=product_name_delete,
                           width=15, bd=2, font=("arial", 18))
    entry_username.place(x=195, y=20)

    Button(subFrame, text="Delete", height="2",
           width=20, bg="#1F92FF", font=("verdana", 9, "bold"), command=deleteItemFromStock).place(x=60, y=70)
    Button(subFrame, text="Back", height="2",
           width=20, bg="#1F92FF", font=("verdana", 9, "bold"), command=deleteBack).place(x=210, y=70)

    root6.mainloop()


def deleteItemFromStock():
    obj2 = dbc.MyDBHelper()
    obj2.deleteEntity(product_name_delete.get())
    messagebox.showinfo("showinfo", f"{product_name_delete.get()} deleted !")
    root6.destroy()
    manageMyStock()


def deleteBack():
    root6.destroy()
    manageMyStock()


def back0():
    root5.destroy()
    page2()


def myStock():
    conn = connector.connect(
        host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')
    query = "select productName,mfg,exp,price,quantity from my_schema.grocery"
    cur = conn.cursor()
    cur.execute(query)
    win = Tk()
    win.geometry("1005x430")
    win.title("Left Stock")
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win, column=(
        "Product", "MFG", "EXP", "Price", "Quantity"), show='headings', height=20)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Product")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="MFG")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="EXP")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Price")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Quantity")
    for i in cur:
        tree.insert('', 'end', text="1", values=i)

    tree.pack()

    win.mainloop()


def initialBack():
    root2.destroy()
    main_screen()


def page3():
    root2.destroy()
    global root3
    global product_name
    global price
    global quantity
    global mfg_date
    global exp_date
    global lim_quantity
    root3 = Tk()
    root3.configure(bg="burlywood1")
    root3.geometry("700x434")
    root3.title("DBMS COURSE PROJECT")
    label0 = Label(text="Add a New Lot",
                   font=("arial", 25, "bold"), fg="black", bg="burlywood1")
    label0.pack(pady=20)
    frame1 = Frame(root3, bg="burlywood1")
    frame1.pack()

    subFrame = Frame(frame1, width=650, height=400, bg="burlywood1")
    subFrame.pack(padx=10, pady=10)
    label1 = Label(subFrame, text="Product name :", font=(
        35), bg="burlywood1").place(x=90, y=0)
    label2 = Label(subFrame, text="Price :", font=(35),
                   bg="burlywood1").place(x=90, y=40)
    label3 = Label(subFrame, text="Quantity :", font=(35),
                   bg="burlywood1").place(x=90, y=80)
    label4 = Label(subFrame, text="Lim Quantity :",
                   font=(35), bg="burlywood1").place(x=90, y=120)
    label5 = Label(subFrame, text="MFG :", font=(
        25), bg="burlywood1").place(x=90, y=160)
    label6 = Label(subFrame, text="EXP :", font=(
        25), bg="burlywood1").place(x=90, y=200)
    product_name = StringVar()
    price = IntVar()
    quantity = IntVar()
    lim_quantity = IntVar()
    mfg_date = StringVar()
    exp_date = StringVar()
    entry31 = Entry(subFrame, textvariable=product_name,
                    width=25, font=("arial", 15)).place(x=250, y=5)
    entry32 = Entry(subFrame, textvariable=price, width=25,
                    font=("arial", 15)).place(x=250, y=45)
    entry33 = Entry(subFrame, textvariable=quantity,
                    width=25, font=("arial", 15)).place(x=250, y=85)
    entry34 = Entry(subFrame, textvariable=lim_quantity, width=25,
                    font=("arial", 15)).place(x=250, y=125)
    entry35 = Entry(subFrame, textvariable=mfg_date,
                    width=25, font=("arial", 15)).place(x=250, y=165)
    entry36 = Entry(subFrame, textvariable=exp_date,
                    width=25, font=("arial", 15)).place(x=250, y=205)
    button1 = Button(subFrame, text="Submit", height="2", width=18,
                     bd=4, bg="#1F92FF", font=("verdana", 9, "bold"), command=newLotSubmit).place(x=90, y=270)
    button2 = Button(subFrame, text="Add a new Product", height="2",
                     width=18, bd=4, bg="#1F92FF", font=("verdana", 9, "bold")).place(x=250, y=270)
    button3 = Button(subFrame, text="Back", height="2",
                     width=18, bd=4, bg="#1F92FF", font=("verdana", 9, "bold"), command=back1).place(x=410, y=270)

    root3.mainloop()


def newLotSubmit():
    obj = dbc.MyDBHelper()
    obj.insertData(product_name.get(), price.get(), mfg_date.get(),
                   exp_date.get(), lim_quantity.get(), quantity.get())
    messagebox.showinfo("showinfo", "New Lot is added to database")


def back1():
    root3.destroy()
    page2()


def page4():
    root2.destroy()

    global root4
    global prd_name
    global pric
    global quant
    global amt
    root4 = Tk()
    root4.configure(bg="burlywood1")
    root4.geometry("700x434")
    root4.title("DBMS COURSE PROJECT")
    label0 = Label(text="Make a Bill",
                   font=("arial", 25, "bold"), fg="black", bg="burlywood1")
    label0.pack(pady=20)
    frame1 = Frame(root4, bg="burlywood1")
    frame1.pack()

    subFrame = Frame(frame1, width=650, height=400, bg="burlywood1")
    subFrame.pack(padx=10, pady=10)

    label1 = Label(subFrame, text="Product name :",
                   font=(35), bg="burlywood1").place(x=90, y=10)
    label2 = Label(subFrame, text="Price :", font=(35),
                   bg="burlywood1").place(x=90, y=50)
    label3 = Label(subFrame, text="Quantity :", font=(35),
                   bg="burlywood1").place(x=90, y=90)
    label4 = Label(subFrame, text="Amount :", font=(35),
                   bg="burlywood1").place(x=90, y=130)

    prd_name = StringVar()
    pric = IntVar()
    quant = IntVar()
    amt = IntVar()

    entry1 = Entry(subFrame, bd=2, textvariable=prd_name,
                   width=25, font=("arial", 15)).place(x=250, y=10)
    entry2 = Entry(subFrame, bd=2, textvariable=pric,
                   width=25, font=("arial", 15)).place(x=250, y=50)
    entry3 = Entry(subFrame, bd=2, textvariable=quant,
                   width=25, font=("arial", 15)).place(x=250, y=90)
    entry4 = Entry(subFrame, bd=2, textvariable=amt,
                   width=25, font=("arial", 15)).place(x=250, y=130)
    button1 = Button(subFrame, text="Print", height="2", width=18,
                     bd=2, command=printBill, bg="#1F92FF", font=("verdana", 9, "bold")).place(x=90, y=220)
    button2 = Button(subFrame, text="Add new Product", height="2",
                     width=18, bd=2, bg="#1F92FF", font=("verdana", 9, "bold")).place(x=250, y=220)
    button3 = Button(subFrame, text="Back", height="2",
                     width=18, bd=2, command=back2, bg="#1F92FF", font=("verdana", 9, "bold")).place(x=410, y=220)

    root4.mainloop()


def printBill():
    today = date.today()
    global myvar
    myvar = 0
    conn = connector.connect(
        host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')
    query = f"select price from my_schema.grocery where productName = '{prd_name.get()}'"
    cur = conn.cursor()
    cur.execute(query)
    for i in cur:
        myvar = int(i[0])
    pric.set(myvar)
    amt.set(quant.get()*myvar)
    obj3 = dbc.MyDBHelper()
    obj3.billingChanges(prd_name.get(), quant.get())

    conn = connector.connect(
        host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')

    # date = yyyy-mm-dd
    query = "insert into my_schema.customerentry(date,productName,quantity,totalAmount)values('{}','{}',{},{})".format(
        today, prd_name.get(), quant.get(), amt.get())
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()


def back2():
    root4.destroy()
    page2()


main_screen()
