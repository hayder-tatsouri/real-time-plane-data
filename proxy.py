from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Wide bbox: all of Tunisia + Mediterranean + neighbors
LAMIN, LAMAX = 30, 38
LOMIN, LOMAX = 7, 13

@app.route("/flights")
def flights():
    url = (
        f"https://opensky-network.org/api/states/all?"
        f"lamin={LAMIN}&lomin={LOMIN}&lamax={LAMAX}&lomax={LOMAX}"
    )
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        states = data.get("states") or []

        planes = []
        for s in states:
            if s[6] is None or s[5] is None:
                continue
            planes.append({
                "icao":      s[0],
                "callsign":  (s[1] or "").strip(),
                "country":   s[2] or "—",
                "lon":       s[5],
                "lat":       s[6],
                "alt":       s[7],
                "on_ground": s[8],
                "velocity":  s[9],
                "heading":   s[10],
                "vert_rate": s[11],
                "squawk":    s[14],
            })

        return jsonify({"ok": True, "planes": planes, "count": len(planes)})

    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    print(f"Bbox: {LAMIN}–{LAMAX}°N, {LOMIN}–{LOMAX}°E")
    print("Proxy running at http://localhost:5050/flights")
    app.run(port=5050, threaded=True)