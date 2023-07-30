import React from 'react';
import {Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from "react-router-dom";

import Root from "./Root";
import Invoice from "./components/InvoiceForm";
import Qoute from "./components/QouteForm";
import Customers from "./components/Customers";

const router = createBrowserRouter(createRoutesFromElements(
  <Route path="/" element={ <Root/> } >
    <Route path='Invoice' element={ <Invoice/> } />
    <Route path='Qoute' element={ <Qoute/> } />
    <Route path='Customers' element={ <Customers/> } />
  </Route>
))

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
