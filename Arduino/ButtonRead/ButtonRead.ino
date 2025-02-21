int BUTTON = 6;
int LED = 3;


void setup() {
  pinMode(BUTTON, INPUT);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
}

void loop() {
  if (digitalRead(BUTTON) == LOW) {
    digitalWrite(LED, 255);
    Serial.println("не нажато");

  }
  
  if (digitalRead(BUTTON) == HIGH) {
    digitalWrite(LED, 0);
  }
}
