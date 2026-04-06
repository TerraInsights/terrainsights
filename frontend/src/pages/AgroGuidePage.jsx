import React, { useState } from 'react';
import { BookOpen } from 'lucide-react';

export default function AgroGuidePage() {
  const guides = [
    { title: 'Best Practices for Loamy Soil', category: 'soil' },
    { title: 'Wheat Seed Selection 2024', category: 'seeds' },
    { title: 'Organic Composting Methods', category: 'sustainable' },
    { title: 'Drip Irrigation Techniques', category: 'sustainable' },
    { title: 'Optimizing Nitrogen Intake', category: 'fertilizer' }
  ];

  const [filter, setFilter] = useState('all');
  const filtered = filter === 'all' ? guides : guides.filter(g => g.category === filter);

  return (
    <div className="page-wrapper container animate-fade-in">
      <h2>AgroGuide Learning Center</h2>
      <div className="flex gap-4" style={{ marginBottom: '2rem', flexWrap: 'wrap' }}>
        <button onClick={() => setFilter('all')} className={filter === 'all' ? 'btn-primary' : 'btn-secondary'}>All</button>
        <button onClick={() => setFilter('soil')} className={filter === 'soil' ? 'btn-primary' : 'btn-secondary'}>Soil</button>
        <button onClick={() => setFilter('seeds')} className={filter === 'seeds' ? 'btn-primary' : 'btn-secondary'}>Seeds</button>
        <button onClick={() => setFilter('fertilizer')} className={filter === 'fertilizer' ? 'btn-primary' : 'btn-secondary'}>Fertilizer</button>
        <button onClick={() => setFilter('sustainable')} className={filter === 'sustainable' ? 'btn-primary' : 'btn-secondary'}>Sustainable</button>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {filtered.map((g, idx) => (
          <div key={idx} className="glass flex gap-4 hover-lift" style={{ padding: '1.5rem', alignItems: 'center' }}>
            <div style={{ background: 'var(--border-glass)', padding: '1rem', borderRadius: '0.5rem' }}>
              <BookOpen size={24} color="var(--primary)" />
            </div>
            <div>
              <h3>{g.title}</h3>
              <p className="text-muted" style={{ textTransform: 'capitalize' }}>Category: {g.category}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
