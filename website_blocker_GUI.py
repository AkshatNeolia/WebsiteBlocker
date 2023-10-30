import platform
import os
import tkinter as tk
from tkinter import messagebox

# List of websites to be blocked
blocked_websites = []

# Path to the host file based on the operating system
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux" or platform.system() == "Darwin":
    hosts_path = "/etc/hosts"
else:
    print("Unsupported operating system")
    exit()

# IP address to redirect the blocked websites to
redirect_ip = "127.0.0.1"

# Function to block websites
def block_websites():
    websites = entry.get().split()
    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites:
                if website not in content:
                    file.write(redirect_ip + " " + website + "\n")
        messagebox.showinfo("Website Blocker", "Websites blocked successfully.")
    except Exception as e:
        messagebox.showerror("Website Blocker", "An error occurred: " + str(e))

# Function to unblock websites
def unblock_websites():
    try:
        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if all(website not in line for website in blocked_websites):
                    file.write(line)
            file.truncate()
        messagebox.showinfo("Website Blocker", "Websites unblocked successfully.")
    except Exception as e:
        messagebox.showerror("Website Blocker", "An error occurred: " + str(e))

# Create GUI
root = tk.Tk()
root.title("Website Blocker")

# Entry and Label for websites input
label = tk.Label(root, text="Enter websites to block (space separated):")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Block and Unblock buttons
block_button = tk.Button(root, text="Block Websites", command=block_websites)
block_button.pack()
unblock_button = tk.Button(root, text="Unblock Websites", command=unblock_websites)
unblock_button.pack()

# Run the GUI main loop
root.mainloop()
