const int MIC = 0;
int adc;
int dB, PdB;
void setup() {
Serial.begin(9600); 
  pinMode(8, OUTPUT);
}
void loop(){
  PdB = dB; 
  
adc= analogRead(MIC); 

dB = (adc+83.2073) / 11.003; 
if (PdB!=dB)
Serial.println (dB);
if (dB>60)
{
  digitalWrite(8, HIGH);
  Serial.println (dB);
   Serial.println ("High Noise Pollution");
  delay(2000);                      
  digitalWrite(8, LOW); 
}
else
{
  digitalWrite(8, LOW);
   Serial.println ("Low Noise Pllution");
}
//delay(100);
}
