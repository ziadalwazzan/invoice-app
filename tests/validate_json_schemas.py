from jsonschema import validate

schema = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#",
	"$id": "localhost:5000/", 
	"title": "Root", 
	"type": "object",
	"required": [
		"invoice_number",
		"customer_info",
		"items"
	],
	"properties": {
		"invoice_number": {
			"$id": "#root/invoice_number", 
			"title": "Invoice_number", 
			"type": "integer",
			"default": 0
		},
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
					"item",
					"qty",
					"unit_price",
					"total"
				],
				"properties": {
					"item": {
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
						"type": "number",
						"default": 0.0
					},
					"total": {
						"$id": "#root/items/items/total", 
						"title": "Total", 
						"type": "number",
						"default": 0.0
					}
				}
			}
		}
	}
}

# No error, the JSON is valid.

validate(
    instance={
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
            }
        ]
    },
    schema=schema,
)

# No error, the JSON is valid.

validate(
    instance={
        "invoice_number" : 123,
        "customer_info" : {
            "customer_name": "Flan AlFlani",
            "customer_phone": "+965 55555555",
            "customer_email": "flan@example.com",
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
            }
        ]
    },
    schema=schema,
)
