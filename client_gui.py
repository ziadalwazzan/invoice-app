# Standard Libs
import json
import os
import tkinter as tk
from PIL import Image

# Other Libs
import requests
import customtkinter
"""
class Client_GUI(customtkinter.CTk):

    def __init__(self) -> None:
        super().__init__()
        
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Invoice System")
        self.geometry("800x600")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "forged_rect.jpeg")), size=(250,100))
        self.invoice_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "invoice_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "invoice_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Logo
        self.logo_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image , font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # invoice navigation view button
        self.invoice_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Invoice",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.invoice_image, anchor="w", command=self.invoice_button_event)
        self.invoice_button.grid(row=1, column=0, sticky="ew")

        # create customer info frame
        self.customer_info_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.customer_info_frame.grid_rowconfigure(3, weight=1)
        self.customer_info_frame.grid_columnconfigure(1, weight=1)

        self.invoice_label = customtkinter.CTkLabel(self.customer_info_frame, text="Customer Information")
        self.invoice_label.grid(row=0, column=1, sticky="N" , pady=(0, 20))

        # Create Invoice Entries
        self.customer_name_entry = customtkinter.CTkEntry(master=self.customer_info_frame, placeholder_text="Customer Name")
        self.customer_name_entry.grid(row=1, column=0, pady=(0, 10))
        self.customer_number_entry = customtkinter.CTkEntry(master=self.customer_info_frame, placeholder_text="Customer Number")
        self.customer_number_entry.grid(row=2, column=0, pady=(0, 10))
        self.customer_email_entry = customtkinter.CTkEntry(master=self.customer_info_frame, placeholder_text="Customer E-mail")
        self.customer_email_entry.grid(row=3, column=0, pady=(0, 10))
        self.company_name_entry = customtkinter.CTkEntry(master=self.customer_info_frame, placeholder_text="Company Name")
        self.company_name_entry.grid(row=1, column=1, pady=(0, 10))
        self.company_address_entry = customtkinter.CTkEntry(master=self.customer_info_frame, placeholder_text="Company Address")
        self.company_address_entry.grid(row=2, column=1, pady=(0, 10))
        self.save_checkbox = customtkinter.CTkCheckBox(master=self.customer_info_frame, text="Save Customer") #Feature not implemented
        self.save_checkbox.grid(row=6, column=3, pady=(0, 10))

        # create items frame
        self.items_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.items_frame.grid_rowconfigure(1, weight=1)
        self.items_frame.grid_columnconfigure(3, weight=1)

        self.customer_number_entry = customtkinter.CTkEntry(master=self.items_frame, placeholder_text="Item Name")
        self.customer_number_entry.grid(row=1, column=0, pady=(0,10))
        self.customer_number_entry = customtkinter.CTkEntry(master=self.items_frame, placeholder_text="Qty")
        self.customer_number_entry.grid(row=1, column=1, pady=(0,10))
        self.customer_number_entry = customtkinter.CTkEntry(master=self.items_frame, placeholder_text="Unit Price")
        self.customer_number_entry.grid(row=1, column=2, pady=(0,10))

        self.invoice_button_event()
        '''
        # create main frame
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(row=0, column=1, pady=20, padx=20)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Invoice System")
        self.label.grid(row=0, column=1, pady=(0, 20))

        self.doc_option_menu = customtkinter.CTkOptionMenu(master=self.frame, values=["Invoice"])
        self.doc_option_menu.grid(row=1, column=1, pady=(0, 10))
        self.doc_option_menu.set("Document Type")

        self.customer_name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Customer Name")
        self.customer_name_entry.grid(row=2, column=1, pady=(0, 10))

        self.customer_number_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Customer Number")
        self.customer_number_entry.grid(row=3, column=1, pady=(0, 20))
        '''

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.invoice_button.configure(fg_color=("gray75", "gray25") if name == "invoice" else "transparent")
        #self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        #self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "invoice":
            self.customer_info_frame.grid(row=0, column=1, sticky="nsew")
            self.items_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.customer_info_frame.grid_forget()
            self.items_frame.grid_forget()
        '''
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
            
        '''

    def invoice_button_event(self):
        self.select_frame_by_name("invoice")
"""
def main():
    data = {
        "invoice_number" : 123,
        "customer_info" : {
            "customer_name": "Flan AlFlani",
            "customer_phone": "+965 55555555",
            "customer_email": "flan@example.com",
            "company_name": "Pear Inc",
            "company_address": "Yarmouk, Block 1, St 10, House 11"
        },
        "items" : [
            {
                "item": "Web App",
                "qty": 2,
                "unit_price": 150.750,
                "total": 301.500
            },{
                "item": "AWS Hosting",
                "qty": 2,
                "unit_price": 75.032,
                "total": 150.064
            },{
                "item": "Domain (6 Months)",
                "qty": 1,
                "unit_price": 10.325,
                "total": 10.325
            }
        ]
    }

    #gui = Client_GUI()
    #gui.mainloop()


    #return
    #data = {}

    url = 'http://127.0.0.1:5000/'
    html = requests.post(url, json=data)
    with open('invoice.pdf', 'wb') as f:
        f.write(html.content)

if __name__ == "__main__":
    main()