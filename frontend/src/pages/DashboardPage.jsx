import React, { useState } from 'react';
import axios from 'axios';
import { Beaker } from 'lucide-react';

export default function DashboardPage() {
  const [formData, setFormData] = useState({
    Temperature: 25, Humidity: 60, Rainfall: 1000, 
    Soil_pH: 6.5, Soil_Moisture: 40, Organic_Carbon: 0.5,
    Electrical_Conductivity: 1.5, Nitrogen_Level: 50,
    Phosphorus_Level: 50, Potassium_Level: 50,
    Soil_Type: 'Loamy', Crop_Type: 'Wheat',
    Crop_Growth_Stage: 'Vegetative', Season: 'Rabi',
    Irrigation_Type: 'Canal', Previous_Crop: 'Rice',
    Region: 'North', Fertilizer_Used_Last_Season: 100,
    Yield_Last_Season: 5.0
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const formattedData = {
        ...formData,
        Temperature: Number(formData.Temperature),
        Humidity: Number(formData.Humidity),
        Rainfall: Number(formData.Rainfall),
        Soil_pH: Number(formData.Soil_pH),
        Soil_Moisture: Number(formData.Soil_Moisture),
        Organic_Carbon: Number(formData.Organic_Carbon),
        Electrical_Conductivity: Number(formData.Electrical_Conductivity),
        Nitrogen_Level: Number(formData.Nitrogen_Level),
        Phosphorus_Level: Number(formData.Phosphorus_Level),
        Potassium_Level: Number(formData.Potassium_Level),
        Fertilizer_Used_Last_Season: Number(formData.Fertilizer_Used_Last_Season),
        Yield_Last_Season: Number(formData.Yield_Last_Season),
      };
      const res = await axios.post('http://localhost:8000/predict', formattedData);
      setResult(res.data.recommended_fertilizer);
    } catch (err) {
      console.error(err);
      setResult('Error connecting to ML model');
    }
    setLoading(false);
  };

  return (
    <div className="page-wrapper container animate-fade-in">
      <h2>Yield Optimization Dashboard</h2>
      <p className="text-muted" style={{ marginBottom: '2rem' }}>Enter your soil and environmental metrics to get a tailored fertilizer recommendation.</p>
      
      <div className="grid grid-cols-2 gap-8" style={{ gridTemplateColumns: '2fr 1fr' }}>
        <div className="glass" style={{ padding: '2rem' }}>
          <h3>Farm Data</h3>
          <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4" style={{ marginTop: '1.5rem' }}>
            <input name="Temperature" placeholder="Temp (°C)" value={formData.Temperature} onChange={handleChange} className="input-field" type="number" step="0.1" title="Temperature"/>
            <input name="Humidity" placeholder="Humidity (%)" value={formData.Humidity} onChange={handleChange} className="input-field" type="number" step="0.1" title="Humidity" />
            <input name="Soil_pH" placeholder="Soil pH" value={formData.Soil_pH} onChange={handleChange} className="input-field" type="number" step="0.1" title="Soil pH" />
            <input name="Nitrogen_Level" placeholder="Nitrogen (N)" value={formData.Nitrogen_Level} onChange={handleChange} className="input-field" type="number" title="Nitrogen" />
            <input name="Phosphorus_Level" placeholder="Phosphorus (P)" value={formData.Phosphorus_Level} onChange={handleChange} className="input-field" type="number" title="Phosphorus" />
            <input name="Potassium_Level" placeholder="Potassium (K)" value={formData.Potassium_Level} onChange={handleChange} className="input-field" type="number" title="Potassium" />
            
            <select name="Soil_Type" value={formData.Soil_Type} onChange={handleChange} className="input-field">
              <option value="Loamy">Loamy</option>
              <option value="Sandy">Sandy</option>
              <option value="Clay">Clay</option>
              <option value="Silt">Silt</option>
            </select>
            
            <select name="Crop_Type" value={formData.Crop_Type} onChange={handleChange} className="input-field">
              <option value="Wheat">Wheat</option>
              <option value="Rice">Rice</option>
              <option value="Maize">Maize</option>
              <option value="Cotton">Cotton</option>
              <option value="Sugarcane">Sugarcane</option>
              <option value="Potato">Potato</option>
              <option value="Tomato">Tomato</option>
            </select>
            
            <select name="Season" value={formData.Season} onChange={handleChange} className="input-field">
              <option value="Rabi">Rabi</option>
              <option value="Kharif">Kharif</option>
              <option value="Zaid">Zaid</option>
            </select>
            
            <input name="Rainfall" placeholder="Rainfall (mm)" value={formData.Rainfall} onChange={handleChange} className="input-field" type="number" />
            <input name="Yield_Last_Season" placeholder="Yield Last Season" value={formData.Yield_Last_Season} onChange={handleChange} className="input-field" type="number" step="0.1" title="Yield Last Season" />
            <input name="Organic_Carbon" placeholder="Organic Carbon" value={formData.Organic_Carbon} onChange={handleChange} className="input-field" type="number" step="0.1" title="Organic Carbon" />

            <button type="submit" className="btn-primary" style={{ gridColumn: 'span 2', marginTop: '1rem' }} disabled={loading}>
              {loading ? 'Analyzing...' : 'Get Recommendation'}
            </button>
          </form>
        </div>

        <div className="glass flex flex-col justify-center items-center text-center" style={{ padding: '2rem', height: 'fit-content', top: '2rem', position: 'sticky' }}>
          <Beaker size={64} color="#10B981" style={{ marginBottom: '1rem' }} />
          <h3>Recommendation</h3>
          {result ? (
            <div className="animate-fade-in" style={{ marginTop: '1rem' }}>
              <span style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--primary)' }}>{result}</span>
              <p className="text-muted" style={{ marginTop: '1rem' }}>This fertilizer is optimal based on your NPK levels, soil type, and weather predictions.</p>
              <a href="/store" className="btn-primary" style={{ display: 'inline-block', marginTop: '1.5rem' }}>View in Store</a>
            </div>
          ) : (
            <p className="text-muted">Enter your data and click Get Recommendation to see the results here.</p>
          )}
        </div>
      </div>
    </div>
  );
}
