import React, { useEffect, useState } from "react";

export default function Dealers() {
  const [rows, setRows] = useState([]);
  const [stateFilter, setStateFilter] = useState("All");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState("");

  // Load on first render + whenever stateFilter changes
  useEffect(() => {
    let cancelled = false;

    (async () => {
      try {
        setErr("");
        setLoading(true);

        const url =
          stateFilter === "All"
            ? "/api/get_dealers"
            : `/api/get_dealers/${encodeURIComponent(stateFilter)}`;

        const res = await fetch(url, { credentials: "include" });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);

        const data = await res.json(); // backend returns { dealers: [...] }
        if (!cancelled) setRows(data.dealers || []);
      } catch (e) {
        if (!cancelled) setErr(e.message || "Failed to load dealers");
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [stateFilter]);

  return (
    <div style={{ padding: "16px" }}>
      <h2>Dealerships</h2>

      <label>
        Filter by State:{" "}
        <select
          value={stateFilter}
          onChange={(e) => setStateFilter(e.target.value)}
        >
          <option value="All">All</option>
          <option value="TX">Texas</option>
          <option value="FL">Florida</option>
          <option value="KS">Kansas</option>
        </select>
      </label>

      {loading ? (
        <p>Loading...</p>
      ) : err ? (
        <p style={{ color: "red" }}>Error: {err}</p>
      ) : (
        <table border="1" cellPadding="8" style={{ marginTop: "16px" }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Dealer Name</th>
              <th>City</th>
              <th>Address</th>
              <th>Zip</th>
              <th>State</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.id}>
                <td>{row.id}</td>
                <td>{row.full_name}</td>
                <td>{row.city}</td>
                <td>{row.address}</td>
                <td>{row.zip}</td>
                <td>{row.state}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}