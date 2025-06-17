from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/download", methods=["POST"])
def download_video():
    data = request.get_json()
    video_url = data.get("url")
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    # Dummy response (replace with actual downloader logic)
    return jsonify({
        "download": video_url,
        "stream": video_url
    })

if __name__ == "__main__":
    app.run(debug=True)
