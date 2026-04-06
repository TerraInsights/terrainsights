import React from 'react';

export default function ProfilePage() {
  return (
    <div className="page-wrapper container animate-fade-in">
      <h2>User Profile</h2>
      <div className="glass" style={{ padding: '2rem', maxWidth: '600px' }}>
        <p><strong>Name:</strong> John Doe</p>
        <p><strong>Email:</strong> john@example.com</p>
        <p><strong>Farm Location:</strong> North Region</p>
        <p><strong>Preferred Crop:</strong> Wheat</p>
        <button className="btn-secondary" style={{ marginTop: '1rem' }}>Edit Profile</button>
      </div>
    </div>
  );
}
