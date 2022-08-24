import tkinter as tk

root = tk.Tk()
root.title("hello")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack()

b1 = tk.Button(frame, text="Select", width=25).grid(row=1,column=0)

b2 = tk.Button(frame, text="Update", width=25).grid(row=1,column=1)

b3 = tk.Button(frame, text="Delete", width=25).grid(row=1,column=2)


root.mainloop()
