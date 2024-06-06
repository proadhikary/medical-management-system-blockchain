import paho.mqtt.client as mqtt
import json

class DataTransmitter:
    def __init__(self, broker_address, topic, username, password):
        self.client = mqtt.Client()
        self.client.tls_set('/path/to/ca.crt')
        self.client.username_pw_set(username, password)
        self.client.connect(broker_address, 8883, 60)
        self.topic = topic

    def transmit_data(self, data):
        payload = json.dumps(data)
        self.client.publish(self.topic, payload)
