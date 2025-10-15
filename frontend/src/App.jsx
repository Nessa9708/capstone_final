import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";

function Nav({ user }) {
  return (
    <div style={{background:"#00c0c7", padding:"14px"}}>
      <span style={{fontWeight:"bold", fontSize:22, marginRight:20}}>Dealerships</span>
      <Link to="/" style={{marginRight:12}}>Home</Link>
      <Link to="/about" style={{marginRight:12}}>About Us</Link>
      <Link to="/contact" style={{marginRight:12}}>Contact Us</Link>
      <span style={{float:"right"}}>
        {user ? (
          <>
            <span style={{marginRight:12}}>{user}</span>
            <a href={`/logout/?u=${encodeURIComponent(user)}`}>Logout</a>
          </>
        ) : (
          <>
            <Link to="/login" style={{marginRight:12}}>Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </span>
    </div>
  );
}

function Home() {
  const [user,setUser] = useState(sessionStorage.getItem("username") || "");
  useEffect(() => setUser(sessionStorage.getItem("username") || ""), []);
  return (
    <div style={{padding:"16px"}}>
      <Nav user={user} />
      <h2>Welcome to our Dealerships!</h2>
    </div>
  );
}
function About() {
  const user = sessionStorage.getItem("username");
  return (
    <div style={{padding:"16px"}}>
      <Nav user={user} />
      <h2>About Us</h2>
      <p>Best Cars dealership — domestic &amp; imported cars at reasonable prices.</p>
    </div>
  );
}
function Contact() {
  const user = sessionStorage.getItem("username");
  return (
    <div style={{padding:"16px"}}>
      <Nav user={user} />
      <h2>Contact Us</h2>
      <ul>
        <li>Email: support@bestcars.com</li>
        <li>Phone: 312-611-1111</li>
      </ul>
    </div>
  );
}

function Login() {
  const nav = useNavigate();
  const [username,setUsername] = useState("");
  const [password,setPassword] = useState("");
  const doLogin = (e) => {
    e.preventDefault();
    sessionStorage.setItem("username", username || "root");
    nav("/");
    window.location.reload();
  };
  const user = sessionStorage.getItem("username");
  return (
    <div style={{padding:"16px"}}>
      <Nav user={user} />
      <h2>Login</h2>
      <form onSubmit={doLogin}>
        <div><label>Username</label><br/><input value={username} onChange={e=>setUsername(e.target.value)} /></div>
        <div style={{marginTop:8}}><label>Password</label><br/><input type="password" value={password} onChange={e=>setPassword(e.target.value)} /></div>
        <div style={{marginTop:12}}><button type="submit">Login</button></div>
      </form>
      <p style={{marginTop:10}}><Link to="/register">Register Now</Link></p>
    </div>
  );
}

function Register() {
  const nav = useNavigate();
  const [username,setUsername] = useState("");
  const [first,setFirst] = useState("");
  const [last,setLast] = useState("");
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const doRegister = (e) => {
    e.preventDefault();
    sessionStorage.setItem("username", username || "newuser");
    nav("/");
    window.location.reload();
  };
  const user = sessionStorage.getItem("username");
  return (
    <div style={{padding:"16px"}}>
      <Nav user={user} />
      <h2>SignUp</h2>
      <form onSubmit={doRegister}>
        <div><input placeholder="First Name" value={first} onChange={e=>setFirst(e.target.value)} /></div>
        <div><input placeholder="Last Name"  value={last}  onChange={e=>setLast(e.target.value)} /></div>
        <div><input placeholder="email"      value={email} onChange={e=>setEmail(e.target.value)} /></div>
        <div><input placeholder="Username"   value={username} onChange={e=>setUsername(e.target.value)} /></div>
        <div><input placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} /></div>
        <div style={{marginTop:8}}><button type="submit">Register</button></div>
      </form>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/about" element={<About/>} />
        <Route path="/contact" element={<Contact/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
      </Routes>
    </BrowserRouter>
  );
}
