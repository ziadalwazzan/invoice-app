from jsonschema import validate

schema = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#",
	"$id": "localhost:5000/", 
	"title": "Root", 
	"type": "object",
	"required": [
		"customer_info",
		"items",
		"discount_amount",
		"total"
	],
	"properties": {
		"customer_info": {
			"$id": "#root/customer_info", 
			"title": "Customer_info", 
			"type": "object",
			"required": [
				"customer_name",
				"customer_phone",
				"customer_email"
			],
			"properties": {
				"customer_name": {
					"$id": "#root/customer_info/customer_name", 
					"title": "Customer_name", 
					"type": "string",
					"default": "",
					"pattern": "^.*$"
				},
				"customer_phone": {
					"$id": "#root/customer_info/customer_phone", 
					"title": "Customer_phone", 
					"type": "string",
					"default": "",
					"pattern": "^.*$"
				},
				"customer_email": {
					"$id": "#root/customer_info/customer_email", 
					"title": "Customer_email", 
					"type": "string",
					"default": "",
					"pattern": "^.*$"
				},
				"company_name": {
					"$id": "#root/customer_info/company_name", 
					"title": "Company_name", 
					"type": "string",
					"default": "",
					"pattern": "^.*$"
				},
				"company_address": {
					"$id": "#root/customer_info/company_address", 
					"title": "Company_address", 
					"type": "string",
					"default": "",
					"pattern": "^.*$"
				}
			}
		},
		"items": {
			"$id": "#root/items", 
			"title": "Items", 
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/items/items", 
				"title": "Items", 
				"type": "object",
				"required": [
					"name",
					"qty",
					"unit_price"
				],
				"properties": {
					"name": {
						"$id": "#root/items/items/item", 
						"title": "Item", 
						"type": "string",
						"default": "",
						"pattern": "^.*$"
					},
					"qty": {
						"$id": "#root/items/items/qty", 
						"title": "Qty", 
						"type": "integer",
						"default": 0
					},
					"unit_price": {
						"$id": "#root/items/items/unit_price", 
						"title": "Unit_price", 
						"type": "string",
						"default": "^.*$"
					}
				}
			}
		},
		"discount_amount": {
			"$id": "#root/discount_amount", 
			"title": "Discount_amount", 
			"type": "string",
			"default": ""
		},
		"total": {
			"$id": "#root/total", 
			"title": "Total", 
			"type": "string",
			"default": ""
		}
	}
}

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
    schema=schema,
)

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
    schema=schema,
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
    schema=schema,
)
