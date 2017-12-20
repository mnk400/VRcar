int INbyte=0;
void setup()

{
  Serial.begin(115200);
  pinMode( 0, INPUT);
}
void loop()

{
  if(Serial.available()>=0)
  {
    INbyte=Serial.read();
    switch(INbyte)
    {
      case 49 :      Serial.println("Left");
                     analogWrite(9,200);
                     break;

      case 50 :      Serial.println("Right");
                     analogWrite(6,200);
                     break;

      case 51 :      Serial.println("Up");
                     analogWrite(10,200);
                     break;

      case 52 :      Serial.println("Down");
                     analogWrite(11,200);
                     break;

      case 53 :      Serial.println("Bae");
                     analogWrite(9,200);
                     analogWrite(10,200);
                     analogWrite(11,200);
                     analogWrite(6,200);
                     delay(100);
                     analogWrite(9,0);
                     analogWrite(10,0);
                     analogWrite(11,0);
                     analogWrite(6,0);
                     break;

      case 48 :      analogWrite(9,0);
                     analogWrite(10,0);
                     analogWrite(11,0);
                     analogWrite(6,0);
                     break;
    }
  }
}
