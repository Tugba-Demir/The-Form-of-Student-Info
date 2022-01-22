from tkinter import *
from tkinter import messagebox

class ögrenciForm():
    def __init__(self):
        window = Tk()
        window.title("THE FORM OF STUDENT INFO")
        window.geometry("500x750")
        window.minsize(500,790)
        window.maxsize(500,790)

        # frame-1  Name-Surname Info
        self._frame1 = Frame(window, bg="light green", width=400, height=150)
        self._frame1.pack(side=TOP)
        lblNameSurnameInfo = Label(self._frame1, text="NAME-SURNAME INFO", bg="light green", font="Times 10 bold").place(x=180, y=5)
        lblName = Label(self._frame1, text="Name:", bg="light green").place(x=80, y=40)
        lblSurname = Label(self._frame1, text="Surname:", bg="light green").place(x=80, y=65)
        lblEducation = Label(self._frame1, text="Education Status:", bg="light green").place(x=80, y=90)

        self._nameVar = StringVar()
        self._nameEntry = Entry(self._frame1, textvariable=self._nameVar) 
        self._nameEntry.place(x=190, y=40)

        self._surnameVar = StringVar()
        self._surnameEntry = Entry(self._frame1, textvariable=self._surnameVar)
        self._surnameEntry.place(x=190,y=65)

        self._educationVar = StringVar()
        self._educationEntry = Entry(self._frame1, textvariable=self._educationVar)
        self._educationEntry.place(x=190, y=90)


        # frame-2 Contact İnformations

        self._frame2 = Frame(window, bg="light blue", width=400, height=370)
        self._frame2.pack(side=TOP)
        lblContactInfo = Label(self._frame2, text="COMMUNICATION INFO", bg="light blue", font="Times 10 bold").place(x=170, y=5)

        lblTelNum = Label(self._frame2, text="Telephone Number:", bg="light blue").place(x=80, y=40)
        lblSecondTelNum = Label(self._frame2, text="Second Tel. Num:", bg="light blue").place(x=80, y=65)
        lblEmail = Label(self._frame2, text="Email:", bg="light blue").place(x=80, y=90)

        self._telNum = StringVar()
        self._telNumEntry = Entry(self._frame2, textvariable = self._telNum)
        self._telNumEntry.place(x=190, y=40)

        self._secondTelNum = StringVar()
        self._secondTelNumEntry = Entry(self._frame2, textvariable = self._secondTelNum)
        self._secondTelNumEntry.place(x=190, y=65)

        self._email = StringVar()
        self._emailEntry = Entry(self._frame2, textvariable = self._email)
        self._emailEntry.place(x=190, y=90)

        # These are contact informations to be entered according to you
        
        self._rbSecondEmailVariable = StringVar()
        self._rbSecondEmailVariable.set(" ")
        rbSecondEmail = Radiobutton(self._frame2, text="I want to enter the second email:", bg="light blue", variable=self._rbSecondEmailVariable, value='1',command=self.communicationInformations)
        rbSecondEmail.place(x=80, y=125)

        self._rbLinkedInVariable = StringVar()
        self._rbLinkedInVariable.set(" ")
        rbLinkedIn = Radiobutton(self._frame2, text = "I want to enter the LinkedIn account:", bg="light blue", variable=self._rbLinkedInVariable, value='2', command = self.communicationInformations)
        rbLinkedIn.place(x=80, y=175)

        self._rbGithubVariable = StringVar()
        self._rbGithubVariable.set(" ")
        rbGithub = Radiobutton(self._frame2, text="I want to enter the GitHub account:", bg="light blue", variable=self._rbGithubVariable, value='3', command=self.communicationInformations)
        rbGithub.place(x=80, y=225)

        self._rbYetenekKapısıVariable = StringVar()
        self._rbYetenekKapısıVariable.set(" ")
        rbYetenekKapısı = Radiobutton(self._frame2, text="I want to enter the Yetenek Kapısı account:", bg="light blue", variable=self._rbYetenekKapısıVariable, value='4', command=self.communicationInformations)
        rbYetenekKapısı.place(x=80,y=275)


        # frame-3 pertaining to abilities

        self._frame3 = Frame(window, width=400,height=250, bg="light pink")
        self._frame3.pack(side=TOP)
        lblAbilities = Label(self._frame3, text="ABILITIES", bg="light pink", font="Times 10 bold").place(x=170, y=5)
      
        lblToInform = Label(self._frame3, text="Please enter the your abilities to box below:", bg="light pink").place(x=45, y=25)

        
        self._abilitiesText = Text(self._frame3, width=40, height=7, wrap=WORD)
        self._abilitiesText.place(x=45, y=55)

        btnRegister = Button(self._frame3, text="REGISTER", font="Times 10 bold", command = self.record)
        btnRegister.place(x=160,y=190)
    
        window.mainloop()

    def communicationInformations(self):

        self._var1 = StringVar()
        self._var2 = StringVar()
        self._var3 = StringVar()
        self._var4 = StringVar()

        if self._rbSecondEmailVariable.get()=='1':
            self._secondEmailEntry = Entry(self._frame2, textvariable=self._var1).place(x=100,y=150)
        if self._rbLinkedInVariable.get()=='2':
            self._linkedInEntry = Entry(self._frame2, textvariable=self._var2).place(x=100, y=200) 
        if self._rbGithubVariable.get()=='3':
            self._githubEntry = Entry(self._frame2, textvariable=self._var3).place(x=100, y=250)
        if self._rbYetenekKapısıVariable.get()=='4':
            self._yetenekKapısıEntry = Entry(self._frame2, textvariable=self._var4).place(x=100, y=300)

        
    def record(self):

        if self._nameVar.get()=="" or self._surnameVar.get()=="" or self._educationVar.get()=="" or self._telNum.get()=="" or self._secondTelNum.get()==""  or self._email.get() ==  "":
            messagebox.showinfo("Warning", "Please enter your name, surname, education status, telephone number, second telephone number and email!")
        else:
            with open("studentRegistration.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"Name: {self._nameVar.get()}\n")
                dosya.write(f"Surname: {self._surnameVar.get()}\n")
                dosya.write(f"Education Status: {self._educationVar.get()}\n")
                dosya.write(f"Telephone Number: {self._telNum.get()}\n")
                dosya.write(f"2. Telephone Number: {self._secondTelNum.get()}\n")
                dosya.write(f"Email: {self._email.get()}\n")
                dosya.write(f"2. Email: {self._var1.get()}\n")
                dosya.write(f"LinkedIn Account: {self._var2.get()}\n")
                dosya.write(f"GitHub Account: {self._var3.get()}\n")
                dosya.write(f"Yetenek Kapısı Account: {self._var4.get()}\n\n")
            

            messagebox.showinfo("To Inform", "Your registration has been created.")

            # to clear inside the entry

            self._nameEntry.delete(0, 'end')
            self._surnameEntry.delete(0, 'end')
            self._educationEntry.delete(0, 'end')
            self._telNumEntry.delete(0, 'end')
            self._secondTelNumEntry.delete(0, 'end')
            self._emailEntry.delete(0,'end')
            self._var1.set("")
            self._var2.set("")
            self._var3.set("")
            self._var4.set("")

            # for radiobuttons
            self._rbSecondEmailVariable.set(" ")
            self._rbLinkedInVariable.set(" ")
            self._rbGithubVariable.set(" ")
            self._rbYetenekKapısıVariable.set(" ")

        
ögrenciForm()