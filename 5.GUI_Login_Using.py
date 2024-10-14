from tkinter import *  # Importing all classes and functions from tkinter
from tkinter import messagebox  # Importing messagebox for pop-up messages

# Function to handle the login process
def login():
    username = entry1.get()  # Get the value from the username entry field
    password = entry2.get()  # Get the value from the password entry field

    # Check if either the username or password fields are blank
    if username == "" or password == "":
        messagebox.showinfo("Login Error", "Username and Password cannot be blank.")
    # Simple authentication logic (to be replaced with secure authentication)
    elif username == "Tamim" and password == "admin":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showinfo("Login Error", "Invalid Username or Password.")

# Create the main window
root = Tk()  # Create a new Tkinter window
root.title("Login")  # Set the title of the window
root.geometry("300x200")  # Set the size of the window to 300x200 pixels

# Username label and entry field
label_username = Label(root, text="Username")  # Create a label for "Username"
label_username.grid(row=0, column=0, sticky=W)  # Position it in the first row, first column

entry1 = Entry(root, bd=5)  # Create an entry field for username input
entry1.grid(row=0, column=1, padx=10)  # Place it in the first row, second column

# Password label and entry field
label_password = Label(root, text="Password")  # Create a label for "Password"
label_password.grid(row=1, column=0, sticky=W)  # Position it in the second row, first column

entry2 = Entry(root, bd=5, show='*')  # Create an entry field for password input, hide characters with '*'
entry2.grid(row=1, column=1, padx=10)  # Place it in the second row, second column

# Login button
login_button = Button(root, text="Login", command=login, height=3, width=13, bd=6)  # Create a login button
login_button.grid(row=2, columnspan=2)  # Position it in the third row, spanning both columns

# Run the Tkinter event loop
root.mainloop()  # This keeps the window open and waits for user interaction
