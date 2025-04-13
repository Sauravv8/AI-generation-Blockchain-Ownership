from flask import Flask, request, jsonify, render_template
from generator import generate_image

app = Flask(__name__)

# 🔁 Serve the frontend HTML page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# 🎯 Endpoint to handle image generation requests
@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt", "")
    image = request.files.get("image")  # Optional user image input

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # You can modify `generate_image()` to accept the image if needed
    image_url = generate_image(prompt)
    return jsonify({"image_url": image_url})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
