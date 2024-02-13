import email
from os import name
import tkinter as tk

def submit_form():
  print("Name: ", name.get())
  print("Email: ", email.get())
  print("Contact: ", contact_label.get())

root = tk.Tk()
root.title("Registration Form")
root.configure(bg="white")

name_label = tk.Label(root, text="Name:", fg="black")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:", fg="black")
email_entry = tk.Entry(root)

contact_label = tk.Label(root, text="Contact:", fg="black")
contact_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit_form)

name_label.pack()
name_entry.pack()
email_label.pack()
email_entry.pack()
contact_label.pack()
contact_entry.pack()
submit_button.pack()

root.mainloop()
import email
from os import name
import tkinter as tk

def submit_form():
  print("Name: ", name.get())
  print("Email: ", email.get())
  print("Contact: ", contact_label.get())

root = tk.Tk()
root.title("Registration Form")
root.configure(bg="white")

name_label = tk.Label(root, text="Name:", fg="black")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:", fg="black")
email_entry = tk.Entry(root)

contact_label = tk.Label(root, text="Contact:", fg="black")
contact_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit_form)

name_label.pack()
name_entry.pack()
email_label.pack()
email_entry.pack()
contact_label.pack()
contact_entry.pack()
submit_button.pack()

root.mainloop()