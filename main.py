import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
from PIL import Image, ImageTk

def get_currency_codes():
    cr = CurrencyRates()
    currencies = cr.get_rates('USD')  # Fetch rates for a base currency (e.g., USD)
    return sorted(list(currencies.keys()))

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = dropdown_from.get()
        to_currency = dropdown_to.get()

        currency_rate = CurrencyRates().get_rate(from_currency, to_currency)
        converted_amount = amount * currency_rate

        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"{converted_amount:.2f} {to_currency}")
        result_text.config(state='disabled')

    except ValueError:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid input")
        result_text.config(state='disabled')

def swap_currencies():
    from_curr = dropdown_from.get()
    to_curr = dropdown_to.get()

    dropdown_from.set(to_curr)
    dropdown_to.set(from_curr)

root = tk.Tk()
root.title("Currency Converter")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_amount = ttk.Label(main_frame, text="Enter amount:")
label_amount.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

entry_amount = ttk.Entry(main_frame)
entry_amount.grid(column=1, row=0, padx=5, pady=5)

label_from = ttk.Label(main_frame, text="Convert From:")
label_from.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

all_currencies = get_currency_codes()

dropdown_from = ttk.Combobox(main_frame, values=all_currencies, state="readonly")
dropdown_from.current(0)
dropdown_from.grid(column=1, row=1, padx=5, pady=5)

swap_icon = Image.open("swapicon.png")  # Replace with swap icon file
swap_icon = swap_icon.resize((20, 20), Image.BICUBIC)
swap_img = ImageTk.PhotoImage(swap_icon)

swap_button = ttk.Button(main_frame, image=swap_img, command=swap_currencies)
swap_button.grid(column=1, row=2, padx=5, pady=2, sticky=tk.W)

label_to = ttk.Label(main_frame, text="Convert To:")
label_to.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)

dropdown_to = ttk.Combobox(main_frame, values=all_currencies, state="readonly")
dropdown_to.current(1)
dropdown_to.grid(column=1, row=3, padx=5, pady=5)

result_label = ttk.Label(main_frame, text="Converted Amount:")
result_label.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)

result_text = tk.Text(main_frame, height=1, width=20, state='disabled')
result_text.grid(column=1, row=4, padx=5, pady=5)

submit_button = ttk.Button(main_frame, text="Convert", command=convert_currency)
submit_button.grid(column=1, row=5, padx=5, pady=15, sticky=tk.E)

root.mainloop()
