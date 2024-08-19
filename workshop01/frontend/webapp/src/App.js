import logo from './dog.jpg';
import React, { useState, useEffect } from "react";
import './App.css';

function App() {
  const [line, setLine] = useState("Temp")

  useEffect(() => {
    fetch('/line').then(res => res.json()).then(data => {
        setLine(data['sentence'])
    })
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p> The dog says: </p>
        <p>
            {line}
        </p>
        <a
          className="App-link"
          href="https://github.com/KeithCZW/myrepo"
          target="_blank"
          rel="noopener noreferrer"
        >
          https://github.com/KeithCZW/myrepo
        </a>
      </header>
    </div>
  );
}

export default App;
