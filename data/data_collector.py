import Adafruit_DHT
from .sensor import Sensor

class DataCollector:
    def __init__(self, sensor_type, pin):
        self.sensor = Sensor(sensor_type, pin)

    def collect_data(self):
        return self.sensor.read_data()
