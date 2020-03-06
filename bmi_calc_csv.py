
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from datetime import *
import csv


class BodyMassIndexApp(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.navFrame = Frame()
        self.mainFrame = Frame()
        self.navbuttons = []
        self.dataList = []
        self.currentIndex = 0
        self.fileName = None
        self.bmi_gui()

    def bmi_gui(self):
        Label(self.mainFrame, text='First Name:').grid(column=0, row=4, sticky='E')
        self.firstNameEntry = Entry(self.mainFrame, width=15)
        self.firstNameEntry.grid(column=1, row=4, sticky='W')

        Label(self.mainFrame, text='Enter you weight:').grid(column=1, row=0, sticky='W')
        Label(self.mainFrame, text='Enter you height:').grid(column=3, row=0, sticky='W')

        Label(self.mainFrame, text='Kilograms:').grid(column=0, row=1, sticky='E')
        self.weightInput = Entry(self.mainFrame, width=15)
        self.weightInput.grid(column=1, row=1, sticky='W')

        Label(self.mainFrame, text='or Stones:').grid(column=0, row=2, sticky='E')
        self.weightInputStones = Entry(self.mainFrame, width=15)
        self.weightInputStones.grid(column=1, row=2, sticky='W')

        Label(self.mainFrame, text='+ Pounds:').grid(column=0, row=3, sticky='E')
        self.weightInputPounds = Entry(self.mainFrame, width=15)
        self.weightInputPounds.grid(column=1, row=3, sticky='W')

        Label(self.mainFrame, text='Last Name:').grid(column=2, row=4, sticky='E')
        self.lastNameEntry = Entry(self.mainFrame, width=15)
        self.lastNameEntry.grid(column=3, row=4, sticky='W')

        Label(self.mainFrame, text='Centimetres:').grid(column=2, row=1, sticky='E')
        self.heightInput = Entry(self.mainFrame, width=15)
        self.heightInput.grid(column=3, row=1, sticky='W')

        Label(self.mainFrame, text='or Feet:').grid(column=2, row=2, sticky='E')
        self.heightInputFeet = Entry(self.mainFrame, width=15)
        self.heightInputFeet.grid(column=3, row=2, sticky='W')

        Label(self.mainFrame, text='+ Inches:').grid(column=2, row=3, sticky='E')
        self.heightInputInches = Entry(self.mainFrame, width=15)
        self.heightInputInches.grid(column=3, row=3, sticky='W')

        self.calculateButton = Button(self.mainFrame, text='Calculate BMI', width=10, command=self.calculate)
        self.calculateButton.grid(column=4, row=0, padx=10)

        self.clearButton = Button(self.mainFrame, text='Clear form', width=10, command=self.clear_entries)
        self.clearButton.grid(column=4, row=1, padx=10)

        self.addButton = Button(self.mainFrame, text='Add to file', width=10, command=self.add_to_list)
        self.addButton.grid(column=4, row=2, padx=5)

        self.deleteButton = Button(self.mainFrame, text='Delete', width=10, command=self.delete_from_list)
        self.deleteButton.grid(column=4, row=3, padx=10)

        self.save_asButton = Button(self.mainFrame, text='Save As...', width=10, command=self.save_as)
        self.save_asButton.grid(column=4, row=4, padx=10)

        self.openFileButton = Button(self.mainFrame, text='Open File...', width=10, command=self.read_from_file)
        self.openFileButton.grid(column=4, row=5, padx=10)

        self.mainFrame.pack(side=TOP)

        names = ['First entry', 'Previous', 'Next', 'Last entry']
        for item in range(0, len(names)):
            button = Button(self.navFrame, text=names[item], fg='black', width=13,
                            command=lambda i=item: self.check_nav_button(i))
            self.navbuttons.append(button)
            self.navbuttons[item].grid(row=0, column=item, padx=2, pady=4)

        self.navFrame.pack(side=BOTTOM)

    def add_to_list(self):
        # if BMI was calculated, the result will be added to the file 
        # otherwise, only data entries and time will be saved

        now = datetime.now()
        try:
            print(self.firstNameEntry.get(), self.lastNameEntry.get(),
                  self.weightInput.get(), self.heightInput.get(), self.weightInputStones.get(),
                  self.weightInputPounds.get(), self.heightInputFeet.get(),
                  self.heightInputInches.get(), self.bmi, self.category, now.strftime('%d/%m/%Y %H:%M:%S'))

            record = (self.firstNameEntry.get(), self.lastNameEntry.get(),
                      self.weightInput.get(), self.heightInput.get(), self.weightInputStones.get(),
                      self.weightInputPounds.get(), self.heightInputFeet.get(),
                      self.heightInputInches.get(), self.bmi, self.category, now.strftime('%d/%m/%Y %H:%M:%S'))

        except:
            print(self.firstNameEntry.get(), self.lastNameEntry.get(),
                  self.weightInput.get(), self.heightInput.get(), self.weightInputStones.get(),
                  self.weightInputPounds.get(), self.heightInputFeet.get(),
                  self.heightInputInches.get(), '', '', now.strftime('%d/%m/%Y %H:%M:%S'))

            record = (self.firstNameEntry.get(), self.lastNameEntry.get(),
                      self.weightInput.get(), self.heightInput.get(), self.weightInputStones.get(),
                      self.weightInputPounds.get(), self.heightInputFeet.get(),
                      self.heightInputInches.get(), '', '', now.strftime('%d/%m/%Y %H:%M:%S'))

        self.dataList.append(record)
        self.currentIndex = len(self.dataList) - 1
        print(self.dataList)
        mb.showinfo('Record Added', 'One Record Added')
        self.clear_entries()

    def delete_from_list(self):
        try:
            del self.dataList[self.currentIndex]
            self.display(self.currentIndex)

        except:
            mb.showerror('Delete error', 'Nothing to delete')

    def check_nav_button(self, value):
        try:
            if value == 0:
                self.currentIndex = 0
            elif value == 1:
                self.currentIndex -= 1
            elif value == 2:
                self.currentIndex += 1
            elif value == 3:
                self.currentIndex = len(self.dataList) - 1
            else:
                self.currentIndex = 0
            self.display(self.currentIndex)

        except:
            mb.showerror('No entries', 'No entries, please update records')

    def display(self, index):
        self.clear_entries()
        if index < 0:
            index = 0

        if index >= (len(self.dataList) - 1):
            index = (len(self.dataList) - 1)

        row = self.dataList[index]
        self.firstNameEntry.insert(0, row[0])
        self.lastNameEntry.insert(0, row[1])
        self.weightInput.insert(0, row[2])
        self.heightInput.insert(0, row[3])
        self.weightInputStones.insert(0, row[4])
        self.weightInputPounds.insert(0, row[5])
        self.heightInputFeet.insert(0, row[6])
        self.heightInputInches.insert(0, row[7])
        self.currentIndex = index

    def clear_entries(self):
        self.firstNameEntry.delete(0, END)
        self.lastNameEntry.delete(0, END)
        self.weightInput.delete(0, END)
        self.weightInputStones.delete(0, END)
        self.weightInputPounds.delete(0, END)
        self.heightInput.delete(0, END)
        self.heightInputFeet.delete(0, END)
        self.heightInputInches.delete(0, END)
        self.bmi = ''
        self.category = ''

    def save_as(self):
        self.fileName = fd.asksaveasfilename(defaultextension='.csv',
                                             filetypes=[('csv files', '.csv'), ('all files', '.*')])
        self.write_to_file()

    def write_to_file(self):
        try:
            if len(self.dataList) > 0:
                csvfile = open(file=self.fileName, mode='w', newline='\n')
                writer = csv.writer(csvfile, delimiter=',')

                for values in range(0, len(self.dataList)):
                    writer.writerow(self.dataList[values])
                csvfile.close()
            else:
                mb.showwarning("File not saved", "The file not saved")
        except FileNotFoundError:
            mb.showwarning("File not saved", "No such file or directory")

    def read_from_file(self):
        try:
            self.dataList.clear()
            self.fileName = fd.askopenfilename(defaultextension='.csv',
                                               filetypes=[('csv files', '.csv'), ('all files', '.*')])
            csvfile = open(self.fileName, 'r')
            reader = csv.reader(csvfile, delimiter=',')

            for line in reader:
                print(tuple(line))
                self.dataList.append(line)

            self.display(0)
            csvfile.close()
            self.currentIndex = 0
            print(self.dataList)
        except FileNotFoundError:
            mb.showwarning("File Not Found", "No such file or directory")

    def get_weight(self):  # metric input is a priority source for calculation
        try:
            if '0' == self.weightInput.get() or 0 >= float(self.weightInput.get()):
                stones = float(self.weightInputStones.get())
                pounds = float(self.weightInputPounds.get())
                self.weight = (stones * 14 + pounds) * 0.45359

            else:
                self.weight = float(self.weightInput.get())

        except ValueError:
            stones = float(self.weightInputStones.get())
            pounds = float(self.weightInputPounds.get())
            self.weight = (stones * 14 + pounds) * 0.45359

    def get_height(self):  # metric input is a priority source for calculation
        try:
            if '0' == self.heightInput.get() or 0 >= float(self.heightInput.get()):
                feet = float(self.heightInputFeet.get())
                inches = float(self.heightInputInches.get())
                self.height = (feet * 12 + inches) * 0.0254
            else:
                self.height = float(self.heightInput.get()) / 100

        except ValueError:
            feet = float(self.heightInputFeet.get())
            inches = float(self.heightInputInches.get())
            self.height = (feet * 12 + inches) * 0.0254

    def calculate(self):
        try:
            self.get_weight()
            self.get_height()

            self.bmi = round(self.weight / (self.height ** 2), 1)
            if self.bmi < 18.5:
                self.category = ' underweight'
            elif 18.5 <= self.bmi < 25:
                self.category = ' healthy weight'
            elif 25 <= self.bmi < 30:
                self.category = ' overweight'
            else:
                self.category = ' obesity'

            if 2 < self.weight < 650 and 0.5 < self.height < 2.7:  # based on WiKi people data
                mb.showinfo('BMI calculation result', 'BMI calculation result: '
                            + str(self.bmi) + str(self.category))

            else:  # incorrect input is not cleared to allow user to correct it
                mb.showerror('BMI input error', 'Invalid height or weight input')

        except:
            mb.showerror('BMI input error', 'Invalid height or weight input')


if __name__ == '__main__':
    root = Tk()
    root.title('Body Mass Index Calculator')
    root.geometry("428x200+800+100")
    app = BodyMassIndexApp(master=root)
    app.mainloop()