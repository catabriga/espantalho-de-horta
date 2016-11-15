import Adafruit_DHT

dhtPin = 23

def getDhtData():

    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    return (humidity, temperature)
