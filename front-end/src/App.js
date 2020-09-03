import React from 'react';
import logo from './logo.svg';
import Nav from './Components/Navbar/Navbar';
import Dashboard from './Components/Dashboard/Dashboard'
import CssBaseline from '@material-ui/core/CssBaseline';
import './App.css';

function App() {
  return (
    <div className="App">
    <CssBaseline />
      <Nav />
      <Dashboard />
    </div>
  );
}

export default App;
