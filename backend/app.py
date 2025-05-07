from flask import Flask, request, jsonify, render_template
from generator import generate_image

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        prompt = request.form.get("prompt", "")
        image = request.files.get("image")  # Optional

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        print(f"📥 Received prompt: {prompt}")
        if image:
            print(f"🖼️ Received image: {image.filename}")
        
        image_url = generate_image(prompt)  # If you're not passing `image`, that’s okay for now
        print(f"✅ Returning image URL: {image_url}")
        return jsonify({"image_url": image_url})
    
    except Exception as e:
        print(f"🔥 Exception in /generate: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

