from tkinter import *
from  tkinter import messagebox
import ast

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())


    if username in r.keys() and password==r[username]:
        '''screen=Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text="Hello Everyone!",bg='#fff'
              ,font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()'''
        root.destroy()
        import homepage

    else:
        messagebox.showerror('Invalid','invalid username or password')


def signup_command():
    window=Toplevel(root)
    window.title('Sign Up')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        Username = user.get()
        Password = code.get()
        confirmPassword = confirm_code.get()

        if Password == confirmPassword:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {Username: Password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully sign up')
                window.destroy()

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'Password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both Password should match")

    def sign():
        window.destroy()

    img = PhotoImage(file='login1.png')
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        if confirm_code.get() == '':
            code.insert(0, 'Confirm Password')

    confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign Up',
           bg='#57a1f8', fg='white', border=0,
           command=signup).place(x=35, y=280)

    label = Label(frame, text="Have an account?", fg='black'
                  , bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)

    signin = Button(frame, width=6, text='Sign In', border=0,
                    bg='white', cursor='hand2', fg='#57a1f8'
                    , command=sign)
    signin.place(x=200, y=340)

    window.mainloop()


img= PhotoImage(file='login1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')


code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign In',
       bg='#57a1f8',fg='white', border=0,
       command=signin).place(x=35,y=204)

label=Label(frame,text="Don't have an account?",fg='black'
            ,bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign Up',border=0,
                bg='white',cursor='hand2',fg='#57a1f8'
                ,command=signup_command)
sign_up.place(x=215,y=270)



root.mainloop()