import React from 'react';

const CustomerField = ({ cellData }) => {
  return (
      <div 
        className={cellData.className}
        name={cellData.name}
        id={cellData.id}
      >
        {cellData.value}
        </div>
  );
};

export default CustomerField;
