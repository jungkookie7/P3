import math

class AccessPoint:
    def __init__(self, name, x, y, channel, power_level,
                 frequency, standard, supports_11k, supports_11v,
                 supports_11r, coverage_radius, device_limit,
                 minimal_rssi = None): #Minimal_rssi value defaults None because it is optional
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

    def connect(self, client):
        if len(self.connected_clients) >= self.device_limit:
            self.log.append(f'{client.name} TRIED {self.name} BUT WAS DENIED')
            return False
        else:
            self.connected_clients.append(client)
            self.log.append(f'{client.name} CONNECT LOCATION {client.x}{client.y} {client.supported_standards[0]} {client.frequency}')
            return True

    def disconnect(self, client):
        if client in self.connected_clients:
            self.connected_clients.remove(client)
            self.log.append(f'{client.name} DISCONNECTS AT LOCATION {client.x}{client.y}')

    def rssi(self, client):
        distance_x = self.x - client.x
        distance_y = self.y - client.y
        distance_x_y = (distance_x ** 2) + (distance_y ** 2)
        distance = math.sqrt(distance_x_y)
        log_distance = 20 * math.log10(distance)
        log_frequency = 20 * math.log10(client.frequency)
        rssi = client.power_level - log_distance - log_frequency - 32.44
        return rssi


class Client:
    def __init__(self, name, x, y, standard, speed,
                 supports_11k, supports_11v, supports_11r,
                 minimal_rssi):
        self.name = name
        self.x = x
        self.y = y
        self.standard = standard
        self.speed = speed
        self.supports_11k = supports_11k
        self.supports_11v = supports_11v
        self.supports_11r = supports_11r
        self.minimal_rssi = minimal_rssi
        self.connected_ap = None
        self.step = 0
        self.log = []

    def move(self, new_x, new_y):
        self.new_x = new_x
        self.new_y = new_y
        self.step = self.step + 1
        self.log.append(f'STEP {self.step} MOVED TO {self.new_x}{self.new_y}')

    def roam(self, client):
        pass
        """
        Move between different access points
            client checks signals between points
            choosing which point is strongest to connect too
            disconnect if finds one stronger, connecting to stronger one
            logs it
        """

class AccessController():
    def __init__(self):
        self.log = []

def main():
    """
    TEST SAMPLE
    AP AP1 0 0 6 20 2.4/5 WiFi6 true true true 50 10 75
    AP AP2 100 100 6 20 5 WiFi7 false true false 40 60
    CLIENT Client1 10 10 WiFi6 2.4/5 true true true 73
    MOVE Client1 10 9
    """

    ap = AccessPoint("AP1", 0, 0, 6, 20, 2.4, "WiFi6", True, True, True, 50, 10, 75)
    ap2 = AccessPoint("AP2", 100, 100, 6, 20, 5, "WiFi7", False, True, False, 40, 60)

    client = Client("Client1", 10, 10, "WiFi6", 2.4, True, True, True, 73)

    client.move(10, 9)
    client.roam([ap, ap2])

    print(client.log)
    print(ap.log)
    print(ap2.log)

if __name__ == "__main__":
    main()

