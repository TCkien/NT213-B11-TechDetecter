import React, { useState } from 'react';

function App() {
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRunScenario = async (scenario) => {
    setLoading(true);
    setResult(''); // Reset result
    try {
      const response = await fetch(`http://localhost:5000/run/${scenario}`);
      const data = await response.json();
      setResult(data.result || 'No result returned');
    } catch (error) {
      setResult('Error running the scenario: ' + error.message);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Web Detector App</h1>
      <p>Select a scenario to run:</p>
      <div style={{ margin: '20px' }}>
        <button onClick={() => handleRunScenario('scenario1')}>Run Scenario 1</button>
        <button onClick={() => handleRunScenario('scenario2')}>Run Scenario 2</button>
        <button onClick={() => handleRunScenario('scenario3')}>Run Scenario 3</button>
        <button onClick={() => handleRunScenario('scenario4')}>Run Scenario 4</button>
        <button onClick={() => handleRunScenario('scenario5')}>Run Scenario 5</button>
        <button onClick={() => handleRunScenario('scenario6')}>Run Scenario 6</button>
        <button onClick={() => handleRunScenario('all')}>Run All Scenarios</button>
      </div>
      {loading && <p>Loading...</p>}
      {result && (
        <div>
          <h2>Result:</h2>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
