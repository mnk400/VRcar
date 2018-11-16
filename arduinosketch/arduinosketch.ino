int INbyte=0;
int Speed=200;

const int EN1 = 10;
const int IN1 = 9;
const int IN2 = 8;

const int IN3 = 7;
const int IN4 = 6;
const int EN2 = 5;

void setup() {
  Serial.begin(115200);
  pinMode(IN1, OUTPUT);    
  pinMode(IN2, OUTPUT);    
  pinMode(IN3, OUTPUT);     
  pinMode(IN4, OUTPUT);     

}

void loop() {
  analogWrite(EN1, Speed);
  analogWrite(EN2, Speed);  
  int var;
  if(Serial.available()>=0)
  {
    INbyte=Serial.read();
    switch(INbyte)
    {
      case 49 :      Serial.println("GO");
                     digitalWrite(IN1,HIGH);
                     digitalWrite(IN3,HIGH);
                     break;

      case 50 :      Serial.println("RIGHT");
                     digitalWrite(IN1,HIGH);         
                     break;

      case 51 :      Serial.println("LEFT");
                     digitalWrite(IN3,HIGH);
                     break; 
                     
      case 52 :      Serial.println("BACK");
                     digitalWrite(IN2,HIGH);
                     digitalWrite(IN4,HIGH);
                     break;
                      
      case 48 :      Serial.println("STOP");
                     digitalWrite(IN1,LOW);
                     digitalWrite(IN2,LOW);
                     digitalWrite(IN3,LOW);
                     digitalWrite(IN4,LOW);
                     break;

      case 53 :      Serial.println("Speed Set Low");
                     Speed = 130;
                     break;

      case 54 :      Serial.println("Speed Set Mid");
                     Speed = 200;
                     break;                               
      
      case 55 :      Serial.println("Speed Set High");
                     Speed = 255;
                     break;
                     
      default :      break;               
    }
  }
}
