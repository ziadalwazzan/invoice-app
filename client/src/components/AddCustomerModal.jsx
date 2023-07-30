import React, { Fragment, useState } from 'react';
import { Dialog, Transition } from '@headlessui/react';
import axios from 'axios';

const AddCustomerModal = ({
  isOpen,
  setIsOpen,
  onAddCustomer,
}) => {
    const [newCustomerName, setNewCustomerName] = useState('')
    const [newCustomerPhone, setNewCustomerPhone] = useState('')
    const [newCustomerEmail, setNewCustomerEmail] = useState('')
    const [newCompanyName, setNewCompanyName] = useState('')
    const [newCompanyAddress, setNewCompanyAddress] = useState('')

    function closeModal() {
        setIsOpen(false);
    };


    const addCustomerHandler = (event) => {
        event.preventDefault();
        axios.post(
            'http://127.0.0.1:5000/customers/addCustomer',
            {
                'customer_name': newCustomerName,
                'customer_phone': newCustomerPhone,
                'customer_email': newCustomerEmail,
                'company_name': newCompanyName,
                'company_address': newCompanyAddress,
                responseType: 'json',
                headers: {
                'Access-Control-Allow-Origin' : '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Credentials': 'true'
                }
            }
            )
            .then((response) => {
                const c_id = response.data['c_id']
                const newCustomer = {
                    'id': c_id,
                    'customerName': newCustomerName,
                    'customerPhone': newCustomerPhone,
                    'customerEmail': newCustomerEmail,
                    'companyName': newCompanyName,
                    'companyAddress': newCompanyAddress
                }
                onAddCustomer(newCustomer);
                closeModal();
            })
            .catch(error => {
                alert('Server responded with:' + error.response.status )
                if (error.response) {
                    console.error('Server Error:', error.response.status);
                } else if (error.request) {
                    console.error('Network Error:', error.request);
                } else {
                    console.error('Error:', error.message);
                }
            });
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
            <div className="my-8 inline-block w-full max-w-md transform overflow-hidden rounded-lg bg-white align-middle shadow-xl transition-all">
                <div className="p-4" id="print">
                <h1 className="text-center text-lg font-bold text-gray-900">
                    Add Customer
                </h1>
                <div className="mt-6">
                    <table className="w-full">
                        <tbody>
                            <tr>
                                <td className="w-full">
                                    <input
                                    required // Figure out why required not working
                                    className='text-center'
                                    type='text'
                                    placeholder='Name'
                                    value={newCustomerName}
                                    onChange={(event) => setNewCustomerName(event.target.value)}
                                    />
                                </td>
                            </tr>
                            <tr>
                                <td className="w-full">
                                    <input
                                    required
                                    className='text-center'
                                    type='text'
                                    placeholder='Phone'
                                    value={newCustomerPhone}
                                    onChange={(event) => setNewCustomerPhone(event.target.value)}
                                    />
                                </td>
                            </tr>
                            <tr>
                                <td className="w-full">
                                    <input
                                    className='text-center'
                                    type='text'
                                    placeholder='Email'
                                    value={newCustomerEmail}
                                    onChange={(event) => setNewCustomerEmail(event.target.value)} />
                                </td>
                            </tr>
                            <tr>
                            <td className="w-full">
                                    <input
                                    className='text-center'
                                    type='text'
                                    placeholder='Company Name'
                                    value={newCompanyName}
                                    onChange={(event) => setNewCompanyName(event.target.value)} />
                                </td>
                            </tr>
                            <tr>
                            <td className="w-full">
                                    <input
                                    className='text-center'
                                    type='text'
                                    placeholder='Company Address'
                                    value={newCompanyAddress}
                                    onChange={(event) => setNewCompanyAddress(event.target.value)} />
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                </div>
                <div className="mt-4 flex space-x-2 px-4 pb-6">
                <button
                    onClick={addCustomerHandler}
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
                    <span>Add Customer</span>
                </button>
                </div>
            </div>
            </Transition.Child>
        </div>
        </Dialog>
    </Transition>
    );
};

export default AddCustomerModal;
