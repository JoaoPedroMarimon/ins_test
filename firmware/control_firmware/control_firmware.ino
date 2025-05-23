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

#define INPUT_E1 A1  // Pino do sinal do clp inicio/fim para zerar contador etapas do processo (ENTRADA 1 - 24v)
#define INPUT_E2 A0  // Pino do sinal do clp sensor carro recuado (ENTRADA 2 - 24v)
#define INPUT_E3 A2  // Pino do botao reset do sinalizador (ENTRADA 3 - 24v)
#define INPUT_E4 A3  // Pino do sensor de posição do gabarito (ENTRADA 4 - 24v)

#define OUTPUT_S1 5  // Pino alimentacao solenoide valvula 1 (SAIDA 1)
#define OUTPUT_S2 6  // Pino alimentacao solenoide valvula 2 (SAIDA 2)
#define OUTPUT_S3 7  // Pino alimentacao liberar CLP (SAIDA 3)

#define OUTPUT_SR 11  // Pino alimentacao torre sinalizacao (RELE)


int etapa = -1;
int defeito_v1 = 1;
int defeito_v2 = 1;
bool enviado = false;
const int INSPECOES_CICLO = 10;
const int LIMITE_REPROVACAO = 5;
bool result_list[INSPECOES_CICLO] = {false};  // Inicializando o array com false
unsigned int step = 0;

void add_insp(bool resultado) {
  result_list[step] = resultado;
  step = (step + 1) % INSPECOES_CICLO;  // Evita acesso inválido
}

void limpar_lista_insp() {
  for (int i = 0; i < INSPECOES_CICLO; i++) {
    result_list[i] = false;
  }
}

bool alcansou_limite() {
  int sum = 0;
  for (bool insp : result_list) sum += insp;
  return sum >= LIMITE_REPROVACAO;
}


void aguarda_inicio() {
  if (analogRead(INPUT_E1) < 500) {
    delay(500);
    Serial.println("k");
    etapa = 1;
  }
}

void verifica_defeito() {
  delay(1000);
  Serial.println("Debug: Iniciando o verifica defeito")
  if (analogRead(INPUT_E2) < 500) {

  Serial.println("Debug: Inserindo defeitos")
    add_insp(defeito_v1);
    add_insp(defeito_v2);

      Serial.println("Debug: Iniciando descarte")

    if (defeito_v1 == 1) {
      digitalWrite(OUTPUT_S1, HIGH);
      digitalWrite(OUTPUT_SR, HIGH);
      delay(200);
    }
    if (defeito_v2 == 1) {
      digitalWrite(OUTPUT_S2, HIGH);
      digitalWrite(OUTPUT_SR, HIGH);
    }
    if (defeito_v1 == 1 || defeito_v2 == 1) {
      delay(2000);
    }
    digitalWrite(OUTPUT_SR, LOW);
    digitalWrite(OUTPUT_S1, LOW);
    digitalWrite(OUTPUT_S2, LOW);
    defeito_v1 = 0;
    defeito_v2 = 0;

    Serial.println("Debug: Decisão do descarte feita")

    Serial.println("Debug: Iniciando a verificação de limite")
    if (alcansou_limite()) {
      digitalWrite(OUTPUT_SR, HIGH);
      digitalWrite(OUTPUT_S3, HIGH);
      Serial.println("w");
      limpar_lista_insp();
    }
    Serial.println("Debug: Limite verificado")

    while (analogRead(INPUT_E2) < 500) {}
    etapa = 2;
  }
}

void primeira_inspecao() {
  delay(1000);
  if (analogRead(INPUT_E2) < 500) {
    delay(1000);
      Serial.println("Debug: Iniciando primeira inspeção")

      Serial.println("Debug: Enviando mensagem para o main")

    if (analogRead(INPUT_E4) > 500) {
      Serial.println("p1");
    } else {
      Serial.println("p2");
    }
      Serial.println("Debug: Recebendo mensagem do main")

    unsigned long startTime = millis();

    while (analogRead(INPUT_E2) < 500) {
      if (Serial.available() > 0) {
        Serial.println("Debug: Mensagem recebida ")
        char ser = Serial.read();
        if (ser == 'n') {
          defeito_v1 = 1;
          break;
        } else if (ser == 'o') {
          break;
        }
      }

      if (millis() - startTime > 2000) {
        digitalWrite(OUTPUT_SR, HIGH);
        defeito_v1 = 1;
        digitalWrite(OUTPUT_S3, HIGH);
        etapa = -1;
          Serial.println("Debug: Mensagem não recebida")

        return;
      }
    }

    while (analogRead(INPUT_E2) < 500) {}
    Serial.println("Debug: Primeira inspeção finalizada ")

    etapa = 3;
  }
}

void segunda_inspecao() {
  delay(1000);
  if (analogRead(INPUT_E2) < 500) {
    delay(1000);
    Serial.println("Debug: Segunda inspeção inicializada ")

    Serial.println("Debug: enviando mensagem para o main")

    if (analogRead(INPUT_E4) > 500) {
      Serial.println("p1");
    } else {
      Serial.println("p2");
    }
      Serial.println("Debug: Recebendo mensagem do main")

    unsigned long startTime = millis();

    while (analogRead(INPUT_E2) < 500) {
      if (Serial.available() > 0) {
      Serial.println("Debug:  Mensagem do main recebida")

        char ser = Serial.read();
        if (ser == 'n') {
          defeito_v2 = 1;
          break;
        } else if (ser == 'o') {
          break;
        }
      }

      if (millis() - startTime > 2000) {
        digitalWrite(OUTPUT_SR, HIGH);
        defeito_v2 = 1;
        digitalWrite(OUTPUT_S3, HIGH);
        etapa = -1;
      Serial.println("Debug:  Mensagem do main NÃO recebida")

        return;
      }
    }

    while (analogRead(INPUT_E2) < 500) {}
    Serial.println("Debug: Segunda inspeção finalizada ")

    etapa = 0;
  }
}

void reset_sinalizador() {
  if (analogRead(INPUT_E3) < 500 && digitalRead(OUTPUT_SR) == HIGH) {
      Serial.println("Debug:  sinalizador resetado")

    // e tambem se etapa for diferente de -1
    //se etapa for igual -1 apenas desliga alarme
    if (etapa != -1) {
      digitalWrite(OUTPUT_S3, LOW);
    }
    digitalWrite(OUTPUT_SR, LOW);
  }
}

void setup() {

  Serial.begin(9600);

  pinMode(INPUT_E1, INPUT);
  pinMode(INPUT_E2, INPUT);
  pinMode(INPUT_E3, INPUT);
  pinMode(INPUT_E4, INPUT);

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

  while (Serial.available() > 0) {
    char ser = Serial.read();
    if (ser == 'x') {
      digitalWrite(OUTPUT_S3, LOW);
      limpar_lista_insp();
      defeito_v1 = 1;
      defeito_v2 = 1;
      etapa = 0;
    }

    else if (ser == 'y') {
      digitalWrite(OUTPUT_S3, HIGH);
      etapa = -1;
    }
  }

  reset_sinalizador();

  if (etapa == 0) aguarda_inicio();
  else if (etapa == 1) verifica_defeito();
  else if (etapa == 2) primeira_inspecao();
  else if (etapa == 3) segunda_inspecao();
}
