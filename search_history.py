import tkinter as tk
from tkinter import messagebox

def save_search():
    search_text = entry.get()
    if search_text:
        search_history.append(search_text)
        entry.delete(0, tk.END)  
    else:
        messagebox.showwarning("You had not entered a search term", "Enter search term")


def show_history():
    if search_history:
        history = "\n".join(search_history)
        messagebox.showinfo("Your Search History", history)
    else:
        messagebox.showinfo("No search history available.")

root = tk.Tk()
root.title("Search History Feature")

search_history = []

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

save_button = tk.Button(root, text="Save my Search", command=save_search)
save_button.pack(pady=5)

history_button = tk.Button(root, text="Show my History", command=show_history)
history_button.pack(pady=5)
root.mainloop()
