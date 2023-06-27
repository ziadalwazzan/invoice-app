import json
from jsonschema import validate

#Load json schemas customer_lookup_schema
with open("./static/render_invoice_schema.json") as fp:
    render_invoice_schema = json.load(fp)
with open("./static/lookup_customer_schema.json") as fp:
    lookup_customer_schema = json.load(fp)

# No error, the JSON is valid.
validate(
    instance={
        'customer_info': {
            'customer_name': 'Ziad AlWazzan',
            'customer_phone': '7864772581',
            'customer_email': 'q8-zayood@hotmail.com',
            'company_name': '',
            'company_address': '1975 30th St, APT 328'
            }, 
            'items': [
                {
                    'id': '819734',
                    'name': 'qww',
                    'qty': 1,
                    'unit_price': '1.000'
                }
            ],
            'discount_amount': "0",
            'total': "1"
    },
    schema=render_invoice_schema,
)

# No error, the JSON is valid.
validate(
    instance={
        "customer_info" : {
            "customer_name": "Flan AlFlani",
            "customer_phone": "+965 55555555",
            "customer_email": "flan@example.com",
            "company_name": "Pear Inc",
            "company_address": "Yarmouk, Block 1, St 10, House 11"
        },
        "items" : [
            {
                "id" : "h234h5hr542",
                "name": "Web App",
                "qty": 2,
                "unit_price": "150.750"
            },{
                "id" : "h234h5hr542",
                "name": "AWS Hosting",
                "qty": 2,
                "unit_price": "75.032"
            }
        ],
        'discount_amount' : '5.0',
        'total' : "100"
    },
    schema=render_invoice_schema,
)

# No error, the JSON is valid.
validate(
    instance={
        "customer_info" : {
            "customer_name": "Flan AlFlani",
            "customer_phone": "+965 55555555",
            "customer_email": "flan@example.com",
        },
        "items" : [
            {
                "name": "Web App",
                "qty": 2,
                "unit_price": "150.750",
                "total": 301.500
            },{
                "name": "AWS Hosting",
                "qty": 2,
                "unit_price": "75.032",
                "total": 150.064
            }
        ],
        'discount_amount' : '5.0',
        'total' : "100"
    },
    schema=render_invoice_schema,
)

# No error, the JSON is valid.
validate(
    instance={
        'customer_info': {
            'customer_name': 'Ziad AlWazzan',
            'customer_phone': '7864772581',
            'customer_email': 'q8-zayood@hotmail.com',
            'company_name': '',
            'company_address': '1975 30th St, APT 328'
		}
    },
    schema=lookup_customer_schema,
)