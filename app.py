from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io, os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

    @app.route("/remove", methods=["POST"])
    def remove_bg():
        if "image" not in request.files:
                return "No image uploaded", 400

                    image_file = request.files["image"]
                        input_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
                            output_path = os.path.join(OUTPUT_FOLDER, f"no_bg_{image_file.filename}")

                                image_file.save(input_path)

                                    with open(input_path, "rb") as inp:
                                            result = remove(inp.read())

                                                with open(output_path, "wb") as out:
                                                        out.write(result)

                                                            return send_file(output_path, as_attachment=True)

                                                            if __name__ == "__main__":
                                                                app.run(host="0.0.0.0", port=5000)