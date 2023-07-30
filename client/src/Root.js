import React from "react";
import { Outlet } from "react-router-dom";

import Sidebar from './components/Sidebar';

const Root = () => {
  return (
    <div className="min-h-screen bg-gray-100 mx-auto">
      <Sidebar/>
      <Outlet/>
    </div>
  );
};
 
export default Root;