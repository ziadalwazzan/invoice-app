import React from 'react';
import CustomerField from './CustomerField';

const Customer = ({ id, customerName, customerPhone, customerEmail, companyName, companyAddress, onDeleteCustomer }) => {
  const deleteCustomerHandler = () => {
    onDeleteCustomer(id);
  };

  return (
    <tr>
      <td className="min-w-[200px] md:min-w-[200px]">
        <CustomerField
          cellData={{
            type: 'text',
            name: 'customerName',
            id: id,
            value: customerName,
          }}
        />
      </td>
      <td className="min-w-[150px] md:min-w-[150px]">
        <CustomerField
          cellData={{
            type: 'text',
            name: 'customerPhone',
            id: id,
            value: customerPhone,
          }}
        />
      </td>
      <td className="relative min-w-[200px] md:min-w-[200px]">
        <CustomerField
          cellData={{
            type: 'text',
            name: 'customerEmail',
            id: id,
            value: customerEmail,
          }}
        />
      </td>
      <td className="relative min-w-[150px] md:min-w-[200px]">
        <CustomerField
          cellData={{
            type: 'text',
            name: 'companyName',
            id: id,
            value: companyName,
          }}
        />
      </td>
      <td className="relative min-w-[150px] md:min-w-[350px]">
        <CustomerField
          cellData={{
            type: 'text',
            name: 'companyAddress',
            id: id,
            value: companyAddress,
          }}
        />
      </td>
      <td className="flex items-center justify-center">
        <button
          className="rounded-md bg-red-500 p-2 text-white shadow-sm transition-colors duration-200 hover:bg-red-600"
          onClick={deleteCustomerHandler}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            />
          </svg>
        </button>
      </td>
    </tr>
  );
};

export default Customer;
