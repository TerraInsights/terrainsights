import React from 'react';
import { Routes, Route, Link, useLocation } from 'react-router-dom';
import { Leaf } from 'lucide-react';

import LandingPage from './pages/LandingPage';
import AuthPage from './pages/AuthPage';
import DashboardPage from './pages/DashboardPage';
import ProfilePage from './pages/ProfilePage';
import AboutPage from './pages/AboutPage';
import StorePage from './pages/StorePage';
import AgroGuidePage from './pages/AgroGuidePage';
import GovtSchemesPage from './pages/GovtSchemesPage';

function Navbar() {
  const location = useLocation();
  const isActive = (path) => location.pathname === path ? 'active' : '';
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const userName = localStorage.getItem('userName') || 'User';

  const handleLogout = () => {
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('userName');
    window.location.href = '/auth';
  };

  return (
    <nav className="glass" style={{ margin: '1rem 2rem', borderRadius: '1rem', padding: '1rem 2rem' }}>
      <div className="nav-container">
        <Link to="/" className="logo gradient-text">
          <Leaf size={24} color="#10B981" />
          TerraInsights
        </Link>
        <div className="nav-links">
          <Link to="/dashboard" className={`nav-link ${isActive('/dashboard')}`}>Dashboard</Link>
          <Link to="/agroguide" className={`nav-link ${isActive('/agroguide')}`}>AgroGuide</Link>
          <Link to="/schemes" className={`nav-link ${isActive('/schemes')}`}>Govt Schemes</Link>
          <Link to="/store" className={`nav-link ${isActive('/store')}`}>Store</Link>
          <Link to="/about" className={`nav-link ${isActive('/about')}`}>About</Link>
          {isLoggedIn ? (
            <div className="flex items-center gap-4">
              <Link to="/profile" className={`nav-link ${isActive('/profile')}`}>{userName}'s Profile</Link>
              <button onClick={handleLogout} className="btn-secondary" style={{ padding: '0.4rem 1.25rem', borderRadius: '0.5rem' }}>Logout</button>
            </div>
          ) : (
             <Link to="/auth" className="btn-primary" style={{ padding: '0.5rem 1.25rem' }}>Login</Link>
          )}
        </div>
      </div>
    </nav>
  );
}

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/auth" element={<AuthPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/store" element={<StorePage />} />
        <Route path="/agroguide" element={<AgroGuidePage />} />
        <Route path="/schemes" element={<GovtSchemesPage />} />
      </Routes>
    </div>
  );
}

export default App;
