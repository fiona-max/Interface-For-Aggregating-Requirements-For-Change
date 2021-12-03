import Functions as a
import tkinter as tk
from tkinter import *

LARGE_FONT = ("Times New Roman", 14)
 
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Aggregated Requirements")
        self.geometry("800x1000")
 
        # this container contains all the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {} # these are pages we want to navigate to
 
        for F in (Menu_Page, Requirements_Page, Add_requirements_Page, Processes_And_Links_Page): # for each page
            frame = F(container, self) # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame(Menu_Page) # let the first page to be the Menu page

        self.update()
 
    def show_frame(self, name):
            frame = self.frames[name]
            frame.update()
            self.frames[name] = frame
            frame.tkraise()


class Menu_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Home Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment
        label = tk.Label(self, text='Click a button to access its functionality', font=LARGE_FONT)
        label.pack(pady=10, padx=10) # center alignment


 
        button1 = tk.Button(self, text='View Requirements', height = 2, width = 50, font =LARGE_FONT, # when click on this button, call the show_frame method to make the Requirements page appear
                            # command=lambda : controller.show_frame(Requirements_Page))
                            command=lambda : [controller.show_frame(Requirements_Page)])
        button1.pack()
        button1 = tk.Button(self, text='Insert Requirements', height = 2, width = 50, font =LARGE_FONT, # when click on this button, call the show_frame method to make the Add requirements page appear
                            command=lambda :[controller.show_frame(Add_requirements_Page)])
        button1.pack()
        button1 = tk.Button(self, text='Processes and Links', height = 2, width = 50, font =LARGE_FONT, # when click on this button, call the show_frame method to make the Add requirements page appear
                            command=lambda :[controller.show_frame(Processes_And_Links_Page)])
        button1.pack()
    

        self.update()
 #class to display button to access their properties
class Requirements_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='List Of Requirements', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text='Click a button to access its functionality', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        # loop To display buttons dynamically
        for req in a.get_requirements():
            frame = Requirements_Details_Page(parent, controller, requirement= a.Requirement.fromDict(req))
            frame.grid(row=0, column=0, sticky="nsew")
            frame.update()
            button = tk.Button(self, text=f'Requirement {req.doc_id}', command=frame.tkraise, )
            button.pack(padx = 3, pady = 3)

        button1 = tk.Button(self, text='Back to Home Page', bg = "black" , fg = "white",
                            command=lambda: controller.show_frame(Menu_Page))
        button1.pack()



        self.update()

#Class to display requirements details
class Requirements_Details_Page(tk.Frame):
    def __init__(self, parent, controller, requirement):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=f'Requirement {requirement.id} details', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text = f"Requirement Definition is : {requirement.definition}")
        label.pack(pady = 10, padx = 10)
        label = tk.Label(self, text=f"Sources of Change are : {requirement.sources}")
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text=f"Dimensions are : {requirement.dimensions}")
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text=f"Processes are  : {requirement.format_property('processes')}")
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text=f"Structures are : {requirement.format_property('structures')}")
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text=f"Constraints are : {requirement.format_property('constraints')}")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='Delete Requirement', command=lambda: [requirement.delete(), controller.show_frame(Requirements_Page)])
        button1.pack(padx = 3, pady = 3)
        frame = Edit_requirements_Page(parent, controller, requirement= requirement)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.update()
        button1 = tk.Button(self, text='Modify Requirement', command=frame.tkraise)
        button1.pack(padx = 3, pady = 3)
        button3 = tk.Button(self, text='Back to Requirements Page', bg = "black" , fg = "white",
                            command=lambda: controller.show_frame(Requirements_Page))
        button3.pack()

        self.update()    


#Class to insert a new requirement and its properties
class Add_requirements_Page(tk.Frame):
    def __init__(self, parent, controller, LEFT=None, RIGHT=None):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Fill the boxes below to insert a new requirement', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        l1 = tk.Label(self, text='Requirement Definition: \n In the form R1: ')
        l1.pack(side = LEFT)
        e1 = Text(self, height=2, width=60)
        e1.pack(side = LEFT)
        l2 = tk.Label(self, text='Source Of Change:\n Choose from the list:\n[Change Audits, Basic Nature, Business Issues, Mission and Policies, Technology]')
        l2.pack(side=LEFT)
        e2 = Text(self, height=2, width=60)
        e2.pack()
        l1 = tk.Label(self, text='Dimension Of Change:\n Choose from the list:\n[Organization and Governance, Business Processes, People, Information(Assets) and Technology]')
        l1.pack(side=LEFT)
        e3 = Text(self, height=2, width=60)
        e3.pack()
        l1 = tk.Label(self, text='Processes Of the Requirement: Enter Processes in the form P21.1')
        l1.pack(side=LEFT)
        e4 = Text(self, height=5, width=60)
        e4.pack()
        l1 = tk.Label(self, text='Structure Of the Requirement: Enter Structure in the form S21.1')
        l1.pack(side=LEFT)
        e5 = Text(self, height=5, width=60)
        e5.pack()
        l1 = tk.Label(self, text='Constraint Of the Requirement: Enter Constraints in the form C21.1')
        l1.pack(side=LEFT)
        e6 = Text(self, height=5, width=60)
        e6.pack()

        # function to clear the add requirements page
        def clear():
            e1.delete("1.0", END)
            e2.delete("1.0", END)
            e3.delete("1.0", END)
            e4.delete("1.0", END)
            e5.delete("1.0", END)
            e6.delete("1.0", END)

        button1 = tk.Button(self, text="Insert new requirement",
            command= lambda: [a.Requirement(definition = e1.get("1.0", "end-1c"), sources= e2.get("1.0", "end-1c"), dimensions = e3.get("1.0", "end-1c"), processes = e4.get("1.0", "end-1c").split("\n"), structures = e5.get("1.0", "end-1c").split("\n"), constraints = e6.get("1.0", "end-1c")).insert().split("\n"), clear()])
        button1.pack(padx = 5, pady =5)
        button1 = tk.Button(self, text='Back to Home Page',bg = "black", fg = "white" ,
                            command=lambda: controller.show_frame(Menu_Page))
        button1.pack(padx = 5, pady =5)
        

        self.update()
#Class to enable the modification of existing requirements
class Edit_requirements_Page(tk.Frame):
    def __init__(self, parent, controller, requirement, LEFT=None):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Fill the boxes below to Modify the requirement', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        nl = "\n"
        l1 = tk.Label(self, text='Requirement Definition:')
        l1.pack(side = LEFT)
        e1 = Text(self, height=2, width=60)
        e1.pack(side = LEFT)
        e1.insert(INSERT, requirement.definition)
        l2 = tk.Label(self, text='Source Of Change:')
        l2.pack(side=LEFT)
        e2 = Text(self, height=2, width = 60)
        e2.pack()
        e2.insert(INSERT, requirement.sources)
        l1 = tk.Label(self, text='Dimension Of Change:')
        l1.pack(side=LEFT)
        e3 = Text(self, height=2, width=60)
        e3.pack()
        e3.insert(INSERT, requirement.dimensions)
        l1 = tk.Label(self, text='Processes Of the Requirement:')
        l1.pack(side=LEFT)
        e4 = Text(self, height=5, width = 60)
        e4.pack(side=LEFT)
        e4.insert(INSERT, nl.join(requirement.processes))
        l1 = tk.Label(self, text='Structure Of the Requirement:')
        l1.pack(side=LEFT)
        e5 = Text(self, height=5, width=60)
        e5.pack()
        e5.insert(INSERT, nl.join(requirement.structures))
        l1 = tk.Label(self, text='Constraint Of the Requirement:')
        l1.pack(side=LEFT)
        e6 = Text(self, height=5, width=60)
        e6.pack()
        e6.insert(INSERT, nl.join(requirement.constraints))


        button1 = tk.Button(self, text="Save changes", 
            command = lambda: [requirement.update(definition = e1.get("1.0", "end-1c"), sources= e2.get("1.0", "end-1c"),dimensions = e3.get("1.0", "end-1c"), processes = e4.get("1.0", "end-1c"),structures = e5.get("1.0", "end-1c"), constraints = e6.get("1.0", "end-1c"))])
        button1.pack(padx = 5, pady =5)
        button1 = tk.Button(self, text='Back to Home Page',bg = "black", fg = "white" ,
                            command=lambda: controller.show_frame(Menu_Page))
        button1.pack(padx = 5, pady =5)

        self.update()
#class to display processes
class Processes_And_Links_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = Scrollbar(self, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack( side = RIGHT, fill = Y )
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        frame = tk.Frame(canvas)
        canvas.create_window((0,0), window=frame, anchor='nw', width=(parent.winfo_width() - scrollbar.winfo_width()))

        label = tk.Label(frame, text='List Of Processes', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        # loop To display buttons dynamically
        for process in a.get_processes():
            new_frame = Processes_Details_Page(parent, controller, process=process)
            new_frame.grid(row=0, column=0, sticky="nsew")
            new_frame.update()
            button = tk.Button(frame, text=f'Process {list(process.keys())[0]}', command=new_frame.tkraise, )
            button.pack(padx = 3, pady = 3)

        button1 = tk.Button(frame, text='Back to Home Page', bg = "black" , fg = "white",
                            command=lambda: controller.show_frame(Menu_Page))
        button1.pack(pady=10, padx=10)


        frame.update()

#Class to display processes details
class Processes_Details_Page(tk.Frame):
    def __init__(self, parent, controller, process):
        tk.Frame.__init__(self, parent)
        process_id = list(process.keys())[0]
        label = tk.Label(self, text=f'Process {process_id} details', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text = list(process.values())[0], font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        links = filter(lambda link: f"P{process_id}" in link, a.get_links())
        for link in links:
            label = tk.Label(self, text=link)
            label.pack(pady=10, padx=10)


        button1 = tk.Button(self, text='Back to Home Page', bg = "black" , fg = "white",
                            command=lambda: controller.show_frame(Menu_Page))
        button1.pack(pady=10, padx=10)
        button2 = tk.Button(self, text='Back to Process & Links Page', bg = "black" , fg = "white",
                            command=lambda: controller.show_frame(Processes_And_Links_Page))
        button2.pack(pady=10, padx=10)

        self.update()





 
if __name__ == '__main__':
    app = MainWindow()
    app.update()
    app.mainloop()
