import network
import time

# Wi-Fi credentials
SSID = "xxxxxxxx"       # Replace with your Wi-Fi SSID
PASSWORD = "xxxxxxxxxxxx"  # Replace with your Wi-Fi password

def connect_to_wifi():
    # Initialize Wi-Fi in station mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    # Check if already connected
    if wlan.isconnected():
        print("Already connected to Wi-Fi!")
        return wlan
    
    # Connect to Wi-Fi
    print(f"Connecting to Wi-Fi network '{SSID}'...")
    wlan.connect(SSID, PASSWORD)
    
    # Wait for connection
    timeout = 10  # Timeout in seconds
    start_time = time.time()
    while not wlan.isconnected():
        if time.time() - start_time > timeout:
            print("Failed to connect to Wi-Fi.")
            return None
        time.sleep(1)
    
    # Print network details
    print("Connected to Wi-Fi!")
    print("Network details:", wlan.ifconfig())
    return wlan

