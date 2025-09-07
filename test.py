import tkinter as tk

root = tk.Tk()
root.title("Учебный тест")
root.geometry("300x100")

label = tk.Label(root, text="Программа в разработке", font=("Times New Roman", 14))
label.pack(expand=True)

root.mainloop()
