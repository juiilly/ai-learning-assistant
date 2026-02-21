"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [url, setUrl] = useState("");

  const processVideo = async () => {
    try {
      await axios.post(
        "https://shiny-space-dollop-977765xrj4q4f779q-8000.app.github.dev/process-video",
        null,
        { params: { url } }
      );
      alert("Video processed!");
    } catch (error) {
      alert("Backend error");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>YouTube RAG Processor</h1>

        <input
          type="text"
          placeholder="Paste YouTube URL here..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={styles.input}
        />

        <button onClick={processVideo} style={styles.button}>
          Process
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f3f4f6",
  },
  card: {
    padding: "40px",
    backgroundColor: "white",
    borderRadius: "12px",
    boxShadow: "0 10px 25px rgba(0,0,0,0.1)",
    width: "400px",
    textAlign: "center" as const,
  },
  title: {
    marginBottom: "20px",
  },
  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "20px",
    borderRadius: "6px",
    border: "1px solid #ccc",
  },
  button: {
    width: "100%",
    padding: "10px",
    borderRadius: "6px",
    border: "none",
    backgroundColor: "#2563eb",
    color: "white",
    cursor: "pointer",
  },
};