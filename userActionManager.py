from encryptionManager import * 
from userDatabaseManager import * 

def loginExistingUser(existingUsernameInput, existingPasswordInput):
        existingUserUsername = existingUsernameInput.get()
        existingUserPassword = existingPasswordInput.get() 

        print("Raw username and password: ")
        print("Username: " + existingUserUsername)
        print("Password: " + existingUserPassword)

        hashedExistingUserPassword = hashPassword(existingUserPassword).hex()
        print("Hashed password: ", hashedExistingUserPassword)

        checkPassword(existingUserUsername, hashedExistingUserPassword)


def addNewUser(newUsernameInput, newPasswordInput): 
    newUserUsername = newUsernameInput.get()
    newUserPassword = newPasswordInput.get()

    print("Raw username and password: ")
    print("Username: " + newUserUsername)
    print("Password: " + newUserPassword)

    hashedNewUserPassword = hashPassword(newUserPassword).hex()
    print("Hashed password: ", hashedNewUserPassword )

    addUser(newUserUsername, hashedNewUserPassword)

#No tests as using the UI provides the same functionality 