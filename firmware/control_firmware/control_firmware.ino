/////////////////////////////////////////////////////
/*
INSPECAO TAMPOGRAFIA INJETORA - PROGRAMA DE CONTROLE

Autor: Felipe Cabral
Setor: Engenharia Industrial
Versão: 3.0

Controle de Versões:
0.0: Teste entradas da placa
1.0: Teste entradas e saidas da placa
2.0: Programa comunicação serial para fotos
3.0: Versão piloto para inspeção
*/
//////////////////////////////////////////////////

#define INPUT_E1 A1 // Pino do sinal do clp inicio/fim para zerar contador etapas do processo (ENTRADA 1 - 24v)
#define INPUT_E2 A0 // Pino do sinal do clp sensor carro recuado (ENTRADA 2 - 24v)
#define INPUT_E3 A2 // Pino do botao reset do sinalizador (ENTRADA 3 - 12v)

#define OUTPUT_S1 5 // Pino alimentacao solenoide valvula 1 (SAIDA 1)
#define OUTPUT_S2 6 // Pino alimentacao solenoide valvula 2 (SAIDA 2)
#define OUTPUT_S3 7 // Pino alimentacao liberar CLP (SAIDA 3)


#define OUTPUT_SR 11 // Pino alimentacao torre sinalizacao (RELE) 

int etapa = -1;
int defeito_v1 = 0;
int defeito_v2 = 0;
int cont_reprovadas = 0;
// const int NUMERO_MAXIMO_DE_REPROVACOES = ; Isso fala sobre as quantidades máximas que a máquina irá aturar no sistema. Fica melhor numa constanste para facilitar mudanças futuras

void aguarda_inicio() {
    if(analogRead(INPUT_E1) < 500) {
        etapa = 1;
    }
}

void verifica_defeito() {
    if (analogRead(INPUT_E2) < 500) {  // se o carro estiver no local de checagem, ou seja, liberado para o controlador soltar as placas defeituosas
        if (defeito_v1 == 1 && defeito_v2 == 0) {
          //Delay para saber quando soltar
            digitalWrite(OUTPUT_S1,HIGH);
            delay(1000);
            digitalWrite(OUTPUT_S1,LOW);
            defeito_v1 = 0;
            cont_reprovadas ++;            
        }
        else if (defeito_v1 == 0 && defeito_v2 == 1) {
            digitalWrite(OUTPUT_S2,HIGH);
            delay(1000);
            digitalWrite(OUTPUT_S2,LOW);
            defeito_v2 = 0;
            cont_reprovadas ++;            
        }
        else if (defeito_v1 == 1 && defeito_v2 == 1) {
            digitalWrite(OUTPUT_S1,HIGH);
            digitalWrite(OUTPUT_S2,HIGH);
            delay(1000);
            digitalWrite(OUTPUT_S1,LOW);
            digitalWrite(OUTPUT_S2,LOW);
            defeito_v1 = 0;
            defeito_v2 = 0;
            cont_reprovadas += 2;            
        }
        else if (defeito_v1 == 0 && defeito_v2 == 0) {
            cont_reprovadas = 0;
        }
        if (cont_reprovadas >= 4) { //pode colocar a constante NUMERO_MAXIMO_DE_REPROVACOES aqui
            digitalWrite(OUTPUT_SR, HIGH); //ATIVAR SIRENE
            Serial.println("w");
            cont_reprovadas = 0;       
        }
        while (analogRead(INPUT_E2) < 500) {} // Esperar o carro sair da área de checagem para a próxima etapa
                etapa = 2;
    }
}

void primeira_inspecao() {
    if (analogRead(INPUT_E2) < 500) { //voltando para a área de checagem
        delay(500);
        Serial.println("p"); // Envia 'p' pela serial indicando a primeira inspeção
        
        while (analogRead(INPUT_E2) < 500) {
            if (Serial.available() > 0) {
                char ser = Serial.read();
                if (ser == 'n') {
                    defeito_v1 = 1;
                    break;
                }
            }
        }
        while (analogRead(INPUT_E2) < 500){}
        etapa = 3;
    }
}

void segunda_inspecao() {
    if (analogRead(INPUT_E2) < 500) { //voltando para a área de checagem
        delay(500);
        Serial.println("p"); // Envia 'p' pela serial indicando a primeira inspeção
        
        while (analogRead(INPUT_E2) < 500) {
            if (Serial.available() > 0) {
                char ser = Serial.read();
                if (ser == 'n') {
                    defeito_v2 = 1;
                    break;
                }
            }
        }
        while (analogRead(INPUT_E2) < 500){}
        etapa = 0;
    }
}

void reset_sinalizador() {
    if(analogRead(INPUT_E3) < 500) {
        digitalWrite(OUTPUT_SR, LOW);
        cont_reprovadas = 0;
    }
}

void setup() {

    Serial.begin(9600);
    
    pinMode(INPUT_E1, INPUT);
    pinMode(INPUT_E2, INPUT);
    pinMode(INPUT_E3, INPUT);
    
    pinMode(OUTPUT_S1, OUTPUT);
    pinMode(OUTPUT_S2, OUTPUT);
    pinMode(OUTPUT_S3, OUTPUT);
    pinMode(OUTPUT_SR, OUTPUT);

    digitalWrite(OUTPUT_S1, LOW);
    digitalWrite(OUTPUT_S2, LOW);
    digitalWrite(OUTPUT_S3, HIGH);
    digitalWrite(OUTPUT_SR, LOW);
     
}

void loop() {
    
    while((Serial.available() > 0)){
       char ser = Serial.read(); 
       if(ser == 'x') {
        digitalWrite(OUTPUT_S3, LOW);
        etapa = 0;
       }
       else if(ser == 'y') { //A interface enviou um modo espera para o arduino
        digitalWrite(OUTPUT_S3, HIGH);
        etapa = -1;
       }
    }

    reset_sinalizador();

    if (etapa == 0) aguarda_inicio();
    else if (etapa == 1)verifica_defeito(); //verifica os defeitos antes de inspecionar? Não deveria ser o inverso? |Pois ele irá responder para o ciclo anterior|
    else if (etapa == 2)primeira_inspecao();
    else if (etapa == 3)segunda_inspecao();

}
