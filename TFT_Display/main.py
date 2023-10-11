import machine
import adafruit_ili9341

# Define the GPIO pins for SPI communication
spi = machine.SPI(1, baudrate=40000000, polarity=1, phase=0, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19))

# Define the GPIO pins for CS (chip select) and DC (data/command)
tft_cs = machine.Pin(5)  # Replace with your CS pin
tft_dc = machine.Pin(4)  # Replace with your DC pin

# Create the ILI9341 display
display = ili9341.ILI9341(spi, cs=tft_cs, dc=tft_dc)

# Create a simple test graphic
display_group = displayio.Group()

# Create a solid color background
bg_color = displayio.Bitmap(display.width, display.height, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = 0x00FF00  # Green color
bg_tilegrid = displayio.TileGrid(bg_color, pixel_shader=bg_palette)
display_group.append(bg_tilegrid)

# Create a text label
text = "Hello, ESP32-S3!"
text_area = displayio.Text(
    font=None, text=text, x=20, y=120, color=0x000000
)
display_group.append(text_area)

# Show the display group
display.show(display_group)

while True:
    pass  # You can add your code here to update the display as needed