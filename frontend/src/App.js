import React, { useState } from 'react';

function App() {
  const [url, setUrl] = useState('');
  const [selectedFunction, setSelectedFunction] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const functions = [
    { value: 'detect_cms', label: 'Detect CMS' },
    { value: 'detect_backend_framework', label: 'Detect Backend Framework' },
    { value: 'detect_js_libraries', label: 'Detect JavaScript Libraries' },
    { value: 'detect_web_server', label: 'Detect Web Server' },
    { value: 'analyze_ssl_fingerprint', label: 'Analyze SSL/TLS Fingerprint' },
    { value: 'analyze_api_paths', label: 'Analyze API Paths' },
    { value: 'all', label: 'Run All Functions' },
  ];

  const handleRun = async () => {
    if (!url || !selectedFunction) {
      alert('Please enter a URL and select a function.');
      return;
    }

    setLoading(true);
    setResult('');
    try {
      const response = await fetch('http://localhost:5000/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, function: selectedFunction }),
      });
      const data = await response.json();
      setResult(data.result || 'No result returned');
    } catch (error) {
      setResult('Error: ' + error.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Web Detection Tool</h1>
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          placeholder="Enter URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ width: '300px', padding: '10px' }}
        />
      </div>
      <div style={{ marginBottom: '20px' }}>
        <select
          value={selectedFunction}
          onChange={(e) => setSelectedFunction(e.target.value)}
          style={{ padding: '10px', width: '320px' }}
        >
          <option value="">Select a Function</option>
          {functions.map((func) => (
            <option key={func.value} value={func.value}>
              {func.label}
            </option>
          ))}
        </select>
      </div>
      <button onClick={handleRun} style={{ padding: '10px 20px', cursor: 'pointer' }}>
        Run
      </button>
      {loading && <p>Loading...</p>}
      {result && (
        <div style={{ marginTop: '20px', textAlign: 'left' }}>
          <h2>Result:</h2>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
