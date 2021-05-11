# ESP8266 with Nodejs (socket.io)
This is a Nodejs based realtime socket communication for ESP8266 node mcu hardware and webpage using socket.io technology. This is a node.js package for a simple client/server using socket.io to toggle a "light".

## How to run
1. In your terminal, navigate to the `ESP8266 with Nodejs (socket.io)` directory.
2. Run `npm install`
3. Change `index.js` IP and Port as yours. 
4. Goto Library Manager in Arduino IDE Install ArduinoJson library
5. Add `Socket.io-v1.x-Library-master.zip` library to IDE
6. Change `ESP8266.ino` ssid,password for wifi and IP and port which used in `index.js`
7. Upload `.ino` file to ESP`
8. Run `node index.js`
