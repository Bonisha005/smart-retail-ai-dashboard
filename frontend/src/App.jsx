import React, { useEffect, useState } from "react"

function App() {
  const [forecast, setForecast] = useState(null)
  const [inventory, setInventory] = useState(null)

  useEffect(() => {
    fetch("http://localhost:5000/forecast")
      .then(res => res.json())
      .then(data => setForecast(data.predicted_demand))

    fetch("http://localhost:5000/inventory")
      .then(res => res.json())
      .then(data => setInventory(data))
  }, [])

  return (
    <div style={{
      minHeight: "100vh",
      backgroundColor: "#f3f4f6",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>
      <div style={{
        backgroundColor: "white",
        padding: "30px",
        borderRadius: "12px",
        width: "320px"
      }}>
        <h2>Smart Retail AI Dashboard</h2>

        <p><strong>Predicted Demand:</strong></p>
        <h3>{forecast ? forecast + " units" : "Loading..."}</h3>

        {inventory && (
          <>
            <p>Current Stock: {inventory.current_stock}</p>
            <p><strong>{inventory.recommendation}</strong></p>
          </>
        )}
      </div>
    </div>
  )
}

export default App
