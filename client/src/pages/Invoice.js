import React from 'react';
import InvoiceForm from '../components/InvoiceForm';

function Invoice() {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="mx-auto max-w-6xl absolute right-0">
        <InvoiceForm />
      </div>
    </div>
  );
}

export default Invoice;
