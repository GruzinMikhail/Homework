class Road:
    weigth = None
    tickness = None
    __length = None
    __width = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Проложить дорогу к поселку')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Нужно {intake} тон для строительства')

road_to_village = Road(20000, 6)
road_to_village.intake()