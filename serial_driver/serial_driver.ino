const int PIN_Trig = 7;
const int PIN_Echo = 6;
const int PIN_Buzz = 3;
const int PIN_LED1 = 8;
const int PIN_LED2 = 9;

const char* value_string = "{\"value\": ";
const char* noerr_string = "{\"error\": 0}";
int i, j, k;
int sign_word, is_working;

long Ultrasonic_Module(){ // 超声波测距
  long duration;
  pinMode(PIN_Trig, OUTPUT);
  digitalWrite(PIN_Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_Trig, LOW);
  pinMode(PIN_Echo, INPUT);
  duration = pulseIn(PIN_Echo, HIGH);
  return duration / 29.0 / 2.0;
}

void Buzzer_Module(int pin=PIN_Buzz){ // 蜂鸣器响1秒
  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);
  delay(1000);
  digitalWrite(pin, HIGH);
}

void setup(){
  Serial.begin(9600);
}

void loop(){
  is_working = 0;
  if (Serial.available()){
    sign_word = Serial.read();
    if(sign_word == 0x21){ // 蜂鸣器声音
      Buzzer_Module();
      Serial.println(noerr_string);
      is_working = 1;
    }
    if(sign_word == 0x22){ // 超声波测距
      long duration = 0;
      duration = Ultrasonic_Module();
      Serial.print(value_string);
      Serial.print(duration, 2);
      Serial.println("}");
      is_working = 1;
    }
    if(sign_word == 0x23){ // LED1 代表继电器1控制的步进电机，负责通过
      Buzzer_Module(PIN_LED1);
      Serial.println(noerr_string);
      is_working = 1;
    }
    if(sign_word == 0x24){ // LED2
      Buzzer_Module(PIN_LED2);
      Serial.println(noerr_string);
      is_working = 1;
    }
    if(!is_working && sign_word > 0x20){
      Serial.println("{\"error\": 1}");
    }
  } else {
    delay(200);
  }
}
