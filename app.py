# Standard Libs
from flask import Flask, render_template, send_file, request, abort
import sqlite3
import os
import io
import json
from math import fsum
from datetime import datetime

# Other Libs
from flask_expects_json import expects_json
from weasyprint import HTML

# Set up app config

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Load json schema
with open("static/schema.json") as fp:
    schema = json.load(fp)

@app.route('/', methods = ['POST'])
@expects_json(schema)
def render_invoice():

    # Parse client POST request JSON data
    params = request.get_json()
    customer_info, items, invoice_number = params.get('customer_info'), params.get('items'), params.get('invoice_number')
    current_date = datetime.today().strftime("%B %-d, %Y")

    # Validate request data
    if not (customer_info['customer_name'] and customer_info['customer_phone'] and customer_info['customer_email'] and [i['total'] for i in items] ):
            return abort(400, 
                         ("Request must include customer_info -> ",
                         "customer_name,customer_phone,customer_email ",
                         "and 'items' as part of the JSON data.")
                        )

    # DB
    conn = get_db_connection()
    ins = conn.execute('SELECT * FROM c_info').fetchall()
    conn.close()
    print(ins)


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