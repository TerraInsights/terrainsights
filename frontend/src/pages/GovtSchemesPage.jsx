import React from 'react';
import { Landmark } from 'lucide-react';

export default function GovtSchemesPage() {
  const schemes = [
    { name: 'PM-KISAN Samman Nidhi', desc: 'Financial support of ₹6,000 per year to all landholding farmer families.' },
    { name: 'Pradhan Mantri Krishi Sinchayee Yojana', desc: 'Focuses on improving water use efficiency and expanding cultivable land under irrigation.' },
    { name: 'Soil Health Card Scheme', desc: 'Provides farmers with soil nutrient status and recommendations for appropriate dosage of nutrients.' },
    { name: 'Paramparagat Krishi Vikas Yojana', desc: 'Promotes organic farming to improve soil health and increase farmers net income.' }
  ];

  return (
    <div className="page-wrapper container animate-fade-in">
      <h2>Government Schemes & Perks</h2>
      <p className="text-muted" style={{ marginBottom: '2rem' }}>Explore benefits to support your sustainable farming journey.</p>
      
      <div className="grid grid-cols-2 gap-6">
        {schemes.map((s, i) => (
          <div key={i} className="glass hover-lift flex flex-col justify-between" style={{ padding: '1.5rem', borderLeft: '4px solid var(--primary)' }}>
            <div>
              <Landmark size={24} color="var(--secondary)" style={{ marginBottom: '1rem' }} />
              <h3>{s.name}</h3>
              <p className="text-muted">{s.desc}</p>
            </div>
            <button className="btn-secondary" style={{ marginTop: '1.5rem', alignSelf: 'flex-start' }}>Apply Now</button>
          </div>
        ))}
      </div>
    </div>
  );
}
