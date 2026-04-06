import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    // Simulate an API call
    setTimeout(() => {
      setLoading(false);
      localStorage.setItem('isLoggedIn', 'true');
      localStorage.setItem('userName', isLogin ? email.split('@')[0] : name);
      // Proceed to dashboard and force reload to update Navbar state
      window.location.href = '/dashboard';
    }, 1000);
  };

  const toggleAuthMode = () => {
    setIsLogin(!isLogin);
    // Reset fields on toggle
    setEmail('');
    setPassword('');
    setName('');
  };

  return (
    <div className="page-wrapper animate-fade-in flex justify-center items-center" style={{ minHeight: '80vh' }}>
      <div className="glass" style={{ padding: '3rem', maxWidth: '400px', width: '100%' }}>
        <h2 className="text-center gradient-text">{isLogin ? 'Welcome Back' : 'Create Account'}</h2>
        <p className="text-center text-muted" style={{ marginBottom: '2rem' }}>
          {isLogin ? 'Enter your details to login.' : 'Sign up for sustainable insights.'}
        </p>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          {!isLogin && (
            <input 
              type="text" 
              placeholder="Full Name" 
              className="input-field" 
              value={name} 
              onChange={(e) => setName(e.target.value)} 
              required 
            />
          )}
          <input 
            type="email" 
            placeholder="Email Address" 
            className="input-field" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            required 
          />
          <input 
            type="password" 
            placeholder="Password" 
            className="input-field" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          />
          
          <button type="submit" className="btn-primary" style={{ width: '100%', marginTop: '1rem' }} disabled={loading}>
            {loading ? 'Processing...' : (isLogin ? 'Login' : 'Sign Up')}
          </button>
        </form>

        <p className="text-center" style={{ marginTop: '1.5rem', fontSize: '0.9rem' }}>
          {isLogin ? "Don't have an account? " : "Already have an account? "}
          <span 
            className="gradient-text" 
            style={{ fontWeight: 600, cursor: 'pointer' }}
            onClick={toggleAuthMode}
          >
            {isLogin ? 'Sign up' : 'Login'}
          </span>
        </p>
      </div>
    </div>
  );
}
