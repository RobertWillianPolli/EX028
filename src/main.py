
from machine import Pin, SoftI2C
from sh1107 import SH1107_I2C
import utime


# ============================================================
# PINOS
# ============================================================

TRIG = Pin(1, Pin.OUT)
ECHO = Pin(0, Pin.IN)

# OLED da BitDogLab V7
i2c = SoftI2C(
    scl=Pin(3),
    sda=Pin(2),
    freq=50000
)

oled = SH1107_I2C(128, 128, i2c, addr=0x3C)


# ============================================================
# FUNÇÃO PARA MEDIR A LARGURA DO ECHO
# ============================================================

def medir_echo_us(timeout_us=30000):

    # Garante que o TRIG esteja em LOW
    TRIG.value(0)
    utime.sleep_us(2)

    # Pulso de disparo de 10 us
    TRIG.value(1)
    utime.sleep_us(10)
    TRIG.value(0)

    # --------------------------------------------------------
    # Espera o ECHO subir
    # --------------------------------------------------------

    inicio_espera = utime.ticks_us()

    while ECHO.value() == 0:

        if utime.ticks_diff(
            utime.ticks_us(),
            inicio_espera
        ) > timeout_us:
            return None

    # Momento exato em que ECHO ficou HIGH
    inicio = utime.ticks_us()

    # --------------------------------------------------------
    # Espera o ECHO voltar para LOW
    # --------------------------------------------------------

    while ECHO.value() == 1:

        if utime.ticks_diff(
            utime.ticks_us(),
            inicio
        ) > timeout_us:
            return None

    # Momento exato em que ECHO voltou para LOW
    fim = utime.ticks_us()

    # Largura do pulso
    tempo = utime.ticks_diff(fim, inicio)

    return tempo


# ============================================================
# INICIALIZAÇÃO
# ============================================================

TRIG.value(0)

oled.fill(0)
oled.text("HC-SR04", 32, 0)
oled.text("Aguardando...", 12, 20)
oled.show()

utime.sleep_ms(1000)


# ============================================================
# LOOP PRINCIPAL
# ============================================================

while True:

    tempo_us = medir_echo_us()

    oled.fill(0)

    oled.text("HC-SR04", 32, 0)

    if tempo_us is None:

        oled.text("Sem resposta", 12, 24)

    else:

        # Tempo em microssegundos
        oled.text("Tempo de", 32, 16)
        oled.text("propagacao:", 20, 28)

        texto = "{} us".format(tempo_us)
        oled.text(texto, 36, 42)

    oled.show()

    # Evita disparos muito rápidos
    utime.sleep_ms(100)



