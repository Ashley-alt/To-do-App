#import tkinter libraries
from tkinter import *
import tkinter.messagebox

task_window =Tk()

#giving a title
task_window.title("To-Do list") 

#creating 2 frames top and bottom 
task_frame = tkinter.Frame(task_window).pack()
button_frame = tkinter.Frame(task_window).pack(side = BOTTOM)

#click button events

def add_task():
    task = task_entered.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        task_entered.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="please enter a task")


def delete_task():
    try:
  #      listbox_tasks.get(listbox_tasks.curselection()) #only gets tasks thats have been selected
        listbox_tasks.delete( tkinter.ACTIVE) #deletes tasks that are active (selected)
    except:
        tkinter.messagebox.showwarning(title="warning", message="please select a task")


def delete_all_tasks():
    end_index = listbox_tasks.index("end") #index of the position after the last item in listbox
    if end_index != 0:
        listbox_tasks.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="there are no tasks to delete")

def completed_tasks():
    marked= listbox_tasks.curselection()
    temp= marked[0]
    temp_marked=listbox_tasks.get(marked) #store the text of selected item in a string
    temp_marked= temp_marked + (" ✔")  #update it 
    #delete it then insert it 
    listbox_tasks.delete(temp)
    listbox_tasks.insert(temp,temp_marked)



#application widget layout  

listbox_tasks=Listbox(task_frame,height=15,width=50)  
listbox_tasks.pack()

task_entered = Entry(task_frame, width=50, bg="black", fg="white")
task_entered.pack()

add_task_button = Button(button_frame, text="add task", fg="blue", command= add_task)
add_task_button.pack(side= TOP)

delete_task_button = Button(button_frame, text="delete task", fg="blue", command=delete_task)
delete_task_button.pack()

clear_all_button = Button(button_frame, text="clear all tasks", fg="blue", command=delete_all_tasks)
clear_all_button.pack(side= BOTTOM)

completed_button = Button(button_frame, text="mark as completed", fg="blue", command=completed_tasks)
completed_button.pack()

task_window.mainloop()