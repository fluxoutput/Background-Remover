from flask import Flask, request, jsonify, send_file
import os
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Background Remover API (rembg) is running!"

    @app.route("/remove", methods=["POST"])
    def remove_bg():
        if "image" not in request.files:
                return jsonify({"error": "No image uploaded"}), 400

                    file = request.files["image"]
                        img = Image.open(file.stream)

                            output = remove(img)

                                img_io = io.BytesIO()
                                    output.save(img_io, format="PNG")
                                        img_io.seek(0)

                                            return send_file(img_io, mimetype="image/png")

                                            if __name__ == "__main__":
                                                import os
                                                    port = int(os.environ.get("PORT", 5000))
                                                        app.run(host="0.0.0.0", port=port)