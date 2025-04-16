import tkinter
from tkinter import * 
from userDatabaseManager import *
from encryptionManager import *
from userActionManager import * 

def loginWindow():
    Login=Toplevel(root)
    Login.title("Login")
    Login.geometry("500x500")

    existingUsernameInput = StringVar()
    existingPasswordInput = StringVar()

    titleLabel = Label(Login, text = "Welcome back!", width=30)
    titleLabel.place(x=70, y=60)

    usernameLabel = Label(Login, text = "Enter username", width=30)
    usernameLabel.place(x=70, y=100)
    usernameEntry = Entry(Login, textvariable=existingUsernameInput)
    usernameEntry.place(x=110, y=130)

    usernameLabel = Label(Login, text = "Enter password", width=30)
    usernameLabel.place(x=70, y=160)
    usernameEntry = Entry(Login, textvariable=existingPasswordInput)
    usernameEntry.place(x=110, y=190)

    Button(Login, text="Login", width=20, bg="grey", fg="white", command=loginExistingUser(existingUsernameInput, existingPasswordInput)).place(x=120, y=240)


root = Tk()
root.geometry("500x500")
root.title("RegistrationWindow")

newUsernameInput = StringVar()
newPasswordInput = StringVar()

titleLabel = Label(root, text = "Welcome new user!", width=30)
titleLabel.place(x=100, y=60)

usernameLabel = Label(root, text = "Enter new username", width=30)
usernameLabel.place(x=80, y=100)
usernameEntry = Entry(root, textvariable=newUsernameInput)
usernameEntry.place(x=110, y=130)

usernameLabel = Label(root, text = "Enter new password", width=30)
usernameLabel.place(x=80, y=160)
usernameEntry = Entry(root, textvariable=newPasswordInput)
usernameEntry.place(x=110, y=190)

Button(root, text="Register", width=20, bg="grey", fg="white", command=addNewUser(newUsernameInput, newPasswordInput)).place(x=120, y=240)
Button(root, text="I already have an account.", width=20, bg="grey", fg="white", command=loginWindow).place(x=120, y=290)

root.mainloop()


