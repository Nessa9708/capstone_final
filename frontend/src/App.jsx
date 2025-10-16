import React from "react";                    // <-- add this line
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Dealers from "./components/Dealers/Dealers";

function Home() {
  return (
    <div style={{ padding: 16 }}>
      <h2>Home</h2>
      <p>Go to Dealers to view the list.</p>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
    <nav style={{ padding: "8px 12px" }}>
  <Link to="/">Home</Link>{" | "}
  <Link to="/dealers">Dealers</Link>{" | "}
  {/* These hit Django via the Vite proxy */}
  <a href="/api/login?next=/dealers" style={{ marginLeft: 8 }}>Login</a>{" | "}
  <a href="/api/logout?next=/dealers" style={{ marginLeft: 8 }}>Logout</a>
</nav>

      <Routes>
        <Route path="/" element={<div />} />
        <Route path="/dealers" element={<Dealers />} />
      </Routes>
    </BrowserRouter>
  );
}
