# Standard Libs
import json
import tkinter as tk

# Other Libs
import requests

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

def main():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()
    print("HIIIII")
    return
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

    url = 'http://127.0.0.1:5000/'
    html = requests.post(url, json=data)
    with open('invoice.pdf', 'wb') as f:
        f.write(html.content)

if __name__ == "__main__":
    main()