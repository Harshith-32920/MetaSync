import React, { useState } from 'react';
import { Button, Select, MenuItem } from '@mui/material';
import axios from 'axios';

export const IntegrationForm = () => {
  const [provider, setProvider] = useState('airtable');

  const handleConnect = async () => {
    const formData = new FormData();
    formData.append('user_id', 'test_user');
    formData.append('org_id', 'test_org');

    const res = await axios.post(`http://localhost:8000/integrations/${provider}/authorize`, formData);
    const popup = window.open(res.data.auth_url, 'OAuth', 'width=600,height=700');
    
    const timer = setInterval(() => {
      if (popup.closed) {
        clearInterval(timer);
        console.log('Authorization complete');
      }
    }, 1000);
  };

  return (
    <div style={{ marginBottom: 20 }}>
      <Select value={provider} onChange={(e) => setProvider(e.target.value)}>
        <MenuItem value="airtable">Airtable</MenuItem>
        <MenuItem value="notion">Notion</MenuItem>
        <MenuItem value="hubspot">HubSpot</MenuItem>
      </Select>
      <Button variant="contained" onClick={handleConnect} style={{ marginLeft: 10 }}>Connect</Button>
    </div>
  );
};
