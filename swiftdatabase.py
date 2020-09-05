import sqlite3

conn = sqlite3.connect('swiftlogger.db')

c = conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS login 
            ( username TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL) ''')

c.execute(''' CREATE TABLE IF NOT EXISTS url 
            ( email_id TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL,
            url TEXT NOT NULL,
            swift_user TEXT NOT NULL)''')

class login:
    def __init__(self):
        print("")
      
    #insert new login
    def insert_login(self,username,password):
        self.username = username
        self.password = password
        c.execute("INSERT INTO login VALUES(?,?)",(self.username,self.password))
        conn.commit()

    #login into existing account
    def login_acc(self,username):
        self.username = username     
        self.acc_data = c.execute("SELECT password FROM login WHERE username = ? ",(self.username,))
        self.a = tuple(self.acc_data)
        for i in self.a:
            return(i[0])
           
class url:
    def __init__(self):
        print("")
    
    #insert new login id
    def insert_url(self,email_id,password,url,swift_user):
        self.email_id = email_id
        self.password = password
        self.url = url
        self.swift_user = swift_user
        c.execute("INSERT INTO url VALUES(?,?,?,?)",(self.email_id,self.password,self.url,self.swift_user))
        conn.commit()
    
    def delete_url(self,email_id,password):
        self.email_id = email_id
        self.password = password
        c.execute("DELETE FROM url WHERE email_id = ? AND password = ?",(self.email_id,self.password))
        conn.commit()
        return()
    
    def select_url(self,email_id,password):
        self.email_id = email_id    
        self.password = password
        self.data = c.execute("SELECT * FROM url WHERE email_id = ? AND password = ?",(self.email_id,self.password))
        for i in self.data:
            a = i
        return(a)
    

    def count_url(self,swift_user):
        self.swift = swift_user
        self.user = c.execute("SELECT email_id,password,url FROM url WHERE swift_user = ?",(self.swift,))
        self.c = tuple(self.user)
        return(self.c)