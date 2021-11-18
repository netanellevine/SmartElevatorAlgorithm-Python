from Elevator import Elevator


def calculate_route(call, elev):
    # 1 for UP -1 for DOWN
    call_type = -1 if call.src > call.dest else 1
    src_floor = call.src
    dest_floor = call.dest
    starting_time = call.runTime
    # elev.curr_pos()
    elev_pos = elev.whereAtTime(starting_time)
    elev_state = elev.state
    estimated_time = 0
    ALLOCATE_STATE = 0
    # OPTIONS to add ->
    # call is up:
    # 1 -> route up is empty and pos < src < dest
    # 1 -> src in route up, dest in route up
    # 2 -> route up is empty but pos > src < dest
    # 2 -> src in route down, dest in route up
    # 3 -> route up is not empty and pos > src < dest
    # 3 -> src in route down, dest in route up
    # 4 -> route up is not empty and pos < src < dest
    # 4 -> src in route up, dest in route up
    # call is down:
    # 5 -> route down is empty and pos > src > dest
    # 5 -> src in route down, dest in route down
    # 6 -> route down is empty but pos < src > dest
    # 6 -> src in route up, dest in route down
    # 7 -> route down is not empty and pos < src > dest
    # 7 -> src in route up, dest in route down
    # 8 -> route down is not empty and pos > src > dest
    # 8 -> src in route down, dest in route down
    #
    # call is up
    # and (elev_state == 1 or elev_state == 0)
    if call_type == 1:
        elev_route = elev.up.copy()
        # CASE 1 ->
        if len(elev_route) == 0 and elev_pos < src_floor < dest_floor:
            # route is empty
            estimated_time = elev.get_distance(elev_pos, src_floor) + elev.get_distance(src_floor, dest_floor)
            ALLOCATE_STATE = 1
        # CASE 2 ->
        elif len(elev_route) == 0 and elev_pos > src_floor < dest_floor:
            last_pos = elev_pos
            elev_route = elev.down.copy()
            elev_route.append(src_floor)
            elev_route.sort(reverse=True)
            for floor in elev_route:
                # start to go over all the calls down
                estimated_time += elev.get_distance(last_pos, floor)
                last_pos = floor
            estimated_time += elev.get_distance(last_pos, dest_floor)
            # + max(estimated_time * (len(elev_route) / 2), estimated_time)
            ALLOCATE_STATE = 2

        # CASE 3 ->
        elif len(elev_route) != 0 and elev_pos > src_floor < dest_floor:
            # if the pos of the elev is grater then the src floor ->
            # first finish all the calls up
            # second start doing all the calls down and add the src floor
            # third add the dest to the new route up and finish that call
            last_pos = elev_pos
            for floor in elev_route:
                # finish all the calls up
                estimated_time += elev.get_distance(last_pos, floor)
                last_pos = floor
            # estimated_time += estimated_time * (len(elev_route) / 2)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            elev_route = elev.down.copy()
            # add the src floor
            elev_route.append(src_floor)
            elev_route.sort(reverse=True)
            for floor in elev_route:
                # start to go over all the calls down
                estimated_time += elev.get_distance(last_pos, floor)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            estimated_time += elev.get_distance(last_pos, dest_floor)
            # + max(estimated_time * (len(elev_route) / 4), estimated_time)
            ALLOCATE_STATE = 3
        # CASE 4 ->
        else:
            # route is not empty and src + dest are up
            last_pos = elev_pos
            elev_route.append(src_floor)
            elev_route.append(dest_floor)
            elev_route.sort()
            for floor in elev_route:
                estimated_time += elev.get_distance(last_pos, floor)
                last_pos = floor
            # estimated_time = max(estimated_time * (len(elev_route) / 2), estimated_time)
            ALLOCATE_STATE = 4
    # call is down
    # and (elev_state == 0 or elev_state == -1)
    elif call_type == -1:
        elev_route = elev.down.copy()
        # CASE 5 ->
        if len(elev_route) == 0 and elev_pos > src_floor > dest_floor:
            # route is empty
            estimated_time = elev.get_distance(elev_pos, src_floor) + elev.get_distance(src_floor, dest_floor)
            ALLOCATE_STATE = 5
        # CASE 6 ->
        if len(elev_route) == 0 and elev_pos < src_floor > dest_floor:
            last_pos = elev_pos
            elev_route = elev.up.copy()
            elev_route.append(src_floor)
            elev_route.sort()
            for floor in elev_route:
                # start to go over all the calls up
                estimated_time += elev.get_distance(last_pos, floor)
                last_pos = floor
            estimated_time += elev.get_distance(last_pos, dest_floor)
            # + max(estimated_time * (len(elev_route) / 4), estimated_time)
            ALLOCATE_STATE = 6
        # CASE 7 ->
        elif len(elev_route) != 0 and elev_pos < src_floor > dest_floor:
            # if the pos of the elev is lower than the src
            # first finish all the calls down
            # second start doing all the calls up and add the src floor
            # third add the dest to the new route down and finish that call
            for floor in elev_route:
                # finish all the calls down
                estimated_time += elev.get_distance(elev_pos, floor)
            # estimated_time = estimated_time * (len(elev_route) / 2)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            elev_route = elev.up.copy()
            # add the src floor
            elev_route.append(src_floor)
            elev_route.sort()
            for floor in elev_route:
                # start to go over all the calls up
                estimated_time += elev.get_distance(last_pos, floor)
            # save the last pos of the elevator
            last_pos = elev_route[len(elev_route) - 1]
            estimated_time += elev.get_distance(last_pos, dest_floor)
            # + max(estimated_time * (len(elev_route) / 4), estimated_time)
            ALLOCATE_STATE = 7
        # CASE 8 ->
        else:
            # route is not empty and src + dest are down
            elev_route.append(src_floor)
            elev_route.append(dest_floor)
            elev_route.sort(reverse=True)
            for floor in elev_route:
                estimated_time += elev.get_distance(elev_pos, floor)
            # estimated_time = max(estimated_time * (len(elev_route) / 4), estimated_time)
            ALLOCATE_STATE = 8
    return estimated_time, ALLOCATE_STATE


class MyAlgo:
    def __init__(self, building, calls):
        self.building = building
        self.calls = calls
        self.elevators = building.elevators
        self.route_up = [[]] * len(self.elevators)
        self.route_down = [[]] * len(self.elevators)

    # def allocate_an_elevator(self, call):
    #     call_type = 1 if call.src < call.dest else -1
    #     src_floor = call.src
    #     dest_floor = call.dest
    #     starting_time = call.runTime
    #     MIN_estimated_time = 2**20
    #     ind_of_elev = -1
    #     allocate_state = 0
    #     for elev in self.elevators:
    #         curr_estimated_time, curr_allocate_state = calculate_route(call, elev)
    #         if curr_estimated_time < MIN_estimated_time:
    #             MIN_estimated_time = curr_estimated_time
    #             ind_of_elev = elev.id
    #             allocate_state = curr_allocate_state
    #     # add to the list of calls
    #     self.elevators[ind_of_elev].calls_list.append(call)
    #     # CASE 1 or CASE 4 ->
    #     if allocate_state == 1 or allocate_state == 4:
    #         route1 = self.route_up[ind_of_elev]
    #         route1.append(src_floor)
    #         route1.append(dest_floor)
    #         route1.sort()
    #         self.route_up[ind_of_elev] = route1
    #     # CASE 2 or CASE 3 ->
    #     elif allocate_state == 2 or allocate_state == 3:
    #         route1 = self.route_down[ind_of_elev]
    #         route1.append(src_floor)
    #         route1.sort(reverse=True)
    #         self.route_down[ind_of_elev] = route1
    #         route1 = self.route_up[ind_of_elev]
    #         route1.append(dest_floor)
    #         route1.sort()
    #         self.route_up[ind_of_elev] = route1
    #     # CASE 5 or CASE 8 ->
    #     elif allocate_state == 5 or allocate_state == 8:
    #         route1 = self.route_down[ind_of_elev]
    #         route1.append(src_floor)
    #         route1.append(dest_floor)
    #         route1.sort(reverse=True)
    #         self.route_down[ind_of_elev] = route1
    #     # CASE 6 or CASE 7 ->
    #     elif allocate_state == 6 or allocate_state == 7:
    #         route1 = self.route_up[ind_of_elev]
    #         route1.append(src_floor)
    #         route1.sort()
    #         self.route_up[ind_of_elev] = route1
    #         route1 = self.route_down[ind_of_elev]
    #         route1.append(dest_floor)
    #         route1.sort(reverse=True)
    #         self.route_down[ind_of_elev] = route1
    #     return ind_of_elev

    def allocate_an_elevator(self, call):
        if len(self.building.elevators) == 1:
            return 0
        call_type = 1 if call.src < call.dest else -1
        src_floor = call.src
        dest_floor = call.dest
        max_floor = max(int(src_floor), int(dest_floor))
        num_of_floors = abs(int(self.building.minFloor) - int(self.building.maxFloor))
        num_of_elevators = len(self.building.elevators)
        section_length = num_of_floors / int(num_of_elevators)
        index_to_allocate = int(int(max_floor) / int(section_length))
        id_of_allocated = self.building.elevators[index_to_allocate].id
        return id_of_allocated
