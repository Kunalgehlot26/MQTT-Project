MQTT Vehicle Data Publisher
Overview
This Python script is designed to publish vehicle data to an MQTT broker. It utilizes the Paho MQTT client library to establish a connection with the broker and publish JSON-formatted vehicle data.

Prerequisites
Python 3.x installed on your system.
Paho MQTT client library. You can install it using pip:
pip install paho-mqtt
Usage
Setup MQTT Broker: Ensure you have an MQTT broker configured and running. The code is currently configured to use the public MQTT broker hosted at test.mosquitto.org. You can replace broker_address with your MQTT broker's address if needed.

Run the Script: Execute the Python script (mqtt_vehicle_publisher.py). Upon execution, the script prompts the user to input fuel level and speed data for the vehicle.

Input Data: Enter the requested fuel level and speed when prompted by the script.

Data Publication: After receiving the input data, the script publishes the vehicle data in JSON format to the specified topic (vehicle/tracking). The published data includes fuel level, speed, and an example of vehicle behavior, which is currently set to "normal".

Termination: Once the data is published, the script disconnects from the MQTT broker.

Customization
Broker Configuration: If you're using a different MQTT broker, modify the broker_address variable in the script to match your broker's address.
Topic: Adjust the topic variable in the script to publish data to a different MQTT topic if necessary.
Additional Data: You can include additional vehicle data in the publish_vehicle_data function as required. Modify the vehicle_data dictionary to include any additional parameters.
Behavior: Update the "behavior" field in the vehicle_data dictionary to reflect the actual behavior of the vehicle.
Dependencies
Paho MQTT: A Python client library for MQTT.
