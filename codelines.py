import paho.mqtt.client as mqtt
import json

broker_address = "test.mosquitto.org"  # Replace with your MQTT broker address
port = 1883  # Default MQTT port
topic = "vehicle/tracking"

def publish_vehicle_data(client, fuel_level, speed):
    vehicle_data = {
        "fuel_level": fuel_level,  # Fuel level from user input
        "speed": speed,  # Speed from user input
        "behavior": "normal"  # Example vehicle behavior, can be modified as needed
    }
    client.publish(topic, json.dumps(vehicle_data))
    print("Data published")

client = mqtt.Client("VehiclePublisher")
client.connect(broker_address, port)

# Input from the user
fuel_level = float(input("Enter fuel level: "))
speed = float(input("Enter speed: "))

# Publishing the data once
publish_vehicle_data(client, fuel_level, speed)

client.disconnect()
