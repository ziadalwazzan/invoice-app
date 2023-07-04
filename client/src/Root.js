import React from "react";
import Sidebar from './components/Sidebar';
import { Outlet } from "react-router-dom";

const Root = () => {
  return (
    <div className="root">
      <Sidebar />
      <div className="rootContainer">
        <Outlet/>
      </div>
    </div>
  );
};
 
export default Root;