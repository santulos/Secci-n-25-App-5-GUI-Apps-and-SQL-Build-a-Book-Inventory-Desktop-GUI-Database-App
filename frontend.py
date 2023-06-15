from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    try:
        global selected_tupla
        index=list1.curselection()[0]
        selected_tupla=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tupla[1])
        e2.delete(0,END)
        e2.insert(END,selected_tupla[2])
        e3.delete(0,END)
        e3.insert(END,selected_tupla[3])
        e4.delete(0,END)
        e4.insert(END,selected_tupla[4])
    except IndexError:
        pass
    

def delete_command():
    backend.delete(selected_tupla[0])

def update_command():
    backend.update(selected_tupla[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    



window=Tk()

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(column=0,row=0)

l2=Label(window,text="Author")
l2.grid(column=2,row=0)

l3=Label(window,text="Year")
l3.grid(column=0,row=1)

l4=Label(window,text="ISBN")
l4.grid(column=2,row=1)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(column=1,row=0)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(column=3,row=0)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(column=1,row=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(column=3,row=1)

list1=Listbox(window, height=6, width=35)
list1.grid(column=0,row=2,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(column=2,row=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(column=3,row=2)

b2=Button(window,text="Search entry", width=12, command=search_command)
b2.grid(column=3,row=3)

b3=Button(window,text="Add entry", width=12, command=add_command)
b3.grid(column=3,row=4)

b4=Button(window,text="Update", width=12, command=update_command)
b4.grid(column=3,row=5)

b5=Button(window,text="Delete", width=12, command=delete_command)
b5.grid(column=3,row=6)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(column=3,row=7)


window.mainloop()
