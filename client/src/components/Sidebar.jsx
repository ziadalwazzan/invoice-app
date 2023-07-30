import React, { useState } from 'react'
import { NavLink } from 'react-router-dom';

const Sidebar = () => {
    const [showSidebar, setShowSidebar] = useState(false);
    // const sideNavRef = useRef(null);

    // useEffect(() => {
    //     // Add event listener to the document object
    //     document.addEventListener('mousedown', handleClickOutside);

    //     // Remove event listener when the component unmounts
    //     return () => {
    //     document.removeEventListener('mousedown', handleClickOutside);
    //     };
    // }, []);

    // function handleClickOutside(event) {
    //     if (sideNavRef.current && !sideNavRef.current.contains(event.target)) {
    //     // Clicked outside the side navigation bar, close it
    //     // Implement your close side navigation bar logic here

    //     // TODO: Review/Refactor closing implementation to use event triggered close
    //     //setShowSidebar(!showSidebar);
    //     }
    // }

    return (
        <div className='Sidebar'>
            { showSidebar ? (
                <button
                    className="fixed left-6 top-10 z-50 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    onClick={() => setShowSidebar(!showSidebar)}
                >
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"> 
                        <path d="M15.59 7L12 10.59L8.41 7L7 8.41L10.59 12L7 15.59L8.41 17L12 13.41L15.59 17L17 15.59L13.41 12L17 8.41L15.59 7Z" fill="white"/> 
                    </svg>
                </button>
                ) : (
                <button onClick={ () => { setShowSidebar(!showSidebar)}} className="fixed top-10 left-6 z-30 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
                    <svg className="w-8 h-8" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path clipRule="evenodd" fillRule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
                    </svg>
                </button>
                )
            }

            <div className={`top-1 left-0 w-[20vw] min-w-[250px] rounded-lg bg-gray-300 pt-20 p-5 text-white fixed h-[99vh] z-40 ease-in-out duration-300 
                ${showSidebar ? "translate-x-1" : "-translate-x-full" }`}>
                    <ul className="space-y-4 font-medium">
                        <li>
                            <NavLink to="/Invoice">
                                <div className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <svg aria-hidden="true" className="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path><path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path></svg>
                                    <span className="ml-3">Invoice</span>
                                </div>
                            </NavLink>
                        </li>
                        <li>
                            <NavLink to="/Qoute">
                                <div className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <svg aria-hidden="true" className="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path><path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path></svg>
                                    <span className="ml-3">Qoute</span>
                                </div>
                            </NavLink>
                        </li>
                        <li>
                            <NavLink to="/Customers">
                                <div className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <svg aria-hidden="true" className="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path><path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path></svg>
                                    <span className="ml-3">Customers</span>
                                </div>
                            </NavLink>
                        </li>
                    </ul>
            </div>
        </div>
    );
};

export default Sidebar;