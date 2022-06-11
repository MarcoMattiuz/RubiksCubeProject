#include "stepper.h"
int button = A0;
const int ON = 0, OFF = 1;  //per la logica del pulsante

Stepper mot1(51, 53); // (dirPin, stepPin)
Stepper mot2(45, 47);
Stepper mot3(39, 41);
Stepper mot4(33, 35);
Stepper mot5(27, 29);

void setup()
{

  mot1.setup();
  mot2.setup();
  mot3.setup();
  mot4.setup();
  mot5.setup();

  pinMode(button, INPUT_PULLUP);
 
  Serial.begin(9600);

  
}

void loop()
{
  int value = analogRead(button);
  Serial.println(value);
  if (value > 100&&value<250) {
    mot1.turn(90, 1000); //90=gradi di rotazione, 1000=delayMicroseconds
    delay(500);
  }else if (value > 350&&value<400) {
    mot2.turn(90, 1000); //90=gradi di rotazione, 1000=delayMicroseconds
     delay(500); 
      
    }else if (value > 500&&value<600) {
    mot3.turn(90, 1000); //90=gradi di rotazione, 1000=delayMicroseconds
      delay(500); 
    }else if (value > 650&&value<750) {
    mot4.turn(90, 1000); //90=gradi di rotazione, 1000=delayMicroseconds
         delay(500); 
    }else if (value >800&&value<900) {
   /* while(digitalRead(button) == ON) delay(1); //si ferma finchè non rilasci il pulsante (per evitare rimbalzi)
    mot1.turn(90, 1000); //90=gradi di rotazione, 1000=delayMicroseconds
    delay(1000);
    mot3.turn(90, 1000);
    delay(1000);
    mot2.turn(90, 1000);
    delay(1000);
    mot4.turn(90, 1000);
    delay(1000);
    */
    mot5.turn(90, 1000);
      delay(500) ;

            
  }
}