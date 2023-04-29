# Standard Libs
from flask import Flask, render_template, send_file
import os
import io
from datetime import datetime

# Other Libs
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def render_invoice():

    # Structure invoice data
    current_date = datetime.today().strftime("%B %-d, %Y")
    invoice_number = 123
    customer_info = {
        'customer_name': 'John Doe',
        'customer_number': '+965 99999999',
        'customer_email': 'john@example.com',
        'company_name': 'Orange Inc',
        'company_address': 'Yarmouk, Block 1, St 10, House 11'
    }
    items = [
        {
            'item': 'Website design',
            'qty': 2,
            'unit_price': 150.000,
            'total': 300.000
        },{
            'item': 'Hosting (3 months)',
            'qty': 2,
            'unit_price': 75.032,
            'total': 150.064
        },{
            'item': 'Domain name (1 year)',
            'qty': 1,
            'unit_price': 10.000,
            'total': 10.000
        }

    ]
    total = sum([i['total'] for i in items])

    # Pass in invoice data and render html invoice
    rendered_invoice = render_template('forged_invoice.html',
                            date_issued = current_date,
                            invoice_number = invoice_number,
                            customer_info = customer_info,
                            items = items,
                            total = total
                            )
    # Convert html into pdf
    html = HTML(string=rendered_invoice)
    rendered_pdf = html.write_pdf('static/forged_invoice.pdf')
    return send_file(
            io.BytesIO(rendered_pdf),
            attachment_filename='forged_invoice.pdf'
        )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)