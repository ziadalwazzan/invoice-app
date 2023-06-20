import React, { Fragment } from 'react';
import { Dialog, Transition } from '@headlessui/react';
import axios from 'axios';

const InvoiceModal = ({
  isOpen,
  setIsOpen,
  invoiceInfo,
  items,
  onAddNextInvoice,
}) => {
  function closeModal() {
    setIsOpen(false);
  }

  const postInvoiceData = async(e) => {
    e.preventDefault()
    let post_data = {
      customer_info : {
        customer_name : invoiceInfo.customerName,
        customer_phone : invoiceInfo.customerPhone,
        customer_email : invoiceInfo.customerEmail,
        company_name: invoiceInfo.companyName,
        company_address : invoiceInfo.companyAddress
      },
      items,
      discount_amount: JSON.stringify(invoiceInfo.discountAmount),
      total: JSON.stringify(invoiceInfo.total)
    }
    console.log(post_data)
    axios.post(
      'http://127.0.0.1:5000/render_invoice', 
      post_data,
      {
        responseType: 'blob',
        headers: {
          'Access-Control-Allow-Origin' : '*',
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Credentials': 'true'
        }
      }
    )
    .then(response => {
      // create file link in browser's memory
      const href = URL.createObjectURL(response.data);

      const filename = response.headers.get("content-disposition").split('filename=')[1]

      // create "a" HTML element with href to file & click
      const link = document.createElement('a');
      link.href = href;
      link.setAttribute('download', filename); //or any other extension
      document.body.appendChild(link);
      link.click();

      // clean up "a" element & remove ObjectURL
      document.body.removeChild(link);
      URL.revokeObjectURL(href);
    })
    .catch(e => {
      console.log('error: ', e);
    });
  };

  const addNextInvoiceHandler = (event) => {
    postInvoiceData(event);
    setIsOpen(false);
    onAddNextInvoice();
  };

  return (
    <Transition appear show={isOpen} as={Fragment}>
      <Dialog
        as="div"
        className="fixed inset-0 z-10 overflow-y-auto"
        onClose={closeModal}
      >
        <div className="min-h-screen px-4 text-center">
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <Dialog.Overlay className="fixed inset-0 bg-black/50" />
          </Transition.Child>

          {/* This element is to trick the browser into centering the modal contents. */}
          <span
            className="inline-block h-screen align-middle"
            aria-hidden="true"
          >
            &#8203;
          </span>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0 scale-95"
            enterTo="opacity-100 scale-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100 scale-100"
            leaveTo="opacity-0 scale-95"
          >
            <div className="my-8 inline-block w-full max-w-md transform overflow-hidden rounded-lg bg-white text-left align-middle shadow-xl transition-all">
              <div className="p-4" id="print">
                <h1 className="text-center text-lg font-bold text-gray-900">
                  INVOICE
                </h1>
                <div className="mt-6">
                  <div className="mb-4 grid grid-cols-2">
                    <span className="font-bold">Customer Name:</span>
                    <span>{invoiceInfo.customerName}</span>
                    <span className="font-bold">Customer Number:</span>
                    <span>{invoiceInfo.customerPhone}</span>
                    <span className="font-bold">Customer E-mail:</span>
                    <span>{invoiceInfo.customerEmail}</span>
                    <span className="font-bold">Company Name:</span>
                    <span>{invoiceInfo.companyName}</span>
                    <span className="font-bold">Company Address:</span>
                    <span>{invoiceInfo.companyAddress}</span>
                  </div>

                  <table className="w-full text-left">
                    <thead>
                      <tr className="border-y border-black/10 text-sm md:text-base">
                        <th>ITEM</th>
                        <th className="text-center">QTY</th>
                        <th className="text-right">PRICE</th>
                        <th className="text-right">AMOUNT</th>
                      </tr>
                    </thead>
                    <tbody>
                      {items.map((item) => (
                        <tr key={item.id}>
                          <td className="w-full">{item.name}</td>
                          <td className="min-w-[50px] text-center">
                            {item.qty}
                          </td>
                          <td className="min-w-[120px] text-right">
                            KWD {Number(item.unit_price).toFixed(3)}
                          </td>
                          <td className="min-w-[140px] text-right">
                            KWD {Number(item.unit_price * item.qty).toFixed(3)}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>

                  <div className="mt-4 flex flex-col items-end space-y-2">
                    <div className="flex w-full justify-between border-t border-black/10 pt-2">
                      <span className="font-bold">Subtotal:</span>
                      <span>KWD {invoiceInfo.subtotal.toFixed(3)}</span>
                    </div>
                    <div className="flex w-full justify-between">
                      <span className="font-bold">Discount:</span>
                      <span>KWD {invoiceInfo.discountAmount.toFixed(3)}</span>
                    </div>
                    <div className="flex w-full justify-between border-t border-black/10 py-2">
                      <span className="font-bold">Total:</span>
                      <span className="font-bold">
                        KWD
                        {invoiceInfo.total % 1 === 0
                          ? invoiceInfo.total
                          : invoiceInfo.total.toFixed(3)}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <div className="mt-4 flex space-x-2 px-4 pb-6">
                <button
                  onClick={addNextInvoiceHandler}
                  className="flex w-full items-center justify-center space-x-1 rounded-md bg-blue-500 py-2 text-sm text-white shadow-sm hover:bg-blue-600"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-4 w-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M13 5l7 7-7 7M5 5l7 7-7 7"
                    />
                  </svg>
                  <span>Generate invoice</span>
                </button>
              </div>
            </div>
          </Transition.Child>
        </div>
      </Dialog>
    </Transition>
  );
};

export default InvoiceModal;
