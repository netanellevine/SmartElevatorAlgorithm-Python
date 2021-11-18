import csv
import json

import MyAlgo
from Building import Building
from Call import Call
from Calls import Calls
from Elevator import Elevator
import LookAlgo


def building_from_json(file_name):
    f = open(file_name)
    data = json.load(f)
    f.close()
    l1 = []
    for Any in data['_elevators']:
        l1.append(Elevator(Any))
    b = Building(l1)
    b.sort_by_speed()
    return b


def calls_from_CSV(file_name):
    f = open(file_name)
    csv_reader = csv.reader(f)
    li = []
    for call in csv_reader:
        li.append(Call(call))
    return Calls(li)


def write_to_csv(list_of_calls, ind):
    # https://www.pythontutorial.net/python-basics/python-write-csv-file/
    data = open("output" + str(ind) + ".csv", "w", newline='')
    writer = csv.writer(data)
    for i in list_of_calls.calls:
        li = [i.kind, i.runTime, i.src, i.dest, i.status, i.allocatedTo]
        writer.writerow(li)
    data.close()


def read_calculate_write(building_file, calls_file, ind):
    curr_building = building_from_json(building_file)
    curr_calls = calls_from_CSV(calls_file)
    algo = MyAlgo.MyAlgo(curr_building, curr_calls)
    for call in algo.calls.calls:
        call.allocatedTo = algo.allocate_an_elevator(call)

    write_to_csv(algo.calls, ind)
    # try:
    #     with open(building_file) as parser:
    #         building = json.load(parser)
    # except:
    #     print("The file is not a Json file!!")
    # curr_building = Building(building)
    # ind = 0
    # for elev in building['_elevators']:
    #     curr_building.elevators.appand(ind, elev)
    #     ind += 1
    # try:
    #     calls_data = pd.read_csv(calls_file, header=None)
    #     output_file = pd.read_csv(calls_file, header=None)
    # except:
    #     print("The file is not a CSV file!!")



b = building_from_json("B5.json")
speed_of_elevators = []
# for elevator in b.elevators:
#     speed_of_elevators.append(elevator.speed)
# speed_of_elevators.sort()
# print(speed_of_elevators)
# new_sorted_elevators = []
# for i in range(0, len(speed_of_elevators)):
#     current_speed = speed_of_elevators[i]
#     current_elevator = ""
#     for elevator in b.elevators:
#         current_elev_speed = elevator.speed
#         if current_elev_speed == current_speed:
#             current_elevator = elevator
#         break
#     new_sorted_elevators.append(current_elevator)
# b.to_string()
b.sort_by_speed()
for elevator in b.elevators:
    print(elevator.speed)
# f = calls_from_CSV("Calls_d.csv")
# f.alloc(b)
# f.write_to_csv()