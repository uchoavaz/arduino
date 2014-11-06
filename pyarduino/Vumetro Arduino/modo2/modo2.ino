void setup(){
  pinMode(13,OUTPUT);
    pinMode(12,OUTPUT);
     pinMode(11,OUTPUT);
       pinMode(10,OUTPUT);
       pinMode(9,OUTPUT);
    pinMode(8,OUTPUT);
     pinMode(7,OUTPUT);
       pinMode(6,OUTPUT);
        pinMode(5,OUTPUT);
       pinMode(4,OUTPUT);


  Serial.begin(9600);
}
void loop(){
 int sensorValue = analogRead(A4);
 float voltagem = sensorValue * (5.0/1023.0);

 Serial.println(voltagem);
 
 if(voltagem>=0.2)
   {
    digitalWrite(4,HIGH);
    digitalWrite(13,HIGH);
    
    if(voltagem>=0.6){
     digitalWrite(5,HIGH);
     digitalWrite(12,HIGH);
         }
         
    if(voltagem>=1.0){
     digitalWrite(6,HIGH);
      digitalWrite(11,HIGH);
     
         }
     if(voltagem>=1.4){
     digitalWrite(7,HIGH);
      digitalWrite(10,HIGH);
         }
         if(voltagem>=1.8){
     digitalWrite(8,HIGH);
        digitalWrite(9,HIGH);
         }
         
   delay(10);
       }

  

 

else {
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
   digitalWrite(10,LOW);
   digitalWrite(9,LOW);
  digitalWrite(8,LOW);
  digitalWrite(7,LOW);
   digitalWrite(6,LOW);
    digitalWrite(5,LOW);
   digitalWrite(4,LOW);
   
}
}

