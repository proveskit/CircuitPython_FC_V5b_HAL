import board
import busio
import digitalio


class proves_fc_v5b:
    def __init__(self):
        self.uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=1)

        self.i2c0 = busio.I2C(board.SCL0, board.SDA0)
        self.i2c1 = busio.I2C(board.SCL1, board.SDA1)

        self.spi0 = busio.SPI(board.SPI0_SCK, board.SPI0_MOSI, board.SPI0_MISO)
        self.spi1 = busio.SPI(board.SPI1_SCK, board.SPI1_MOSI, board.SPI1_MISO)

        self.burnwire_heater_enable = digitalio.DigitalInOut(
            board.FIRE_DEPLOY1_A, direction=digitalio.Direction.OUTPUT, value=False
        )
        self.burnwire1_fire = digitalio.DigitalInOut(
            board.FIRE_DEPLOY1_B, direction=digitalio.Direction.OUTPUT, value=False
        )

        ### Correct Pattern But These are on the GPIO Expander
        # self.burnwire2_fire = digitalio.DigitalInOut(board.FIRE_DEPLOY2_B, direction=digitalio.Direction.OUTPUT, value=False)
        # self.heater_enable = digitalio.DigitalInOut(board.HEATER_ENABLE, direction=digitalio.Direction.OUTPUT, value=False)

        self.watchdog_enable = digitalio.DigitalInOut(
            board.WDT_ENABLE, direction=digitalio.Direction.OUTPUT, value=False
        )
