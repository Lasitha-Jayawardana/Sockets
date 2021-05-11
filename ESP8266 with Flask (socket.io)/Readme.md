# ESP8266 with Flask (socket.io)
This is a Flask server based realtime socket communication for ESP8266 node mcu hardware using socket.io technology.

## How to run
1. In your terminal, navigate to the `ESP8266 with Flask (socket.io)` directory.
2. Run `pip install -r requirements.txt`
3. Change `index.py` IP and Port as yours. 
4. Goto Library Manager in Arduino IDE Install ArduinoJson library
5. Install WebSockets by Markus Sattler v2.3.5 or add WebSocket.zip library to IDE
6. Change `WebSocketIOClient.ino` ssid,password for wifi and IP and port which used in `index.py`
7. Upload `.ino` file to ESP`
8. Run `python index.js`
