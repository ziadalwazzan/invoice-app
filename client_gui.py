# Standard Libs
import json
import tkinter as tk

# Other Libs
import requests
import customtkinter

class Client_GUI():

    def __init__(self) -> None:
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("800x600")

        self.frame = customtkinter.CTkFrame(master=self.root) 
        self.frame.pack(pady=60, padx=80, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Invoice System")
        self.label.pack(pady= 12, padx=10)

        self.doc_option_menu = customtkinter.CTkOptionMenu(master=self.frame, values=["Invoice"])
        self.doc_option_menu.pack(pady= 12, padx=10)
        self.doc_option_menu.set("Document Type")

        self.customer_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Customer Name")
        self.customer_name_entry.pack(pady=12, padx=10)

        self.customer_number_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Customer Number")
        self.customer_number_entry.pack(pady=12, padx=10)

        self.root.mainloop()

def main():
    data = {
        'invoice_number' : 123,
        'customer_info' : {
            'customer_name': 'Mohammed AlFlani',
            'customer_number': '+965 55555555',
            'customer_email': 'Mohammed@example.com',
            'company_name': 'Pear Inc',
            'company_address': 'Yarmouk, Block 1, St 10, House 11'
        },
        'items' : [
            {
                'item': 'Web App',
                'qty': 2,
                'unit_price': 150.750,
                'total': 301.500
            },{
                'item': 'AWS Hosting',
                'qty': 2,
                'unit_price': 75.032,
                'total': 150.064
            },{
                'item': 'Domain (6 Months)',
                'qty': 1,
                'unit_price': 10.325,
                'total': 10.325
            }
        ]
    }

    gui = Client_GUI()


    return

    url = 'http://127.0.0.1:5000/'
    html = requests.post(url, json=data)
    with open('invoice.pdf', 'wb') as f:
        f.write(html.content)

if __name__ == "__main__":
    main()