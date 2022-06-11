#include "final.h"
String serData;
Final f();
void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is ready!");
}

void loop() {
  while(Serial.available() > 0){
    char rec = Serial.read();
    serData += rec;

    if (rec=='\n'){

      Serial.print("Message received: ");
      Serial.println(serData);
      f.elabora(serData);
      serData="";
    }
  }

delay(10);
}
