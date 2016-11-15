import dhtReader

while True:
    (humidity,temperature) = dhtReader.getDhtData()
    print humidity
    print temperature
