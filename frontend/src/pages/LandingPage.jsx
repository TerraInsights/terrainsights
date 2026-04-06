import React from 'react';
import { Link } from 'react-router-dom';
import { Sprout, TrendingUp, ShieldCheck } from 'lucide-react';

export default function LandingPage() {
  return (
    <div className="page-wrapper animate-fade-in text-center">
      <div className="container" style={{ padding: '4rem 2rem' }}>
        <h1 className="gradient-text">Sustainable Fertilizer Optimization</h1>
        <p className="text-xl">Boost your crop yield while protecting the environment with data-driven AI recommendations.</p>
        <div className="flex justify-center gap-4" style={{ marginTop: '2rem' }}>
          <Link to="/auth" className="btn-primary">Get Started</Link>
          <Link to="/about" className="btn-secondary">Learn More</Link>
        </div>

        <div className="grid grid-cols-3 gap-8" style={{ marginTop: '5rem' }}>
          <div className="glass hover-lift" style={{ padding: '2rem' }}>
            <Sprout size={48} color="#10B981" style={{ margin: '0 auto 1rem' }} />
            <h3>Data-Driven Growth</h3>
            <p className="text-muted">Analyze soil health and weather to pick the perfect fertilizer for your specific crop type.</p>
          </div>
          <div className="glass hover-lift" style={{ padding: '2rem' }}>
            <TrendingUp size={48} color="#3B82F6" style={{ margin: '0 auto 1rem' }} />
            <h3>Increase Yield & Income</h3>
            <p className="text-muted">Avoid over-fertilization, reduce costs, and maximize your farm's productivity and revenue.</p>
          </div>
          <div className="glass hover-lift" style={{ padding: '2rem' }}>
            <ShieldCheck size={48} color="#F59E0B" style={{ margin: '0 auto 1rem' }} />
            <h3>Sustainable Future</h3>
            <p className="text-muted">Protect soil health and the environment by using exact and optimized nutrient blends.</p>
          </div>
        </div>
      </div>
    </div>
  );
}
