import tkinter as tk

root = tk.Tk()
root.title("Clicker")

root.geometry("400x300")


clicks = 0
plusclick = tk.IntVar(value=1)

def on_click():
    global clicks
    clicks += plusclick.get()  
    print(clicks)
    label.config(text=f"Clicks: {clicks}")  


def clickadd():
    global clicks
    if clicks >= 20: 
        clicks -= 20  
        plusclick.set(plusclick.get() + 1)  
        label.config(text=f"Clicks: {clicks}")  


buttonadd = tk.Button(root, text="On click add 2! (cost 20 clicks)", command=clickadd)
buttonadd.pack(padx=10, pady=15)


button = tk.Button(root, text="Click me!", command=on_click)
button.pack(pady=20)

label = tk.Label(root, text=f"Clicks: {clicks}", font=("Arial", 16))
label.pack(pady=10)

root.mainloop()
