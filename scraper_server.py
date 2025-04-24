from flask import Flask, request, jsonify
import subprocess
import threading
import time

app = Flask(__name__)

SCRAPER_PATH = "multi_scraper_searay.py"
DELAY = 5

def run_scraper():
    time.sleep(DELAY)
    subprocess.run(["python", SCRAPER_PATH], shell=True)

@app.route("/webhook-scraper", methods=["POST"])
def launch_scraper():
    data = request.get_json()
    print("🔁 Datos recibidos:", data)

    thread = threading.Thread(target=run_scraper)
    thread.start()

    return jsonify({
        "status": "scraper ejecutado",
        "message": "Scraper lanzado en segundo plano"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
