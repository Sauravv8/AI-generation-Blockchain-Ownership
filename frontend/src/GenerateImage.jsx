import { useState } from "react";
import axios from "axios";

export default function GenerateImage() {
  const [prompt, setPrompt] = useState("");
  const [imageURL, setImageURL] = useState("");

  const handleGenerate = async () => {
    const res = await axios.post("http://localhost:5000/generate", { prompt });
    setImageURL("http://localhost:5000" + res.data.image_url);
  };

  return (
    <div>
      <input value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="Enter prompt" />
      <button onClick={handleGenerate}>Generate Image</button>
      {imageURL && <img src={imageURL} alt="Generated" style={{ maxWidth: 300 }} />}
    </div>
  );
}
