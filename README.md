# Medição do Tempo de Propagação com HC-SR04 – BitDogLab

## 📌 Descrição do Projeto

Este projeto utiliza o sensor ultrassônico **HC-SR04** conectado à placa **BitDogLab V7** para medir o tempo de propagação de uma onda ultrassônica.

O sistema realiza o disparo de um pulso ultrassônico pelo pino TRIG, monitora o sinal de retorno pelo pino ECHO e calcula a duração do pulso recebido.

O resultado da medição é apresentado em tempo real em um display OLED de 128 × 128 pixels, utilizando comunicação I²C.

## 🛠️ Hardware utilizado

- BitDogLab V7
- Sensor ultrassônico HC-SR04
- Display OLED SH1107 (128 × 128 pixels)

## 🔌 Ligações

| Componente | Pino BitDogLab |
|---|---|
| HC-SR04 – TRIG | GPIO 1 |
| HC-SR04 – ECHO | GPIO 0 |
| OLED – SCL | GPIO 3 |
| OLED – SDA | GPIO 2 |

**Atenção:** O pino ECHO do HC-SR04 opera em nível lógico de 5 V. Utilize um divisor de tensão ou conversor de nível lógico antes de conectá-lo diretamente ao GPIO da placa.

## 💻 Software e bibliotecas

O projeto foi desenvolvido em **MicroPython**, utilizando:

- `machine`: configuração e controle dos pinos GPIO e I²C.
- `utime`: controle de temporização e medição em microssegundos.
- `sh1107`: biblioteca para comunicação com o display OLED SH1107.

## ⚙️ Funcionamento

O programa executa continuamente as seguintes etapas:

1. Configura o pino TRIG como saída e o ECHO como entrada.
2. Envia um pulso de 10 µs ao pino TRIG para iniciar a medição.
3. Aguarda o sinal ECHO assumir nível lógico HIGH.
4. Registra o instante inicial da resposta.
5. Aguarda o retorno do ECHO para nível LOW.
6. Registra o instante final e calcula a duração do pulso.
7. Exibe o tempo medido no display OLED.

### Medição do tempo

A duração do pulso é calculada pela diferença entre os instantes de início e término do sinal ECHO:

\[
t = t_{final} - t_{inicial}
\]

O resultado é apresentado em microssegundos (µs).

O código também implementa um mecanismo de timeout de 30.000 µs para evitar que o programa permaneça indefinidamente aguardando uma resposta do sensor.

## 🖥️ Interface OLED

O display apresenta:

- Identificação do sensor HC-SR04.
- Tempo de propagação medido em microssegundos.
- Mensagem de ausência de resposta quando ocorre timeout.

## 📂 Estrutura do projeto

```text
EX028/
│
├── RoteiroV2.pdf
├── README.md
└── src/
     │
     ├── main.py
     └── sh1107.py
```

- `main.py`: código principal de aquisição e apresentação das medições.
- `sh1107.py`: biblioteca de controle do display OLED.
- `README.md`: documentação do projeto.
- `RoteiroV2.pdf`: Roteiro utilizado em sala

## 🚀 Como executar

1. Conecte o HC-SR04 e o display OLED à BitDogLab conforme a tabela de ligações.
2. Instale a biblioteca `sh1107.py` na placa.
3. Transfira o código principal para a BitDogLab.
4. Execute o programa utilizando um ambiente compatível com MicroPython, como o Thonny.
5. Observe os valores de tempo apresentados no display OLED.

## 🎯 Objetivo educacional

O projeto permite explorar conceitos fundamentais de sistemas embarcados, incluindo:

- Configuração de entradas e saídas digitais.
- Comunicação I²C.
- Temporização em microssegundos.
- Aquisição de sinais digitais.
- Medição de largura de pulso.
- Tratamento de timeout.
- Integração entre sensores e displays.

---

**Plataforma:** BitDogLab V7  
**Linguagem:** MicroPython  
**Sensor:** HC-SR04  
**Display:** OLED SH1107