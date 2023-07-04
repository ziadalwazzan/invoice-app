import React from 'react';
import {Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from "react-router-dom";
import Root from "./Root";
import Invoice from "./pages/Invoice";
import Qoute from "./pages/Qoute";

const router = createBrowserRouter(createRoutesFromElements(
  <Route path="/" element={ <Root/> } >
    <Route path='Invoice' element={ <Invoice/> } />
    <Route path='Qoute' element={ <Qoute/> } />
  </Route>
))

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
