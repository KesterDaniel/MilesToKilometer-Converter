from tkinter import *

FONT = ("Arial", 10, "bold")

window = Tk()
window.minsize(width=400, height=150)
window.title("Miles to Kilometer Converter")
window.config(padx=200, pady=75)


def mile_converter():
    mile_to_convert = float(user_input.get())
    to_km = round(int(mile_to_convert) * 1.609, 2)
    result_value.config(text=to_km)


def kg_converter():
    kg_to_convert = float(user_input.get())
    to_lbs = round(int(kg_to_convert) * 2.2046, 2)
    result_value.config(text=to_lbs)


def calculate():
    radio_choice = radio_state.get()
    if radio_choice == "miles_to_km":
        mile_converter()
    else:
        kg_converter()


def views_config():
    convert_choice = radio_state.get()
    if convert_choice == "miles_to_km":
        input_label.config(text="Miles")
        result_label2.config(text="Km")
    else:
        input_label.config(text="Kg")
        result_label2.config(text="lbs")


radio_state = StringVar(value="miles_to_km")
radio_btn1 = Radiobutton(text="Miles to KM", value="miles_to_km", variable=radio_state, command=views_config)
radio_btn2 = Radiobutton(text="Kg to lbs", value="kg_to_lbs", variable=radio_state, command=views_config)
radio_btn1.grid(row=0, column=1)
radio_btn2.grid(row=0, column=2)

user_input = Entry(width=10)
user_input.insert(END, string=0)
user_input.grid(row=1, column=1)

input_label = Label(text="Miles", font=FONT)
input_label.grid(row=1, column=2)

result_label1 = Label(text="is equal to", font=FONT)
result_label1.grid(row=2, column=0)

result_value = Label(text=0, font=FONT)
result_value.grid(row=2, column=1)

result_label2 = Label(text="Km", font=FONT)
result_label2.grid(row=2, column=2)

calc_btn = Button(text="Calculate", font=FONT, command=calculate)
calc_btn.grid(row=3, column=1)

window.mainloop()
