#include <ESP8266WiFi.h>

char ssid[] = "SENAI_CAMPINAS";
char senha[] = "senai@mange";

WiFiServer server(80); 

void conectarWifi(char SSID[], char SENHA[]) {
  Serial.print("Conectando a rede");
  Serial.println(SSID);

  WiFi.begin(SSID, SENHA); 

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println(" ");
  Serial.println("Wifi Conectado");
  Serial.println("Endereço de IP: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);

  conectarWifi(ssid, senha);
  server.begin();  
}

void loop() {
  WiFiClient client = server.available(); 

  if (!client) {  
    return;
  }

  while (!client.available()) {
    delay(1);
  }

  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("");
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
  client.println("<meta http-equiv='refresh' content='2'>");
  client.println("<h1>Introdução ao IoT com ESP8266</h1>");
  client.println("<h2>Seja Bem Vindo(a) ao SENAI...!</h2>");
  client.println("<h2>Jonathan Brasil de Sousa</h2>");
  client.println("<h2>Nicole Camacho Rose</h2>");
  client.println("</html>");
}
