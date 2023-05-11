DROP TABLE IF EXISTS c_info;
DROP TABLE IF EXISTS invoice;

CREATE TABLE c_info (
    c_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT,
    company_name TEXT,
    company_address TEXT
);

CREATE TABLE invoice (
    invoice_id INTEGER PRIMARY KEY,
    c_id INTEGER,
    FOREIGN KEY (c_id) REFERENCES c_info(c_id)
);
