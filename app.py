from flask import Flask, request, jsonify, send_file
from backgroundremover.bg import remove
import os
from PIL import Image
import io

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return "✅ Background Remover API is running!"

    @app.route("/remove", methods=["POST"])
    def remove_bg():
        if "image" not in request.files:
                return jsonify({"error": "No image uploaded"}), 400

                    file = request.files["image"]
                        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
                            output_path = os.path.join(OUTPUT_FOLDER, f"no_bg_{file.filename}")

                                # Save uploaded image
                                    file.save(input_path)

                                        # Read image and remove background
                                            with open(input_path, "rb") as i:
                                                    input_data = i.read()
                                                            output_data = remove(input_data)

                                                                # Save output
                                                                    with open(output_path, "wb") as out:
                                                                            out.write(output_data)

                                                                                return send_file(output_path, mimetype="image/png")

                                                                                if __name__ == "__main__":
                                                                                    import os
                                                                                        port = int(os.environ.get("PORT", 5000))
                                                                                            app.run(host="0.0.0.0", port=port)