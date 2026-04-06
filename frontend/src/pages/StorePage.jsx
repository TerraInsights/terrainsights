import React from 'react';
import { ShoppingCart } from 'lucide-react';

export default function StorePage() {
  const products = [
    { id: 1, name: 'Urea (Nitrogen 46%)', price: '₹1,500/bag', type: 'Urea' },
    { id: 2, name: 'DAP (18-46-0)', price: '₹2,200/bag', type: 'DAP' },
    { id: 3, name: 'MOP (Potassium 60%)', price: '₹2,600/bag', type: 'MOP' },
    { id: 4, name: 'Compost Mix', price: '₹1,100/bag', type: 'Compost' },
  ];

  return (
    <div className="page-wrapper container animate-fade-in">
      <h2>Fertilizer Store</h2>
      <div className="grid grid-cols-4 gap-4" style={{ marginTop: '2rem' }}>
        {products.map(p => (
          <div key={p.id} className="glass hover-lift flex flex-col justify-between" style={{ padding: '1.5rem' }}>
            <div>
              <h3 style={{ fontSize: '1.2rem' }}>{p.name}</h3>
              <p className="gradient-text" style={{ fontSize: '1.1rem', fontWeight: 'bold' }}>{p.price}</p>
            </div>
            <button className="btn-secondary flex items-center justify-center gap-2" style={{ marginTop: '1rem', padding: '0.5rem' }}>
              <ShoppingCart size={16} /> Add to Cart
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
