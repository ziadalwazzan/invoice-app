# Standard Libs
from flask import Flask, render_template, send_file, request, abort, make_response
from flask_cors import CORS
import sqlite3
import os
import json
from datetime import datetime
import logging
from logging import handlers

# Other Libs
from flask_expects_json import expects_json
from weasyprint import HTML

# Set up app config
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = handlers.TimedRotatingFileHandler('logs/invoice-app-server.log', when="midnight", backupCount=3, interval=5)
handler.suffix = "%Y-%m-%d_%H-%M-%S"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

app = Flask(__name__)
CORS(app, expose_headers=["Content-Disposition"])

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Load json schemas customer_lookup_schema
with open("static/render_invoice_schema.json") as fp:
    render_invoice_schema = json.load(fp)

'''
render_invoice method:

REQUIRES the following payload with JSON schema:
{
    'customer_info': {
        'customer_name': 'NAME',                            STRING
        'customer_phone': 'PHONE',                          STRING
        'customer_email': 'EMAIL',                          STRING
        'company_name': 'NAME',                             STRING
        'company_address': 'ADDRESS'},                      STRING
    'items': [
        {
        'name': 'ITEM-NAME',                                STRING
        'qty': ITEM-QTY,                                       INT
        'unit_price': 'UNIT_PRICE'                          STRING
        },
        {
        'name': 'ITEM-NAME',                                STRING
        'qty': ITEM-QTY,                                       INT
        'unit_price': 'UNIT_PRICE'                          STRING
        },
        {...}
    ], 
    'discount_amount': 'AMOUNT',                            STRING
    'total': 'AMOUNT'                                       STRING
}
'''
@app.route('/render_invoice', methods = ['POST'])
@expects_json(render_invoice_schema)
def render_invoice():
    app.logger.info('ROUTE: /render_invoice')
    app.logger.info(f"request JSON data: \n {request.get_json()}")
    
    if request.method == "POST": 
        # Parse client POST request JSON data
        params = request.get_json()
        customer_info, items, discount, total = params.get('customer_info'), params.get('items'), params.get('discount_amount'), params.get('total')
        current_date = datetime.today().strftime("%B %-d, %Y")

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
            app.logger.info(f'Customer {row["name"]} already exists')

        # invoice table insert
        conn.execute(f'INSERT INTO invoice (c_id,discount_amount,total) VALUES ({customer_id}, \'{discount}\', \'{total}\')')
        conn.commit()

        # get invoice id from db
        invoice_number = conn.execute('SELECT invoice_id FROM invoice ORDER BY invoice_id DESC LIMIT 1;').fetchone()['invoice_id']
        
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
                            
        # File system formatting
        file_name = f"invoice-{invoice_number}-{customer_info['customer_phone']}.pdf"
        dir_name = f"{datetime.today().year}-{datetime.today().month}"
        if not os.path.exists(f"invoices/{dir_name}"):
            os.mkdir(f"invoices/{dir_name}")

        # Convert html into pdf and send to client
        html = HTML(string=rendered_invoice, base_url=request.base_url)
        html.write_pdf(f'invoices/{dir_name}/{file_name}')
        return send_file(f"invoices/{dir_name}/{file_name}", download_name=file_name)
    

""" TODO Implement /render_qoute method
'''
render_qoute method:

REQUIRES the following payload with JSON schema:
{
    'customer_info': {
        'customer_name': 'NAME',                            STRING
        'customer_phone': 'PHONE',                          STRING
        'customer_email': 'EMAIL',                          STRING
        'company_name': 'NAME',                             STRING
        'company_address': 'ADDRESS'},                      STRING
    'items': [
        {
        'name': 'ITEM-NAME',                                STRING
        'qty': ITEM-QTY,                                       INT
        'unit_price': 'UNIT_PRICE'                          STRING
        },
        {
        'name': 'ITEM-NAME',                                STRING
        'qty': ITEM-QTY,                                       INT
        'unit_price': 'UNIT_PRICE'                          STRING
        },
        {...}
    ], 
    'discount_amount': 'AMOUNT',                            STRING
    'due_date': 'DATE',                                     STRING
    'total': 'AMOUNT'                                       STRING
}
'''
@app.route('/render_qoute', methods = ['POST'])
#@expects_json(render_qoute_schema)
def render_qoute():
    app.logger.info('ROUTE: /render_qoute')
    app.logger.info(f"request JSON data: \n {request.get_json()}")
    
    if request.method == "POST": 
        # Parse client POST request JSON data
        params = request.get_json()
        customer_info, items, discount,due_date, total = params.get('customer_info'), params.get('items'), params.get('discount_amount'), params.get('due_date'), params.get('total')
        current_date = datetime.today().strftime("%B %-d, %Y")

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
            app.logger.info(f'Customer {row["name"]} already exists')

        # invoice table insert
        conn.execute(f'INSERT INTO invoice (c_id,discount_amount,total) VALUES ({customer_id}, \'{discount}\', \'{total}\')')
        conn.commit()

        # get invoice id from db
        invoice_number = conn.execute('SELECT invoice_id FROM invoice ORDER BY invoice_id DESC LIMIT 1;').fetchone()['invoice_id']
        
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
                            
        # File system formatting
        file_name = f"invoice-{invoice_number}-{customer_info['customer_phone']}.pdf"
        dir_name = f"{datetime.today().year}-{datetime.today().month}"
        if not os.path.exists(f"invoices/{dir_name}"):
            os.mkdir(f"invoices/{dir_name}")

        # Convert html into pdf and send to client
        html = HTML(string=rendered_invoice, base_url=request.base_url)
        html.write_pdf(f'invoices/{dir_name}/{file_name}')
        return send_file(f"invoices/{dir_name}/{file_name}", download_name=file_name)
    """


'''
lookup_customer method:

REQUIRES the following payload:
/lookup_customer?customer_phone=INSERT_PHONE_NUMBER

'''
@app.route('/lookup_customer', methods = ['GET'])
def lookup_customer():
    app.logger.info('ROUTE: /lookup_customer')
    if request.method == "GET":
        # Parse client request JSON data
        customer_phone = request.args.get('customer_phone')
        app.logger.info(f'request arguments: {customer_phone}')

        # Query client by phone number
        conn = get_db_connection()
        query = f'select * from c_info where phone={customer_phone};'
        row = conn.execute(query).fetchone()
        if row:
            response = {
                'customer_name' : row['name'],
                'customer_phone' : row['phone'],
                'customer_email' : row['email'],
                'company_name' : row['company_name'],
                'company_address' : row['company_address'],
            }
            app.logger.info(f"DB query returned with customer: {response}")
            return response
        else:
            app.logger.info(f"Customer {customer_phone} not registered")
            abort(404)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)