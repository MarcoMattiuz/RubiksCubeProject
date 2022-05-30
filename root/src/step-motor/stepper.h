#ifndef stepper_h
#define stepper_h

class Stepper {
    public:
        Stepper(int dirPin, int stepPin); //pin direzione, pin controllo step
        void setup(); //inizializza i pin, da mettere sul setup
        void turn(int degrees, int speed); //fa girare il motore di un tot gradi ad una determinata velocità

    private:
        int _stepPin, _dirPin;
};


Stepper::Stepper(int dirPin, int stepPin) 
{
    _stepPin = stepPin;         //salva nelle variabili private della classe
    _dirPin = dirPin;
}

void Stepper::setup()
{
    pinMode(_stepPin, OUTPUT);  //inizializza gli output
    pinMode(_dirPin, OUTPUT);
}

void Stepper::turn(int degrees, int speed)
{
    if (degrees >= 0) {                     //se i gradi di rotazione sono positivi imposta la direzione avanti
        digitalWrite(_dirPin, HIGH);
    }
    else {                                  //se i gradi sono negativi imposta la direzione indietro
        digitalWrite(_dirPin, LOW);
        degrees = -degrees; 
    }

    int step = map(degrees, 0, 360, 0, 200);    //conversione da gradi in step
    for (int i = 0; i < step; i++) {    //gira per n° step
        digitalWrite(_stepPin, HIGH);
        delayMicroseconds(speed); //speed = microsecondi di delay
        digitalWrite(_stepPin, LOW);
        delayMicroseconds(speed);
    }
}

#endif