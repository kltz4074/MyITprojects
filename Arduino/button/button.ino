const int ledPin = 9;      // Пин для светодиода (PWM)
const int buttonPin = 3;   // Пин кнопки
int buttonState = 0;       // Текущее состояние кнопки
int lastButtonState = 0;   // Предыдущее состояние кнопки
bool ledState = false;     // Переменная для хранения состояния светодиода

void setup() {
  pinMode(ledPin, OUTPUT);        
  pinMode(buttonPin, INPUT_PULLUP); // Подтяжка к +5V (HIGH по умолчанию)
}

void loop() {
  buttonState = digitalRead(buttonPin); // Читаем кнопку

  if (buttonState == LOW && lastButtonState == HIGH) { // Если нажали кнопку
    delay(50);  // Антидребезг
    ledState = !ledState;  // Меняем состояние светодиода
    digitalWrite(ledPin, ledState ? HIGH : LOW); // Включаем или выключаем LED
  }

  lastButtonState = buttonState; // Запоминаем состояние кнопки
}
