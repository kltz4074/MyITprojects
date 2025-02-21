#include <Servo.h>

const int VRX = A0;  // Ось X джойстика
const int VRY = A1;  // Ось Y джойстика
const int SW = 2;    // Кнопка джойстика (если нужно, можно использовать)
const int servoPin = 6;  // Пин для сервопривода

Servo myServo;  // Создаём объект для сервопривода

void setup() {
    Serial.begin(9600);  // Запуск Serial Monitor для отладки
    myServo.attach(servoPin);  // Подключаем сервопривод к пину
}

void loop() {
    int x = analogRead(VRX);  // Считываем ось X джойстика
    int y = analogRead(VRY);  // Считываем ось Y джойстика
    int button = digitalRead(SW);  // Считываем кнопку (если нужно)

    // Отображаем значения в Serial Monitor для отладки
    Serial.print("X: "); Serial.print(x);
    Serial.print(" | Y: "); Serial.print(y);
    Serial.print(" | Button: "); Serial.println(button);

    // Преобразуем значение оси Y джойстика (0-1023) в диапазон для угла (0-180)
    int servoAngle = map(y, 0, 1023, 0, 180);  // Преобразуем ось Y в угол для сервопривода

    myServo.write(servoAngle);  // Поворачиваем сервопривод

    delay(15);
}
