import tkinter as tk
import StudentGrader as sg
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog

class StudentGraderGUI:
    #class level variables
    COURIER_FONT = 'Courier'
    TIMES_FONT = 'Times New Roman'
    BOLD_FONT = 1
    
    '''class using tkinter to create a simple grade entry for students '''
    def __init__(self):
        
        #create a list of students
        self.__student_list = []
        
        #main window
        self.main_window = tk.Tk()
        #set main window geometry
        self.main_window.geometry('650x500')
        #window title
        self.main_window.title('Student Grader GUI')
        
        #create label with text
        self.text_label = tk.Label(self.main_window,
                                   text = 'Student Grader',
                                   fg = 'green',
                                   bg = 'white',
                                   font = ('Courier', 14, 'bold italic'))
        self.text_label.pack(side = 'top')
        
        #create a label with an image
        self.pythonImage = tk.PhotoImage(file = 'checkmark.gif')
        #create label with the image
        self.image_label = tk.Label(self.main_window,
                                    image = self.pythonImage)
        self.image_label.pack(side = 'top')
        
        
        #create frame to hold widgets
        self.graderFrame = tk.Frame(self.main_window)
        #create label and entry for student name
        self.student_label = tk.Label(self.graderFrame, text = 'Student Name:')
        self.student_entry = tk.Entry(self.graderFrame, width = 20)
        #create label and entry for assigntment type
        self.assignment_label = tk.Label(self.graderFrame, text = 'Assignment:')
        self.assignment_entry = tk.Entry(self.graderFrame, width = 20)
        #create label and entry for score
        self.score_label = tk.Label(self.graderFrame, text = 'Score:')
        self.score_entry = tk.Entry(self.graderFrame, width = 20)
        
        #place widgets in grid
        self.student_label.grid(row = 0, column = 0, padx = 5, pady = 3)
        self.student_entry.grid(row = 0, column = 1, padx = 5, pady = 3)
        self.assignment_label.grid(row = 1, column = 0, padx = 5, pady = 3)
        self.assignment_entry.grid(row = 1, column = 1, padx = 5, pady = 3)
        self.score_label.grid(row = 2, column = 0, padx = 5, pady = 3)
        self.score_entry.grid(row = 2, column = 1, padx = 5, pady = 3)
        
        #create frame to hold buttons
        self.buttonFrame = tk.Frame(self.main_window)
        #create buttons
        self.add_button = tk.Button(self.buttonFrame, text = 'Add',
                                    command = self.add_student)
        self.show_button = tk.Button(self.buttonFrame, text = 'Display',
                                     command = self.display_grade)
        self.clear_button = tk.Button(self.buttonFrame, text = 'Clear',
                                      command = self.clear_entry)
        self.exit_button = tk.Button(self.buttonFrame, text = 'Exit',
                                     command = self.exit_app)
        
        #pack buttons into frame
        self.add_button.pack(side = 'left', padx = 5)
        self.show_button.pack(side = 'left', padx = 5)
        self.clear_button.pack(side = 'left', padx = 5)
        self.exit_button.pack(side = 'left', padx = 5)
        
        #create a frame to hold listbox and scroller
        self.displayFrame = tk.Frame(self.main_window)
        
        #check button for font weight
        self.font_weight = tk.IntVar()
        self.font_weight.set(StudentGraderGUI.BOLD_FONT)
        self.bold_check = tk.Checkbutton(self.displayFrame,
                                         text = 'Bold',
                                         variable = self.font_weight)
        
        #radio buttons for font family
        self.font_family = tk.StringVar()
        self.font_family.set(StudentGraderGUI.COURIER_FONT)
        self.courier_button = tk.Radiobutton(self.displayFrame,
                                             text = 'Courier',
                                             variable = self.font_family,
                                             value = StudentGraderGUI.COURIER_FONT)
        self.times_button = tk.Radiobutton(self.displayFrame,
                                             text = 'Times New Roman',
                                             variable = self.font_family,
                                             value = StudentGraderGUI.TIMES_FONT)
        
        #scrollbar and listbox
        self.scrollbar = tk.Scrollbar(self.displayFrame, orient = tk.VERTICAL)
        
        self.listbox = tk.Listbox(self.displayFrame,
                                  yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.listbox.yview)
        self.listbox = tk.Listbox(self.displayFrame,
                                  width = 30)
        
        #pack radio buttons, check button, scrollbar, and listbox into frame
        self.courier_button.pack(side = 'left')
        self.times_button.pack(side = 'left')
        self.bold_check.pack(side = 'top')
        self.scrollbar.pack(side = 'right', fill = tk.Y)
        self.listbox.pack(side = 'left', fill = tk.BOTH, expand = 1)
        
        #place frames into window
        self.graderFrame.pack(side = 'top', pady = 5)
        self.buttonFrame.pack(side = 'top', pady = 5)
        self.displayFrame.pack(side = 'top', pady = 5)
        
        #create a menu bar on top
        self.menubar = tk.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)
        
        #add options to menu bar
        self.file_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'Save Student Info...',
                                   command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit',
                                   command = self.exit_app)
        
        #add about menu option
        self.help_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'Help', menu = self.help_menu)
        self.help_menu.add_command(label = 'About',
                                   command = self.show_about)
        
        #start window event loop
        self.main_window.mainloop()
        
    def add_student(self):
        #get text from the entry fields
        stu = self.student_entry.get()
        assign = self.assignment_entry.get()
        score = self.score_entry.get()
        
        #check for a positive score
        try:
            score = int(score)
            if score < 0:
                raise ValueError()
        except ValueError:
            #display error message box
            tk.messagebox.showerror('ERROR',
                                    'Score must be at least 0!')
            #set focus to score
            self.score_entry.focus()
        else:
            #add to the student list
            self.__student_list.append(sg.StudentGrader(stu, assign, int(score)))
            
            #show that the student was added to list
            tk.messagebox.showinfo('Info', 'Student\'s grade added to list')
            #reset fields
            self.clear_entry()
        
    def display_grade(self):
        #clear list box to start
        self.listbox.delete(0, tk.END)
        
        #check user selection for font type and set the listbox font
        if self.font_weight.get() == StudentGraderGUI.BOLD_FONT:
            fontToUse = tk.font.Font(family = self.font_family.get(),
                                     weight = 'bold')
        else:
            fontToUse = tk.font.Font(family = self.font_family.get(),
                                     weight = 'normal')
        #set font to use
        self.listbox.config(font = fontToUse)
        
        #add student info to list box
        for stu in self.__student_list:
            student_string = '{:5} - {:3} - {:.2f}'.format(stu.name,
                                                       stu.assignment,
                                                       stu.score)
            self.listbox.insert(tk.END, student_string)
        
    def clear_entry(self):
        #remove text from entry
        self.student_entry.delete(0, tk.END)
        self.assignment_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)
        #reset focus
        self.student_entry.focus()
        
    def exit_app(self):
        #ask user if they want to exit
        response = tk.messagebox.askyesno('Confirm',
                                          'Are you sure you wish to exit?')
        if response == True:
            self.main_window.destroy()
            
    def save_file(self):
        #get file name from user
        file_name = tk.filedialog.asksaveasfilename(initialdir = '/',
                                                    filetypes = [('Text Files', '*.txt'),
                                                                 ('All Files', '*.*')],
                                                    title = 'Select file for saving',
                                                    defaultextension = '*.txt')
        #check file name
        if len(file_name) != 0:
            #open file
            self.file_var = open(file_name, 'w')
            #write to file
            for item in self.__student_list:
                item_string = '{}:{}:{}\n'.format(item.name,
                                                  item.assignment,
                                                  item.score)
                self.file_var.write(item_string)
            #close file
            self.file_var.close()
            
    def show_about(self):
        tk.messagebox.showinfo('Help',
                               'This program is designed to help input student grades for various assignments.')
        
        
if __name__ == '__main__':
    student_gui = StudentGraderGUI()