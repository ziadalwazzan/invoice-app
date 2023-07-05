import React, {useState} from "react";
import Sidebar from './components/Sidebar';
import { Outlet } from "react-router-dom";

const Root = () => {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  return (
    <div className="root">
      <Sidebar sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen}/>
      <div className="rootContainer">
        <Outlet/>
      </div>
    </div>
  );
};
 
export default Root;