import Elevator


class Building:

    def __init__(self, elevators):
        self.maxFloor = elevators[0].maxFloor
        self.elevators = elevators
        self.minFloor = elevators[0].minFloor
        self.total_speed = sum([a.speed for a in elevators])
        self.grade_of_Speed()

    def getElev(self, elev):
        return self.elevators[elev]

    def grade_of_Speed(self):
        for a in self.elevators:
            a.jump = a.speed / self.total_speed

    def sort_by_speed(self):
        self.elevators.sort(key=lambda x: x.speed)

    def to_string(self):
        return str(self.elevators)
