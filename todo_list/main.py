import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Mohon masukkan tugas!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Peringatan", "Tidak ada tugas yang dipilih!")

def clear_all():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Aplikasi To-Do List")

# Buat daftar tugas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Buat input untuk menambahkan tugas baru
entry = tk.Entry(root, width=40)
entry.pack()

# Buat tombol tambah tugas
add_button = tk.Button(root, text="Tambah Tugas", command=add_task)
add_button.pack(pady=5)

# Buat tombol hapus tugas
delete_button = tk.Button(root, text="Hapus Tugas", command=delete_task)
delete_button.pack(pady=5)

# Buat tombol bersihkan semua tugas
clear_button = tk.Button(root, text="Bersihkan Semua", command=clear_all)
clear_button.pack(pady=5)

root.mainloop()
