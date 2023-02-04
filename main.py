from tkinter import *
FONT = ("Arial", 10, "bold")

window = Tk()
window.minsize(width=400, height=150)
window.title("Miles to Kilometer Converter")
window.config(padx=200, pady=75)

miles_input = Entry(width=10)
miles_input.insert(END, string=0)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

km_label1 = Label(text="is equal to", font=FONT)
km_label1.grid(row=1, column=0)

km_value = Label(text=0, font=FONT)
km_value.grid(row=1, column=1)

km_label2 = Label(text="Km", font=FONT)
km_label2.grid(row=1, column=2)

calc_btn = Button(text="Calculate", font=FONT)
calc_btn.grid(row=2, column=1)


window.mainloop()