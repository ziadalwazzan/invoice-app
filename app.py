# Standard Libs
from flask import Flask, render_template, send_file, request
import os
import io
from math import fsum
from datetime import datetime

# Other Libs
from weasyprint import HTML

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) # Add JSON request capability
def render_invoice():

    # Get client request JSON data
    posted_data = request.get_json() or {}
    #print(posted_data['invoice_number'])

    # Structure invoice data
    current_date = datetime.today().strftime("%B %-d, %Y")

    default_data = {
        'invoice_number' : 123,
        'customer_info' : {
            'customer_name': 'John Doe',
            'customer_number': '+965 99999999',
            'customer_email': 'john@example.com',
            'company_name': 'Orange Inc',
            'company_address': 'Yarmouk, Block 1, St 10, House 11'
        },
        'items' : [
            {
                'item': 'Default_item 1',
                'qty': 2,
                'unit_price': 150.750,
                'total': 301.500
            },{
                'item': 'Default_item 2',
                'qty': 2,
                'unit_price': 75.032, # Check type casting issue
                'total': 150.064
            },{
                'item': 'Default_item 3',
                'qty': 1,
                'unit_price': 10.325,
                'total': 10.325
            }
        ]
    }

    invoice_number = posted_data.get('invoice_number', 
                                      default_data['invoice_number'])
    customer_info = posted_data.get('customer_info', 
                                      default_data['customer_info'])
    items = posted_data.get('items', default_data['items'])

    total = round(fsum([i['total'] for i in items]),3)
    
    # Pass in invoice data and render html invoice
    rendered_invoice = render_template('forged_invoice.html',
                            date_issued = current_date,
                            invoice_number = invoice_number,
                            customer_info = customer_info,
                            items = items,
                            total = total
                            )
                            
    # Convert html into pdf and send to client
    html = HTML(string=rendered_invoice, base_url=request.base_url )
    rendered_pdf = html.write_pdf('static/forged_invoice.pdf')
    return send_file('static/forged_invoice.pdf')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)