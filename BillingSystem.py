import tkinter as tk
from tkinter import ttk





window = tk.Tk()
window.title('Billing Systemm')
window.geometry("900x500")



heading = tk.Label(window, text='Billing System', font=('Arial',20), fg='white', bg='black')
heading.pack(pady=20)

item_details = tk.Frame(window)
item_details.pack()

for col in range(4):
    item_details.columnconfigure(col, minsize=200)


item_label = tk.Label(item_details, text='Item Name', font=('Arial',15))
item_label.grid(row=0,column=0)
Quantity_label = tk.Label(item_details, text='Quantity', font=('Arial',15))
Quantity_label.grid(row=0,column=1)
Price_label = tk.Label(item_details, text='Price', font=('Arial',15))
Price_label.grid(row=0,column=2)
Total_label = tk.Label(item_details, text='Total', font=('Arial',15))
Total_label.grid(row=0,column=3)


item_text = tk.Entry(item_details, font=('Arial',15), width=15)
item_text.grid(row=1,column=0)
Quantity_text = tk.Entry(item_details, font=('Arial',15), width=15, justify="right")
Quantity_text.grid(row=1,column=1)
Price_text = tk.Entry(item_details, font=('Arial',15), width=15, justify='right')
Price_text.grid(row=1,column=2)
Total_text = tk.Entry(item_details, font=('Arial',15), width=15, justify='right')
Total_text.grid(row=1,column=3)


calc_button = tk.Button(item_details, text='Calculate', font=('Arial',15), bg='blue',fg='white')
calc_button.grid(row=2, column=2, padx=10, pady=10)
add_button = tk.Button(item_details, text='Add to Total', font=('Arial',15), bg='blue',fg='white')
add_button.grid(row=2, column=3, padx=10, pady=10)

table = ttk.Treeview(item_details, columns=('item', 'qty', 'price', 'total'), show='headings')
table.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
table.heading("#1", text='Items Name')
table.heading("#2", text='Quantity')
table.heading("#3", text='Price')
table.heading("#4", text='Total')

g_total = tk.Label(window, text='Grand Total', font=('Arial',18), fg='green')
g_total.pack(pady=5)

window.mainloop()