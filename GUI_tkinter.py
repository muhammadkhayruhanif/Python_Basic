# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

# variabel
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
# fungsi
def tombol_sapa():
    pesan = f"Halo! {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Hi Kamu!", message=pesan)

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

## komponen-komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, fill="x", expand=True)
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)
# 5. tombol
input_button = ttk.Button(input_frame, text="Sapa!", command=tombol_sapa)
input_button.pack(padx=10, pady=10, fill="x", expand=True)

# main loop window
window.mainloop()