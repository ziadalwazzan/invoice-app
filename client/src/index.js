import React from 'react';
import ReactDOM from 'react-dom';
//import {createRoot} from 'react-dom/client';
import './index.css';
import App from './App';

/* NEW way of rendering for react 18
const rootElement = document.getElementById('root');
const root = createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
*/

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
