import tkinter as tk
import time
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_pass.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_let = ([random.choice(letters) for _ in range(nr_letters)])
    pass_symb = ([random.choice(symbols) for _ in range(nr_symbols)])
    pass_numb = ([random.choice(numbers) for _ in range(nr_numbers)])

    password_list += pass_let + pass_symb + pass_numb

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char

    entry_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_pass.get()
    if len(website) <= 0 or len(email) <= 0 or len(password) <= 0:
        messagebox.showerror("Error", "Please enter all fields")
    else:
        confirm = messagebox.askyesnocancel(title="website", message=f"This are your credentials:\n"
                                                                     f"Email: {email}\n"
                                                                     f"Password: {password}\n"
                                                                     f"\n"
                                                                     f"Are you sure you want to save it?")
        if confirm == True:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, tk.END)
                entry_pass.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid credentials.")



# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)



label_website = tk.Label(text='Website')
label_website.grid(column=0, row=1)
label_website.focus()
entry_website = tk.Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)

label_pass = tk.Label(text='Password')
entry_pass = tk.Entry(width=21)
label_pass.grid(column=0, row=3)
entry_pass.grid(column=1, row=3)


label_email = tk.Label(text='Email/Username')
label_email.grid(column=0, row=2)
entry_email = tk.Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "dato2006213@gmail.com")

generate_password_btn = tk.Button(text='Generate Password', command=generate_password, width=10, height=1)
generate_password_btn.grid(column=2, row=3, )

add_button = tk.Button(text='Add', command=save_password, width=5, height=1)
add_button.grid(column=1, row=4)







window.mainloop()
