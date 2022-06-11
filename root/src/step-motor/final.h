#include "stepper.h"
#ifndef final_h
#define final_h

Stepper mot1(51, 53); // (dirPin, stepPin)
Stepper mot2(45, 47);
Stepper mot3(39, 41);
Stepper mot4(33, 35);
Stepper mot5(27, 29);

class Final {
    public:
        Final(); //pin direzione, pin controllo step
        void setupMotors(); //inizializza i pin, da mettere sul setup
        void elabora(String s); //fa girare il motore di un tot gradi ad una determinata velocità

    private:
        String _string;
};

Final::Final(){
}
void Final::setupMotors(){

  mot1.setup();
  mot2.setup();
  mot3.setup();
  mot4.setup();
  mot5.setup();

}
void Final::elabora(String s){
  _string = s;
  for(int i=0;_string[i]!='\n';i++){
    int c = 1;
    if(_string[i]=='2'){
      c=2;
    }
    switch(_string[i]){
      case 'L': mot1.turn(90*c, 1000); break;
      case 'R': mot2.turn(90*c, 1000); break;
      case 'B': mot3.turn(90*c, 1000); break;
      case 'D': mot4.turn(90*c, 1000); break;
      case 'F': mot5.turn(90*c, 1000); break;
      case 'L.': mot1.turn(-90*c, 1000); break;
      case 'R.': mot2.turn(-90*c, 1000); break;
      case 'B.': mot3.turn(-90*c, 1000); break;
      case 'D.': mot4.turn(-90*c, 1000); break;
      case 'F.': mot5.turn(-90*c, 1000); break;
      
    }
    delay(500);
  }
}

#endif