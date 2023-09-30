import React, { useState } from 'react';

function App() {
  const [cityName, setCityName] = useState('');
  const [cityData, setCityData] = useState(null);

  const handleCityNameChange = (event) => {
    setCityName(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('/generate_city_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city_name: cityName }),
      });

      if (response.ok) {
        const data = await response.json();
        setCityData(data);
      } else {
        throw new Error('Failed to fetch data');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>City Data Generator</h1>
      <form onSubmit={handleSubmit}>
        <label>
          City Name:
          <input
            type="text"
            value={cityName}
            onChange={handleCityNameChange}
          />
        </label>
        <button type="submit">Generate Data</button>
      </form>
      {cityData && (
        <div>
          <h2>Generated City Data:</h2>
          <pre>{JSON.stringify(cityData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
