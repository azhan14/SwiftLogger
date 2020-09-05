from tkinter import *
import tkinter as tkr
from tkinter import ttk
from tkinter import messagebox
from swiftdatabase import *
from webauto import *
l = login()
u = url()
root = Tk()
root.title("SwiftLogger")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background = "#003333")
class swift_login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.login_user_entry=""
        self.login_pass_entry=""
        self.signup_user_entry=""
        self.signup_pass_entry=""
        self.signup_reenter_pass_entry=""
        self.a=0
        self.b=0
        self.swiftusername = ""
        self.var=""
        self.addaccount_pass_entry=""
        self.addaccount_user_entry=""
        self.details_acc = tuple()


    def swift_gui(self):                               #swift logger login and signup page
        self.title = Label(root,text = "SwiftLogger", width=10, font=("Times New Roman",50,"bold"),anchor='center',bg="#003333",fg="purple")
        self.title.place(x=20,y=30)
        self.layout_login = Canvas(root, width=1000, height=600,bg="#333333")
        self.layout_login.pack()
        self.a=(w/2)-500
        self.b=(h/2)-300
        self.layout_login.place(x=self.a,y=self.b)
        self.login_user_name = Label(root,text = "Username", width=10, font=("bold",30),anchor="w",bg="#333333",fg="white")
        self.large_font = ('Times New Roman',30)
        self.login_user_name.place(x=self.a+300,y=self.b+80)
        self.login_user_entry = Entry(root,width=20,font=self.large_font)
        self.login_user_entry.place(x=self.a+305,y=self.b+140)
        self.login_pass_word = Label(root ,text = "Password", width=10,font=("bold",30),anchor="w",bg="#333333",fg="white")
        self.login_pass_word.place(x=self.a+300,y=self.b+250)
        self.login_pass_entry = Entry(root,show='*',width=20,font=self.large_font)
        self.login_pass_entry.place(x=self.a+305,y=self.b+310)
        self.login_button = Button(text ="LOGIN", relief="raised", bg="#33FF00",height=3,width=25,command=start.verify_details)
        self.login_button.place(x=self.a+300,y=self.b+450)
        self.signup_button = Button(text ="SIGNUP", relief="raised", bg="#D40C00",height=3,width=25,command=start.signup)
        self.signup_button.place(x=self.a+525,y=self.b+450)

    def signup(self):
        self.back_button = Button(text ="Back",fg = "#003300", font=("bold",18),relief="raised", bg="#d40c00",height=1,width=15, command=start.swift_gui)
        self.back_button.place(x=1200,y=40)
        self.title = Label(root,text = "SwiftLogger", width=10, font=("Times New Roman",50,"bold"),anchor='center',bg="#003333",fg="purple")
        self.title.place(x=20,y=30)
        self.layout_signup = Canvas(root, width=1000, height=600,bg="#333333")
        self.layout_signup.pack()
        self.layout_signup.place(x=self.a,y=self.b)
        self.signup_user_name = Label(root ,text = "Enter Username", width=15, font=("bold",20),anchor="w",bg="#333333",fg="white")
        self.large_font = ('Times New Roman',30)
        self.signup_user_name.place(x=self.a+300,y=self.b+40)
        self.signup_user_entry = Entry(root,width=20,font=self.large_font)
        self.signup_user_entry.place(x=self.a+305,y=self.b+100)
        self.signup_pass_word = Label(root ,text = "Enter Password", width=15,font=("bold",20),anchor="w",bg="#333333",fg="white")
        self.signup_pass_word.place(x=self.a+300,y=self.b+200)
        self.signup_pass_entry = Entry(root,show='*',width=20,font=self.large_font)
        self.signup_pass_entry.place(x=self.a+305,y=self.b+260)
        self.signup_reenter_pass_word = Label(root,text = "Re-enter Password", width=15,font=("bold",20),anchor="w",bg="#333333",fg="white")
        self.signup_reenter_pass_word.place(x=self.a+300,y=self.b+360)
        self.signup_reenter_pass_entry = Entry(root,show='*',width=20,font=self.large_font)
        self.signup_reenter_pass_entry.place(x=self.a+305,y=self.b+420)
        self.create_button = Button(text ="Create Account", relief="raised", bg="#D40C00",height=3,width=57,command=start.add_details_db)
        self.create_button.place(x=self.a+305,y=self.b+510)

    def add_details_db(self):
        self.pass1 = self.signup_pass_entry.get()
        self.pass2 = self.signup_reenter_pass_entry.get()
        self.user = self.signup_user_entry.get()
        if self.user == "":
            messagebox.showwarning("warning","username cannot be empty")
        if self.pass1 == "":
            messagebox.showwarning("warning","password cannot be empty")
        if self.pass2 == "":
            messagebox.showwarning("warning","re-enter password cannot be empty")
        if self.pass1 == self.pass2:
            l.insert_login(self.user,self.pass1)
            start.swift_gui()
        else:
            messagebox.showwarning("warning","password did not match")  
            start.signup()
    
    def verify_details(self):
        self.user = self.login_user_entry.get()
        self.pass1 = self.login_pass_entry.get()
        self.detail = l.login_acc(self.user)
        if self.detail == self.pass1:
            self.swiftusername = self.user
            start.select()
        else:
            messagebox.showwarning("Warning","incorrect login details")
            start.swift_gui()

    def select(self):
        self.logout_button = Button(text ="Log Out",fg = "#003300", font=("bold",18),relief="raised", bg="#d40c00",height=1,width=15, command=start.swift_gui)
        self.logout_button.place(x=1200,y=40)
        self.title = Label(root,text = "SwiftLogger", width=10, font=("Times New Roman",50,"bold"),anchor='center',bg="#003333",fg="purple")
        self.title.place(x=20,y=30)
        self.layout_select = Canvas(root, width=1000, height=600,bg="#333333")
        self.layout_select.pack()
        self.layout_select.place(x=self.a,y=self.b)
        self.add_button = Button(text ="Add Account",fg = "#003300", font=("bold",30),relief="raised", bg="#ffcc99",height=3,width=28,command=start.add_account)
        self.add_button.place(x=self.a+180,y=self.b+80)
        self.add_button = Button(text ="Login to Added Account",fg = "#003300", font=("bold",30),relief="raised", bg="#ffcc99",height=3,width=28,command=start.display_acc)
        self.add_button.place(x=self.a+180,y=self.b+340)

    def add_account(self):
        self.title = Label(root,text = "SwiftLogger", width=10, font=("Times New Roman",50,"bold"),anchor='center',bg="#003333",fg="purple")
        self.title.place(x=20,y=30)
        self.layout_addaccount = Canvas(root, width=1000, height=600,bg="#333333")
        self.layout_addaccount.pack()
        self.layout_addaccount.place(x=self.a,y=self.b)
        self.large_font = ('Times New Roman',30)
        self.back_button = Button(text ="Back",fg = "#003300", font=("bold",18),relief="raised", bg="#d40c00",height=1,width=15, command=start.select)
        self.back_button.place(x=1000,y=160)
        self.addaccount_url = Label(root ,text = "Select url type", width=15,font=("bold",20),anchor="w",bg="#333333",fg="white")
        self.addaccount_url.place(x=self.a+300,y=self.b+40)
        self.var=tkr.StringVar()
        self.set1 = OptionMenu(root,self.var,"Google","Yahoo","StudyLeague","Pmart","Instagram","GDrive","Facebook","LinkedIn")
        self.var.set("Google")
        self.set1.configure(font=("Arial",25),width=20,bg="#99ccff")
        self.set1.place(x=self.a+300,y=self.b+100)
        self.addaccount_user_name = Label(root ,text = "Enter email id", width=15,font=("bold",20),anchor="w",bg="#333333",fg="white")
        self.addaccount_user_name.place(x=self.a+300,y=self.b+170)
        self.addaccount_user_entry = Entry(root,width=20,font=self.large_font)
        self.addaccount_user_entry.place(x=self.a+305,y=self.b+230)
        self.addaccount_pass_word = Label(root ,text = "Enter Password", width=15,font=("bold",20),anchor="w",bg="#333333",fg="white")
        self.addaccount_pass_word.place(x=self.a+300,y=self.b+330)
        self.addaccount_pass_entry = Entry(root,show='*',width=20,font=self.large_font)
        self.addaccount_pass_entry.place(x=self.a+305,y=self.b+390)
        self.add_button = Button(text ="Add",fg = "#003300", font=("bold",30),relief="raised", bg="#ffcc99",height=1,width=10,command = start.add_to_db)
        self.add_button.place(x=self.a+380,y=self.b+480)

    def add_to_db(self):
        self.url=self.var.get()
        self.user=self.addaccount_user_entry.get()
        self.pass1=self.addaccount_pass_entry.get()
        if self.user != "" and self.pass1 != "":
            u.insert_url(self.user,self.pass1,self.url,self.swiftusername)
            start.select()
        else:
            messagebox.showwarning("warning","username or password column cannot be empty")
            start.add_account()


    def display_acc(self):
        self.details_acc = u.count_url(self.swiftusername)
        self.count = len(self.details_acc)
        self.title = Label(root,text = "SwiftLogger", width=10, font=("Times New Roman",50,"bold"),anchor='center',bg="#003333",fg="purple")
        self.title.place(x=20,y=30)
        self.layout_display = Canvas(root, width=1000, height=600,bg="#333333")
        self.layout_display.pack()
        self.layout_display.place(x=self.a,y=self.b)
        self.yinc = 0
        for i in range(self.count):
            self.display_url = Label(root ,text = self.details_acc[i][2] , width=15,font=("Comic sans ms",20),anchor="w",bg="#333333",fg="cyan")
            self.display_url.place(x=self.a+90,y=self.b+self.yinc+40)
            self.display_username = Label(root ,text = self.details_acc[i][0] , width=15,font=("Comic sans ms",20),anchor="w",bg="#333333",fg="cyan")
            self.display_username.place(x=self.a+250,y=self.b+self.yinc+40)
            self.login_button = Button(text ="Login",fg = "#003300", font=("bold",14),relief="raised", bg="#99ff33",height=1,width=15,command=lambda x=i : start.login_url(self.details_acc[x][0],self.details_acc[x][1],self.details_acc[x][2]))
            self.login_button.place(x=self.a+550,y=self.b+self.yinc+40)
            self.delete_button = Button(text ="Delete",fg = "#003300", font=("bold",14),relief="raised", bg="#d40c00",height=1,width=15, command=lambda x=i : start.delete_url(self.details_acc[x][0],self.details_acc[x][1],self.details_acc[x][2]))
            self.delete_button.place(x=self.a+775,y=self.b+self.yinc+40)
            self.yinc += 50
    
    def login_url(self,e,p,u):
        self.e = e
        self.p = p
        self.u = u
        if self.u == "Google":
            google(self.e,self.p)
        elif self.u == "Yahoo":
            yahoo(self.e,self.p)
        elif self.u == "StudyLeague":
            studyL(self.e,self.p)
        elif self.u == "Pmart":
            pmart(self.e,slef.p)
        elif self.u == "Instagram":
            instagram(self.e,self.p)
        elif self.u == "GDrive":
            gdrive(self.e,self.p)
        elif self.u == "Facebook":
            facebook(self.e,self.p)
        elif self.u == "LinkedIn":
            linkedin(self.e,self.p)
        start.display_acc()
    
    def delete_url(self,e,p,user):
        self.e = e
        self.p = p
        self.u = user
        u.delete_url(self.e,self.p)
        start.display_acc()
    

        
start = swift_login(root)
start.swift_gui()
root.mainloop()