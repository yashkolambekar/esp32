import urequests
from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
from wlan import connect_to_wifi

# Configure I2C and SSD1306
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))  # Update pins as per your hardware
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text("Turning on..", 0, 0)
oled.show()

wlan = connect_to_wifi()

oled.fill(0)
oled.text("Fetching..", 0, 0)
oled.show()

# Fetch text from the server
url = "https://esp.20022005.xyz/index.php?fetch=true"  # Replace <YOUR_SERVER_IP> with the server's IP
try:
    response = urequests.get(url)
    if response.status_code == 200:  # Check for a successful response
        data = response.json()
        text = data.get('text', 'No text received')
    else:
        text = f"Error: {response.status_code}"
    response.close()
except Exception as e:
    print(e)
    text = "Error: " + str(e)

# Display the text on SSD1306
oled.fill(0)
y = 0
x = 0
for line in text.split('\n'):
    # oled.text(line, 0, y)
        words = line.split(" ")
        for word in words:
            if (len(word) * 10 + x) > oled_width and (len(word) * 10) < oled_width:
                x = 0
                y += 10
            for char in word:
                if ord(char) in [13]:
                    continue
                if x == 0 and char == " ":
                    continue
                oled.text(char, x, y)
                x += 10
                if x > oled_width:
                    x = 0
                    y += 10
                print(char, ord(char))
            x += 10
        x = 0
        y += 10
        if y > oled_height - 10:  # Prevent overflow
            break
oled.show()

