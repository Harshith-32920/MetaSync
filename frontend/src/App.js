import React from 'react';
import { IntegrationForm } from './integration-form';
import { DataForm } from './data-form';

export default function App() {
  return (
    <div style={{ padding: 24 }}>
      <h1>SaaS Integration Portal</h1>
      <IntegrationForm />
      <DataForm />
    </div>
  );
}
