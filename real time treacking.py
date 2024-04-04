import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker Information
broker_address = "test.mosquitto.org"
broker_port = 1883
client_id = "vehicle_tracker"

# Vehicle information
vehicle_id = "vehicle_001"

# Callback function for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing to the topic where the vehicle sends its location data
    client.subscribe("vehicle/" + vehicle_id + "/location")

# Callback function for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print("Received location data: ", payload)

# Create an MQTT client instance
client = mqtt.Client(client_id=client_id)

# Assigning the on_connect and on_message callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start a background thread to handle MQTT communication
client.loop_start()

try:
    while True:
        # Simulating vehicle location data
        location_data = {
            "latitude": 40.7128,  # Example latitude
            "longitude": -74.0060,  # Example longitude
            "speed": 60  # Example speed in km/h
        }
        
        # Publishing the location data to the vehicle's topic
        client.publish("vehicle/" + vehicle_id + "/location", json.dumps(location_data))
        
        print("Published location data:", location_data)
        
        # Sending data every 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
    client.loop_stop()
