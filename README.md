# INSPEÇÃO-TAMPOGRAFIA-SWITCH-8P

Projeto inspeção-tampografia consiste em identificar erros gráficos nas tampas dos switch's do CMD. <br>
Neste projeto estão envolvidas três  entidades:  

- IHM (Interface Humano Computador) feita pelos Jovens Aprendizes;
- INSPEÇÃO feita por --;
- ARDUINO feita por Felipe Cabral;

## Comunicação entre entidades

Para o funcionamento do projeto, é necessário estabelecer uma relação entre as três partes e suas devidas responsabilidades.

### IHM
Trata-se do desenvolvimento da interface visual que o colaborador poderá interagir. Nesta, tem-se a responsabilidade dividida em 2 partes, a **primeira tela** e a **segunda tela**. Veja abaixo os respectivos fluxogramas:

#### Fluxograma primeira tela - IHM
![Diagrama primeira tela](src/documents/Fluxograma%20primeira%20tela.png)

Sobre a primeira tela, ao dar inicio é disparado na lógica a tela de seleção de modelos, esta consiste em uma tela opaca com botões verdes com os modelos de switch que a **_JIGA INSPEÇÃO-TAMPOGRAFICA-SWITCH-8P_** trabalha. O colaborador fica responsável por escolher qual o modelo switch a jiga vai prosseguir. Assim que o botão do modelo escolhido for pressionado, ele disparará um sinal de envio para a segunda entidade **a INSPEÇÃO**. <br>
<br>
A relação entre o **IHM** e a **INSPEÇÃO** é no sistema de "via dupla", ocorrendo as seguintes trocas de informação:

```
    - IHM -> INSPEÇÃO: Informa qual foi o modelo switch escolhido pelo colaborador
```

```
    - INSPEÇÃO -> IHM: Informa quando uma placa foi aprovada ou reprovada
```
    
- `EXPLICAR O RESTO DAS INTERAÇÕES ENTRE AS ENTIDADES ESPECIFICADAS`

Após a troca de informações entre essas duas entidades é então disparado a segunda tela.

#### Fluxograma segunda tela - IHM
![Diagrama segunda tela](src/documents/Fluxograma%20segunda%20tela.png)


`explicação sobre a segunda tela`

