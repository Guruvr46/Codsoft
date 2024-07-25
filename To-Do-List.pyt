from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do-list")
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-do-list-App',
                           font='ariel, 25 bold', width=10, bd=5, bg='violet', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='ariel, 18 bold', width=10, bd=5, bg='violet', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='ariel, 18 bold', width=10, bd=5, bg='violet', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23,
                                 font='ariel, 20 italic bold')
        self.main_text.place(x=200, y=100)

        self.text = Text(self.root, bd=5, height=2, width=24,
                         font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font='sarif', width=10,
                             bd=5, bg='violet', fg='black', command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif', width=10,
                              bd=5, bg='violet', fg='black', command=self.delete)
        self.button2.place(x=30, y=220)

        self.load_tasks()

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def delete(self):
        try:
            selected = self.main_text.curselection()[0]
            self.main_text.delete(selected)
            self.update_file()
        except IndexError:
            pass

    def update_file(self):
        with open('data.txt', 'w') as file:
            tasks = self.main_text.get(0, END)
            for task in tasks:
                file.write(task + '\n')

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()