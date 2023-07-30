import React, { useState } from 'react';
import { uid } from 'uid';
import InvoiceItem from './InvoiceItem';
import InvoiceModal from './InvoiceModal';
import axios from 'axios';

const date = new Date();
const today = date.toLocaleDateString('en-GB', {
  month: 'numeric',
  day: 'numeric',
  year: 'numeric',
});

const QouteForm = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [discount, setDiscount] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [cashierName, setCashierName] = useState('');
  const [customerName, setCustomerName] = useState('');
  const [customerPhone, setCustomerPhone] = useState('');
  const [customerEmail, setCustomerEmail] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [companyAddress, setCompanyAddress] = useState('');
  const [items, setItems] = useState([
    {
      id: uid(6),
      name: '',
      qty: 1,
      unit_price: '1.000',
    },
  ]);

  const reviewInvoiceHandler = (event) => {
    event.preventDefault();
    setIsOpen(true);
  };

  const addNextInvoiceHandler = () => {
    setItems([
      {
        id: uid(6),
        name: '',
        qty: 1,
        unit_price: '1.000',
      },
    ]);
  };

  const addItemHandler = () => {
    const id = uid(6);
    setItems((prevItem) => [
      ...prevItem,
      {
        id: id,
        name: '',
        qty: 1,
        unit_price: '1.000',
      },
    ]);
  };

  const deleteItemHandler = (id) => {
    setItems((prevItem) => prevItem.filter((item) => item.id !== id));
  };

  const edtiItemHandler = (event) => {
    const editedItem = {
      id: event.target.id,
      name: event.target.name,
      value: event.target.value,
    };

    const newItems = items.map((items) => {
      for (const key in items) {
        if (key === editedItem.name && items.id === editedItem.id) {
          items[key] = editedItem.value;
        }
      }
      return items;
    });

    setItems(newItems);
  };

  const subtotal = items.reduce((prev, curr) => {
    if (curr.name.trim().length > 0)
      return prev + Number(curr.unit_price * Math.floor(curr.qty));
    else return prev;
  }, 0);
  
  const discountAmount = discount - 0;
  const total = subtotal - discountAmount;

  const lookupCustomer = async(e) => {
    e.preventDefault()
    let json_data = {'customer_phone': customerPhone}
    console.log(json_data)
    axios.get(
      'http://127.0.0.1:5000/lookup_customer', 
      { params: {'customer_phone': customerPhone} }, // CHECK MEDIA TYPE
      {
        responseType: 'json',
        headers: {
          'Access-Control-Allow-Origin' : '*',
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Credentials': 'true'
        }
      }
    )
    .then((response) => {
      console.log(response.data)
      setCustomerName(response.data['customer_name']);
      setCustomerPhone(response.data['customer_phone']);
      setCustomerEmail(response.data['customer_email']);
      setCompanyName(response.data['company_name']);
      setCompanyAddress(response.data['company_address']);
    })
    .catch(e => {
      console.log('error: ', e);
    });
  };

  return (
    <form
      className="relative flex flex-col px-2 md:flex-row"
      onSubmit={reviewInvoiceHandler}
    >
      <div className="my-6 flex-1 space-y-2 rounded-md bg-white p-4 shadow-sm sm:space-y-4 md:p-6">
        <div className="flex flex-col justify-between px-20 space-y-2 border-b border-gray-900/10 pb-4 md:flex-row md:items-center md:space-y-0">
          <div className="flex space-x-2">
            <span className="font-bold">Current Date: </span>
            <span>{today}</span>
          </div>
          <div className="flex items-center space-x-2">
            <label className="font-bold" htmlFor="cashierName">
              Cashier Name:
            </label>
            <input
              className="max-w-[150px]"
              type="text"
              name="cashierName"
              id="cashierName"
              value={cashierName}
              onChange={(event) => setCashierName(event.target.value)}
            />
          </div>
        </div>
        <h1 className="text-center text-lg font-bold">QOUTE</h1>
        <div className="grid grid-cols-2 gap-2 pt-4 pb-8">
          <label
            htmlFor="customerPhone"
            className="col-start-1 row-start-1 text-sm font-bold md:text-base"
          >
          Customer Info:
          </label>
          <input
            required
            className="col-start-1 text-sm md:text-base"
            placeholder="Phone"
            type="text"
            name="customerPhone"
            id="customerPhone"
            value={customerPhone}
            onChange={(event) => setCustomerPhone(event.target.value)}
          />
          <button
             className="w-full rounded-md bg-blue-500 py-2 text-sm text-white shadow-sm hover:bg-blue-600"
             type="submit"
             onClick={lookupCustomer}
           >
             Lookup By Phone
          </button>
          <input
            required
            className="flex-1"
            placeholder="Name"
            type="text"
            name="customerName"
            id="customerName"
            value={customerName}
            onChange={(event) => setCustomerName(event.target.value)}
          />
          <input
            className="flex-1"
            placeholder="Email"
            type="text"
            name="customerEmail"
            id="customerEmail"
            value={customerEmail}
            onChange={(event) => setCustomerEmail(event.target.value)}
          />
         <input
           className="col-start-1 text-sm md:text-base"
           placeholder="Company name"
           type="text"
           name="companyName"
           id="companyName"
           value={companyName}
           onChange={(event) => setCompanyName(event.target.value)}
         />
         <input
           className="flex-1"
           placeholder="Company address"
           type="text"
           name="companyAddress"
           id="companyAddress"
           value={companyAddress}
           onChange={(event) => setCompanyAddress(event.target.value)}
         />
        </div>
        <table className="w-full p-4 text-left">
          <thead>
            <tr className="border-b border-gray-900/10 text-sm md:text-base">
              <th>ITEM</th>
              <th>QTY</th>
              <th className="text-center">PRICE</th>
              <th className="text-center">ACTION</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item) => (
              <InvoiceItem
                key={item.id}
                id={item.id}
                name={item.name}
                qty={item.qty}
                unit_price={item.unit_price}
                onDeleteItem={deleteItemHandler}
                onEdtiItem={edtiItemHandler}
              />
            ))}
          </tbody>
        </table>
        <button
          className="rounded-md bg-blue-500 px-4 py-2 text-sm text-white shadow-sm hover:bg-blue-600"
          type="button"
          onClick={addItemHandler}
        >
          Add Item
        </button>
        <div className="flex flex-col items-end space-y-2 pt-6">
          <div className="flex w-full justify-between md:w-1/2">
            <span className="font-bold">Subtotal:</span>
            <span>KWD {subtotal.toFixed(3)}</span>
          </div>
          <div className="flex w-full justify-between md:w-1/2">
            <span className="font-bold">Discount:</span>
            <span>
              KWD {discountAmount.toFixed(3)}
            </span>
          </div>
          <div className="flex w-full justify-between border-t border-gray-900/10 pt-2 md:w-1/2">
            <span className="font-bold">Total:</span>
            <span className="font-bold">
              KWD {total % 1 === 0 ? total : total.toFixed(3)}
            </span>
          </div>
        </div>
      </div>
      <div className="basis-1/4 bg-transparent">
        <div className="sticky top-0 z-10 space-y-4 divide-y divide-gray-900/10 pb-8 md:pt-6 md:pl-4">
          <button
            className="w-full rounded-md bg-blue-500 py-2 text-sm text-white shadow-sm hover:bg-blue-600"
            type="submit"
          >
            Review Qoute
          </button>
          <InvoiceModal
            isOpen={isOpen}
            setIsOpen={setIsOpen}
            docType="Qoute"
            invoiceInfo={{
              cashierName,
              customerPhone,
              customerName,
              customerEmail,
              companyName,
              companyAddress,
              subtotal,
              discountAmount,
              dueDate,
              total,
            }}
            items={items}
            onAddNextInvoice={addNextInvoiceHandler}
          />
          <div className="space-y-4 py-2">
            <div className="space-y-2">
                <label
                className="text-sm font-bold md:text-base"
                htmlFor="discount"
                >
                Discount amount:
                </label>
                <div className="flex items-center">
                    <input
                        className="w-full rounded-r-none bg-white shadow-sm"
                        type="number"
                        name="discount"
                        id="discount"
                        min="0"
                        step="0.500"
                        placeholder="0.000"
                        value={discount}
                        onChange={(event) => setDiscount(event.target.value)}
                    />
                    <span className="rounded-r-md bg-gray-200 py-2 px-4 text-gray-500 shadow-sm">
                        KWD
                    </span>
                </div>
                <br></br>
                <label
                className="text-sm font-bold md:text-base"
                htmlFor="dueDate"
                >
                Due date:
                </label>
                <div className="flex items-center">
                    <input
                    className="w-full rounded-r-none bg-white shadow-sm"
                    type="date"
                    name="dueDate"
                    id="dueDate"
                    value={dueDate}
                    onChange={(event) => setDueDate(event.target.value)}
                    />
                </div>
            </div>
          </div>
        </div>
      </div>
    </form>
  );
};

export default QouteForm;
