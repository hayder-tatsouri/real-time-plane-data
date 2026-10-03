# Real-Time Plane Data

A small live aircraft radar for the Tunisian airspace area. The project uses the OpenSky Network API for flight data, a Flask proxy for local access, and a browser-based radar UI.

## Requirements

- Python 3.9 or newer
- A modern web browser
- Internet access to reach the OpenSky Network API

## Installation

From the project directory, install the Python dependencies:

```powershell
py -m pip install flask flask-cors requests
```

## Run the radar

1. Start the local proxy:

   ```powershell
   py proxy.py
   ```

2. Open `tunis_radar.html` in your browser.

The radar requests flight data through:

```text
http://localhost:5050/flights
```

Keep the proxy terminal running while using the radar. The dashboard refreshes automatically every few seconds.

## Diagnostic script

To test the OpenSky API directly without starting the proxy:

```powershell
py debug_opensky.py
```

## Project files

- `proxy.py` - Flask proxy that requests and reshapes OpenSky flight data.
- `tunis_radar.html` - Browser radar dashboard and live aircraft table.
- `debug_opensky.py` - Simple OpenSky API connectivity and response test.

## Coverage area

The radar covers approximately:

- Latitude: 30 to 38 degrees North
- Longitude: 7 to 13 degrees East

## Notes

Flight availability depends on the data returned by OpenSky at the time of the request. The application is intended for local use and does not include authentication or persistent storage.
