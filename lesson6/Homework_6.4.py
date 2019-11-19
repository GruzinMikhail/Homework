class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "Машина едит"
    def stop(self):
        return "Машина стоит"
    def turn(self, direction):
        return "Машина повернула в сторону " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

mustang = TownCar('shelby', 60, 'Черный')
print(mustang.name, mustang.color, mustang.speed, mustang.is_police)
print(mustang.go(), mustang.turn('Аэропорта'), mustang.stop())
sport = SportCar(' GT', 180, 'Желтый')
work1 = WorkCar('Reno', 90, 'Белое', True)
work2 = WorkCar('Subaru', 90, 'Золотой', False)
police = PoliceCar('Ford', 180, 'Черно, белай')