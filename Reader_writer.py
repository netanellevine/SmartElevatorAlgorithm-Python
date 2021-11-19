import csv
import json

import MyAlgo
from Building import Building
from Call import Call
from Calls import Calls
from Elevator import Elevator


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
    f.close()
    return Calls(li)


def write_to_csv(list_of_calls, file_name="output.csv"):
    # https://www.pythontutorial.net/python-basics/python-write-csv-file/
    data = open(file_name, "x", newline='')
    writer = csv.writer(data)
    for i in list_of_calls.calls:
        li = [i.kind, i.runTime, i.src, i.dest, i.status, i.allocatedTo]
        writer.writerow(li)
    data.close()


def read_calculate_write(building_file, calls_file, file_name="output.csv"):
    curr_building = building_from_json(building_file)
    curr_calls = calls_from_CSV(calls_file)
    algo = MyAlgo.MyAlgo(curr_building, curr_calls)
    for call in algo.calls.calls:
        call.allocatedTo = algo.allocate_an_elevator(call)
    write_to_csv(algo.calls, file_name)
