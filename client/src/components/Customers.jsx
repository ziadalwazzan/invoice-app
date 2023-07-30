import React, { useEffect, useState } from 'react';
import Customer from './Customer';
import AddCustomerModal from './AddCustomerModal';
import axios from 'axios';

const Customers = () => {
  const [loading, setLoading] = useState(true);
  const [customerFilter, setCustomerFilter] = useState('');
  const [customers, setCustomers] = useState([]);
  const [data, setData] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);

  // fetch Customers list from flask API
  const fetchCustomers = () => {
    axios.get(
      'http://127.0.0.1:5000/customers',
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
      setCustomers(response.data);
    })
    .catch(e => {
      console.log('error: ', e);
    })
    .finally( () => {
      setLoading(false);
    });
  };

  useEffect( () => {
    fetchCustomers();
    setData(customers);
  }, [customers.length]);

  const addCustomerHandler = (newCustomer) => {
    setCustomers( customers => [...customers, newCustomer]);
  };

  // On delete: Delete customer request to API. Upon successful request => update customers list
  const deleteCustomerHandler = (c_id) => {
    axios.delete(
      'http://127.0.0.1:5000/customers/delete',
      { params: {'c_id': c_id} },
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
      setCustomers((prevCustomer) => prevCustomer.filter((customer) => customer.c_id !== c_id));
    })
    .catch(error => {
      if (error.response) {
        console.error('Server Error:', error.response.status);
      } else if (error.request) {
        console.error('Network Error:', error.request);
      } else {
        console.error('Error:', error.message);
      }
    })
  };

  // handle change event of search input
  const handleFilterChange = value => {
    setCustomerFilter(value);
    filterData(value);
  };

  // filter records by search text
  const filterData = (value) => {
    const lowercasedValue = value.toLowerCase().trim();
    if (lowercasedValue === "") setData(customers);
    else {
      const filteredData = customers.filter(item => {
        return Object.keys(item).some(key =>
          item[key].toString().toLowerCase().includes(lowercasedValue)
        );
      });
      setData(filteredData);
    }
  }

  return (
    <div className="Customers flex flex-col p-2">
      <div className="flex flex-row justify-end gap-2 pt-8 pb-6">
        <input
          className="text-sm md:text-base w-[30vw] min-w-[140px] bg-gray-50"
          placeholder="Customer Search"
          type="text"
          name="customerFilter"
          id="customerFilter"
          value={customerFilter}
          onChange={event => handleFilterChange(event.target.value)}
        />
        <button
          className="w-[30vw] rounded-md bg-blue-500 text-sm text-white shadow-sm hover:bg-blue-600"
          type="button"
          onClick={ () => { setModalIsOpen(true) }
          }
        >
          Add Contact
        </button>
        <AddCustomerModal
        isOpen = {modalIsOpen}
        setIsOpen = {setModalIsOpen}
        onAddCustomer = {addCustomerHandler}
        />
      </div>
      <div className='bg-gray-50 rounded py-5 px-5 overflow-x-scroll'>
        <table className="w-full p-4 text-left">
          <thead>
            <tr className="border-b border-gray-900/10 text-sm md:text-base">
              <th>Name</th>
              <th>Phone</th>
              <th className="text-left">E-mail</th>
              <th className="text-left">Company Name</th>
              <th className="text-left">Company Address</th>
              <th className="text-left">Delete</th>
            </tr>
          </thead>
          <tbody>
            {data.map((customer) => (
              <Customer
                key={customer.c_id}
                id={customer.c_id}
                customerName={customer.customerName}
                customerPhone={customer.customerPhone}
                customerEmail={customer.customerEmail}
                companyName={customer.companyName}
                companyAddress={customer.companyAddress}
                onDeleteCustomer={deleteCustomerHandler}
              />
            ))}
          </tbody>
        </table>
        {loading && <p>Getting customers from API...</p>}
        <div className="clearboth"></div>
        {data.length === 0 && <span>No records found to display!</span>}
      </div>
    </div>
  );
};

export default Customers;
