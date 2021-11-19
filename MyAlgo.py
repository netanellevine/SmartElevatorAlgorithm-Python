from Elevator import Elevator



class MyAlgo:
    def __init__(self, building, calls):
        self.building = building
        self.calls = calls
        self.elevators = building.elevators
        self.route_up = [[]] * len(self.elevators)
        self.route_down = [[]] * len(self.elevators)

    def allocate_an_elevator(self, call):
        if len(self.building.elevators) == 1:
            return 0
        src_floor = call.src
        dest_floor = call.dest
        max_floor = max(int(src_floor), int(dest_floor))
        num_of_floors = abs(int(self.building.minFloor) - int(self.building.maxFloor))
        num_of_elevators = len(self.building.elevators)
        section_length = num_of_floors / int(num_of_elevators)
        index_to_allocate = int(int(max_floor) / int(section_length))
        id_of_allocated = self.building.elevators[index_to_allocate].id
        return id_of_allocated

