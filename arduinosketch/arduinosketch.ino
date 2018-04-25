int INbyte=0;
void setup()

{
  Serial.begin(115200);
  pinMode( 12, OUTPUT);
  pinMode( 13, OUTPUT);
}
void loop()
{
  if(Serial.available()>=0)
  {
    INbyte=Serial.read();
    switch(INbyte)
    {
      case 49 :      Serial.println("Left");
                     digitalWrite(12,HIGH);
                     break;

      case 50 :      Serial.println("Right");
                     digitalWrite(13,HIGH);
                     break;
      default :      digitalWrite(12,LOW);
                     digitalWrite(13,LOW);
                     break;
    }
  }
}
