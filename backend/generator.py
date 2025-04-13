from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

# Load the model once when the app starts
print("⏳ Loading Stable Diffusion pipeline...")
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
pipe.safety_checker = None  # Disable NSFW checker (optional)
print("✅ Model loaded successfully!")

# Create output directory if not exists
OUTPUT_DIR = "static/generated"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_image(prompt: str) -> str:
    print(f"🖌️ Generating image for prompt: '{prompt}'")

    # Generate image using the prompt
    image = pipe(prompt).images[0]

    # Save image to disk with a unique filename
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    image.save(filepath)

    # Return relative path to the image (used in frontend/backend response)
    return f"/{filepath.replace(os.sep, '/')}"
