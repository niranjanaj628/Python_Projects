from tkinter import * 
from tkinter import messagebox
import random
import json

# ---------------------------- SEARCH OPTION ------------------------------- #

def search():
    website= website_input.get()
    
    try:
        with open('Python_Projects/projects/Day-30/data.json', 'r') as file:
            data=json.load(file)
            
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No details found")
    
    else:
        if website in data:
            data_dict=data[website]
            messagebox.showinfo(title=website, message=f"Email: {data_dict['Email']}\nPassword: {data_dict['Password']}")
        else:
            messagebox.showinfo(title='Error', message="The website details doesn't exist")

    finally:
            website_input.delete(0, END)

    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range (random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range (random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range (random.randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password="".join(password_list)
        
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_input.get()
    email= email_input.get()
    password= password_input.get()
    
    new_data= {website: {
        "Email": email,
        "Password":password,
        }
    }
    
    if len(website) == 0 or len(email)== 0 or len(password) == 0:
        messagebox.showinfo(title='Empty field', message = 'Dont leave any fields empty!')
    
    else:
        try:
            with open('Python_Projects/projects/Day-30/data.json', 'r') as file:
                data= json.load(file)    
        except FileNotFoundError:
            with open('Python_Projects/projects/Day-30/data.json', 'w') as file:
                json.dump(new_data, file, indent = 4)
        else:
            data.update(new_data)
            
            with open('Python_Projects/projects/Day-30/data.json', 'w') as file:
                json.dump(data, file, indent=4)
                
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #

# Window
window=Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas=Canvas(width=200, height=200)
img=PhotoImage(file='Python_Projects\projects\Day-29\logo.png')
canvas.create_image(100,100, image=img)
canvas.grid(column=1, row=0)

# Labels
website_label=Label(text='Website:')
email_label=Label(text='Email/ Username:')
password_label=Label(text='Password:')

# Entry
website_input=Entry()
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()
email_input=Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, 'abc@gmail.com')
password_input=Entry()
password_input.grid(column=1, row=3, sticky="EW")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

#Buttons
search_btn= Button(text='Search', command=search)
search_btn.grid(column=2, row=1, columnspan=2, sticky="EW")

generate_password_btn= Button(text='Generate Password', command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky="EW")

add_btn= Button(text='Add', width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()