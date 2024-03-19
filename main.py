from tkinter import *
def button_clicked():
    result = float(input_text.get())
    result *= 1.609
    result_label.config(text=result)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)

# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=10)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=20, pady=10)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

# buttons
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

# entry component
input_text = Entry(width=10)
input_text.grid(column=1, row=0)

window.mainloop()
