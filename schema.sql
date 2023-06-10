DROP TABLE IF EXISTS c_info;
DROP TABLE IF EXISTS invoice;
DROP TABLE IF EXISTS invoice_items;

CREATE TABLE c_info (
    c_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT,
    company_name TEXT,
    company_address TEXT
);

CREATE TABLE invoice (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    c_id INTEGER,
    discount_amount TEXT,
    total TEXT,
    FOREIGN KEY (c_id) REFERENCES c_info(c_id)
);

CREATE TABLE invoice_items (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    qty TEXT,
    unit_price TEXT,
    invoice_id INTEGER,
    FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id)
);
