import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null); 

  const { actions } = useContext(Context);

  const handleLogin = async (e) => {
    e.preventDefault();

   
    try {
      const success = await actions.login(email, password);

      if (success) {
        
        setEmail("");
        setPassword("");
      } else {
        setError("Invalid email or password"); 
      }
    } catch (error) {
      setError("An error occurred"); 
    }
  };

  return (
    <div>
      <nav className="navbar bg-primary" data-bs-theme="dark"></nav>

      <form onSubmit={handleLogin}>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">
            Email
          </label>
          <input
            type="email"
            className="form-control"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            type="password"
            className="form-control"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        {error && <div className="alert alert-danger">{error}</div>}

        <button type="submit" className="btn btn-primary">
          Login
        </button>
      </form>

      <Link to="/">
        <span className="btn btn-primary btn-lg" href="#" role="button">
          Password Recovery

        </span>
      </Link>
    </div>
  );
};

export default Login;
