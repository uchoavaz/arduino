void setup(){
pinMode(13,OUTPUT);
Serial.begin(9600);
}

boolean seconds = false;
boolean minutes = false;
boolean hour = false;
int scds=0;
int mnts=0;
int hours=0;
int numScds;
int numMnts;
int numHours;
String concatenador = "";

void formTime(char leitura){
    
    if(leitura =='S' || seconds==true){
        
        digitalWrite(13,LOW);
        if(leitura == 'E'){
            seconds=false;
            numScds = concatenador.toInt();
            concatenador="";
            
              hrs(numHours);
              mnt(numMnts);
              sec(numScds);
              Serial.println("OK");
              digitalWrite(13,HIGH);
        }
           
        else if (seconds==true){ 
        concatenador = concatenador + leitura;
        }
        
        else{
            seconds=true;
        }
    }
 
    else if(leitura =='M' || minutes==true){
        
        digitalWrite(13,LOW);
        if(leitura == 'E'){
            minutes=false;
            numMnts = concatenador.toInt();
            concatenador="";
        }
           
        else if (minutes==true){ 
        concatenador = concatenador + leitura;
        }
        
        else{
            minutes=true;
        }
    }
    
    else if(leitura =='H' || hour==true){
        
        digitalWrite(13,LOW);
        if(leitura == 'E'){
            hour=false;
            numHours = concatenador.toInt();
            concatenador="";
        }
           
        else if (hour==true){ 
        concatenador = concatenador + leitura;
        }
        
        else{
            digitalWrite(13,LOW);
            hour=true;
        }
    } 
    
    else if(leitura =='1'){
        digitalWrite(13,HIGH);
    }

    else if(leitura =='0'){
        digitalWrite(13,LOW);
    }    
}

void sec(int time){
    boolean sair=false;
    
    
    while (sair==false){
    
        if (time == scds){
            scds = 0;
            sair =true;

        }
    
        else{
            delay(1000);
            scds = scds + 1;
            
            if (scds != 60){
                printer();
            }  
        }
    
    }
}

void mnt(int time){
    boolean sair=false;
    mnts = 0;
    
    while (sair==false){
    
        if (time == mnts){         
            sair =true;  
        }
    
        else{
            sec(60);
            mnts = mnts + 1;  
          
            if (mnts != 60){
                printer();
            }  
            
        }
    
    }
}

void hrs(int time){
    boolean sair=false;
    hours = 0;
    
    while (sair==false){
    
        if (time == hours){
            sair =true;  
        }
    
        else{
            mnt(60);
            hours = hours + 1;
            printer();      
        }
    
    }
}

void printer(){
   Serial.print(hours);
   Serial.print(" hrs "); 
   Serial.print(mnts); 
   Serial.print(" min ");    
   Serial.print(scds);
   Serial.println(" sec"); 
}

void loop(){
  
delay(1);
char reader = Serial.read();
formTime(reader);

}
