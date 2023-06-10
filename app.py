# Standard Libs
from flask import Flask, render_template, send_file, request, abort, make_response
from flask_cors import CORS # TODO: add CORS support
import sqlite3
import os
import json
from math import fsum
from datetime import datetime

# Other Libs
from flask_expects_json import expects_json
from weasyprint import HTML

# Set up app config

app = Flask(__name__)
CORS(app, expose_headers=["Content-Disposition"])

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Load json schema
with open("static/schema.json") as fp:
    schema = json.load(fp)

@app.route('/', methods = ['POST'])
#@expects_json(schema)
def render_invoice():
    print(f"request JSON data: \n {request.get_json()} \n\n\n")
    
    if request.method == "POST": 
        # Parse client POST request JSON data
        params = request.get_json()
        customer_info, items, discount, total = params.get('customer_info'), params.get('items'), params.get('discount'), params.get('total')
        current_date = datetime.today().strftime("%B %-d, %Y")

        ''' TODO: Review request validation
        # Validate request data
        if not (customer_info['customer_name'] and customer_info['customer_phone'] and customer_info['customer_email'] and [i['total'] for i in items] ):
                return abort(409, 
                            ("Request must include customer_info -> ",
                            "customer_name,customer_phone,customer_email ",
                            "and 'items' as part of the JSON data.")
                            )
        '''

        # Update DB model ->
        # if customer exists -> select and store customer id from table
        #   else--> add customer then select id
        # insert invoice details discount/total into invoices table
        # select and store invoice id
        # insert invoice items into invoice_items table with invoice_id foreign key
        conn = get_db_connection()

        #Check if customer data exists or store it (referenced by phone)
        query = f'select * from c_info where phone={customer_info["customer_phone"]};'
        row = conn.execute(query).fetchone()

        if row is None:
            # insert row into c_info table
            conn.execute(f'INSERT INTO c_info (name,phone,email,company_name,company_address) VALUES ( \'{customer_info["customer_name"]}\', {customer_info["customer_phone"]}, \'{customer_info["customer_email"]}\', \'{customer_info["company_name"]}\', \'{customer_info["company_address"]}\');')
            conn.commit()
            # Select customer ID to insert it as a foreign key
            customer_id = conn.execute(query).fetchone()['c_id']
        else:
            customer_id = row['c_id']
            print("DB query returned with customer: {}".format(row['name']))
            print('customer already exists')

        # invoice table insert
        conn.execute(f'INSERT INTO invoice (c_id,discount_amount,total) VALUES ({customer_id}, \'{discount}\', \'{total}\')')
        conn.commit()

        # get invoice id
        invoice_number = conn.execute('SELECT invoice_id FROM invoice ORDER BY invoice_id DESC LIMIT 1;').fetchone()['invoice_id']
        print("\n\n//////// invoice_id: {} ////////////\n\n".format(invoice_number))

        # insert invoice items
        for item in items:
            conn.execute(f'INSERT INTO invoice_items (name,qty,unit_price,invoice_id) VALUES (\'{item["name"]}\', \'{item["qty"]}\', \'{item["unit_price"]}\', {invoice_number} )')
            conn.commit()

        conn.close()
        
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
        file_name = f"invoice-{invoice_number}-{customer_info['customer_phone']}.pdf"
        return send_file('static/forged_invoice.pdf', download_name=file_name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)