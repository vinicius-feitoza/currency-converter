import tkinter as tk

import currency_converter.currency_converter
from currency_converter import CurrencyConverter
from tkinter import ttk
from tkinter import Button
from tkinter import PhotoImage

# Window setup

root = tk.Tk()
root.iconbitmap("coin_icon.ico")
root.title("Currency converter")
root.geometry("1000x410")
root.resizable(False, False)

# Label list

title = tk.Label(root, text="Currency exchange rate converter", font=('Arial', 32))
sub_title = tk.Label(root, text="Enter the amount and currency below", font=('Helvetica bold', 18))
amount_text = tk.Label(root, text="Amount", font=('Arial', 16))
from_text = tk.Label(root, text="From", font=('Arial', 16))
to_text = tk.Label(root, text="To", font=('Arial', 16))

# Entry / Combobox list
amount_box = ttk.Entry(root, font=('Arial', 16))
from_menu = ttk.Combobox(root, font=('Arial', 16,))
to_menu = ttk.Combobox(root, font=('Arial', 16))

# Combobox setup
c = CurrencyConverter()
menu_list = []

for item in c.currencies:
    menu_list.append(item)
menu_list.sort()

from_menu['values'] = menu_list
to_menu['values'] = menu_list


# Conversion

def convert():
    amount = amount_box.get()
    currency1 = from_menu.get().upper()
    currency2 = to_menu.get().upper()

    try:

        result = c.convert(amount, currency1, currency2)
        result = round(result, 5)

        unit_value = result / float(amount)
        unit_value = round(unit_value, 5)

        result_label = tk.Label(root, text=amount + " " + currency1 + " = " + str(result) + " " + currency2, anchor='w',
                                font=('Arial', 18)).place(x=35, y=300, width=400)
        result_label = tk.Label(root, text="1 " + currency1 + " = " + str(unit_value) + " " + currency2, anchor='w',
                                font=('Arial', 12)).place(x=35, y=360)
    except ValueError as e:
        if str(e).startswith("could not convert"):
            error_label = tk.Label(root, text="Amount field must be filled with a number", anchor='w',
                                   font=('Arial', 16)).place(x=35, y=300, width=400)
        if str(e).endswith("supported currency"):
            if currency1 == '' or currency2 == '':
                error_label = tk.Label(root, text="Both currency fields must be filled", anchor='w',
                                       font=('Arial', 18)).place(x=35, y=300, width=400)
            else:
                error_label = tk.Label(root, text=str(e), anchor='w', font=('Arial', 18)).place(x=35, y=300, width=400)
    except currency_converter.currency_converter.RateNotFoundError:
        error_label = tk.Label(root, text="This pair is not currently available", anchor='w',
                               font=('Arial', 16)).place(x=35, y=300, width=400)


convert_image = PhotoImage(file="convert_image.png")
convert_button = Button(root, image=convert_image, text="Convert", command=convert, highlightthickness=0, bd=0)


# Swap currency


def swap():
    currency1 = from_menu.get().upper()
    currency2 = to_menu.get().upper()

    to_menu.set(currency1)
    from_menu.set(currency2)


swap_image = PhotoImage(file="swap_image.png")
swap_button = Button(root, image=swap_image, text="Swap", command=swap, width=36, height=36, highlightthickness=0, bd=0)

# Placing stuff

title.place(x=160, y=10)
sub_title.place(x=280, y=70)

amount_text.place(x=35, y=160)
from_text.place(x=340, y=160)
to_text.place(x=700, y=160)

amount_box.place(x=35, y=190, height=40)
from_menu.place(x=340, y=190, height=40)
to_menu.place(x=700, y=190, height=40)

convert_button.place(x=700, y=290)
swap_button.place(x=632, y=192)

root.mainloop()
