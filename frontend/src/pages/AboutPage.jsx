import React from 'react';

export default function AboutPage() {
  return (
    <div className="page-wrapper container animate-fade-in">
      <h2>About TerraInsights</h2>
      <div className="glass" style={{ padding: '2rem' }}>
        <p style={{ marginBottom: '1rem' }}>Excessive and improper use of fertilizers leads to soil degradation and reduced agricultural productivity.</p>
        <p>This data-driven solution analyzes soil health, crop types, and weather patterns to recommend optimal fertilizer usage.</p>
      </div>
    </div>
  );
}
