import math

class AccessPoint:
    def __init__(self, name, x, y, channel, power_level,
                 frequency, standard, supports_11k, supports_11v,
                 supports_11r, coverage_radius, device_limit,
                 minimal_rssi):
        self.name =  name
        self.x = x
        self.y = y
        self.channel = channel
        self.power_level = power_level
        self.frequency = frequency
        self.standard = standard
        self.supports_11k = supports_11k
        self.supports_11v = supports_11v
        self.supports_11r = supports_11r
        self.coverage_radius = coverage_radius
        self.device_limit = device_limit
        self.minimal_rssi = minimal_rssi
        self.connected_clients = []
        self.log = []

class Client:
    def __init__(self):
        pass

