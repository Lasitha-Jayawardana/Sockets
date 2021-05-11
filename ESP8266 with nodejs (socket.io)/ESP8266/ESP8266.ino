#include <SocketIOClient.h>



 
const char* ssid = "Windows Phone7168" ;
const char* password = "12345678";
 

const char HexLookup[17] = "0123456789ABCDEF";

String host = "192.168.137.240";
int port = 8089;
bool clicked = false;

SocketIOClient socket;

void setupNetwork() {


    WiFi.begin(ssid, password);
    uint8_t i = 0;
    while (WiFi.status() != WL_CONNECTED && i++ < 20) delay(500);
    if(i == 21){
      while(1) delay(500);
    }
Serial.println("connected");

}

void click() {
  clicked = true;
}

void light(String state) {
  Serial.println("[light] " + state);
  if (state == "\"state\":true") {
    Serial.println("[light] ON");
    //digitalWrite(LedPin, HIGH);
  }
  else {
    Serial.println("[light] off");
    //digitalWrite(LedPin, LOW);
  }
}

//
// This code runs only once
//
void setup() {

  // set up our pins


  Serial.begin(115200);

  setupNetwork();

 
  socket.on("light", light);

  socket.connect(host, port);
  Serial.println("loading,,,,,,,,,,,,,,,,,,");
}

void toggle() {
   
    Serial.println("[click]");
    socket.emit("toggle", "{\"state\":true}");
    clicked = false;
 
}

//
// This code runs over and over again
//
void loop() {
  socket.monitor();
  toggle();
  delay(2000);
}

