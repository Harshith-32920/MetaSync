import React, { useState } from 'react';
import { Button, TextField } from '@mui/material';
import axios from 'axios';

export const DataForm = () => {
  const [items, setItems] = useState([]);

  const handleFetchData = async () => {
    const res = await axios.post('http://localhost:8000/integrations/airtable/items', { credentials: 'test' });
    setItems(res.data);
  };

  return (
    <div>
      <Button variant="outlined" onClick={handleFetchData}>Fetch Integration Items</Button>
      <pre>{JSON.stringify(items, null, 2)}</pre>
    </div>
  );
};
