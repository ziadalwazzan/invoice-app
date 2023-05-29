# Standard Libs
import json
import os

# Other Libs
import requests

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
                "name": "Web App",
                "qty": 2,
                "unit_price": 150.750,
                "total": 301.500
            },{
                "name": "AWS Hosting",
                "qty": 2,
                "unit_price": 75.032,
                "total": 150.064
            },{
                "name": "Domain (6 Months)",
                "qty": 1,
                "unit_price": 10.325,
                "total": 10.325
            }
        ]
    }

    url = 'http://127.0.0.1:5000/'
    html = requests.post(url, json=data)
    with open('invoice.pdf', 'wb') as f:
        f.write(html.content)

if __name__ == "__main__":
    main()