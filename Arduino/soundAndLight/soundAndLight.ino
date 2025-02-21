int buzzerPin = 6;
int light = 3;
int button = 9;
int buttonState = 0;
int button2 = 6;
void setup() {
  pinMode(light, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  analogWrite(light, 255);
  /*
  buttonState = digitalRead(button);

  if (buttonState == LOW) {
    analogWrite(light, 0);
  } else {
    analogWrite(light, 255);
  }
  */
}
