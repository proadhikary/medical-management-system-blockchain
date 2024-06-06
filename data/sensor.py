import Adafruit_DHT

class Sensor:
    def __init__(self, sensor_type, pin):
        self.sensor = sensor_type
        self.pin = pin

    def read_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return {'temperature': temperature, 'humidity': humidity}
        else:
            return None
