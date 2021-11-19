import unittest

import Reader_writer
from Building import Building
import pandas as pd
import os

# this script will auto clean the files it creates
class Test(unittest.TestCase):
    def test_B3_B4_B5(self):
        buildings = ["./building_files/B3.json", "./building_files/B4.json", "./building_files/B5.json"]
        calls_cases = ["./call_files/calls_a.csv", "./call_files/calls_b.csv", "./call_files/calls_c.csv", "./call_files/calls_d.csv"]
        ind = 2
        print("testing that each elevator has more than 10 calls in building 3 to 5")
        for building in buildings:
            for case in calls_cases:
                Reader_writer.read_calculate_write(building, case, f'output{ind}')
                calls = Reader_writer.calls_from_CSV(case)
                file = pd.read_csv(f'output{ind}', header=None)
                # amount of calls are the same after  the change
                self.assertTrue(len(calls.calls) == len(file.index))
                ind += 1
                for k in file[5].value_counts():
                    # each elev should have at least 10 calls
                    self.assertTrue(k > 10)
        print("test succeeded")
        for building in range(2, 14):
            if os.path.exists(f'output{building}'):
                os.remove(f'output{building}')
            else:
                print(f'The file output{building} does not exist')

    def test_B1_B2(self):

        ind = 0
        print("checks that every call in building 1 goes to 0")
        Reader_writer.read_calculate_write("./building_files/B1.json", "./call_files/calls_a.csv", f'output{ind}')
        calls = Reader_writer.calls_from_CSV("./call_files/calls_a.csv")
        file = pd.read_csv(f'output{ind}', header=None)
        self.assertTrue(len(calls.calls) == len(file.index))
        print("test succeeded")
        ind += 1
        print("checks that in building 2 fast elevator gets more than 60% calls and slow more than 30%")
        # first elev should have all the calls because there is only 1 elevator
        self.assertTrue(file[5].value_counts()[0] >= len(file.index))
        Reader_writer.read_calculate_write("./building_files/B2.json", "./call_files/calls_a.csv", f'output{ind}')
        file = pd.read_csv(f'output{ind}', header=None)
        self.assertTrue(len(calls.calls) == len(file.index))
        self.assertTrue(file[5].value_counts()[0] >= len(file.index) * 0.3)
        # fast elev should get most of the calls
        self.assertTrue(file[5].value_counts()[1] >= len(file.index) * 0.6)
        print("test succeeded")
        # delete files
        for i in range(2):
            if os.path.exists(f'output{i}'):
                os.remove(f'output{i}')
            else:
                print(f'The file output{i} does not exist')
    #this test checks that we don't modify anything but the allocated to part
    def test_dont_change_calls(self):
        print("Checks that the calls haden't been modified except from elev index and checks that elev index is not -1")
        buildings = ["./building_files/B3.json", "./building_files/B4.json", "./building_files/B5.json"]
        calls_cases = ["./call_files/calls_a.csv", "./call_files/calls_b.csv", "./call_files/calls_c.csv", "./call_files/calls_d.csv"]
        ind = 15
        for building in buildings:
            for case in calls_cases:
                Reader_writer.read_calculate_write(building, case, f'output{ind}')
                calls = Reader_writer.calls_from_CSV(case)
                file = pd.read_csv(f'output{ind}', header=None)
                ind += 1
                # amount of calls are the same after  the change
                self.assertTrue(len(calls.calls) == len(file.index))
                for i in range(len(calls.calls)):
                    self.assertTrue(file[0][i] == calls.calls[i].kind)
                    self.assertTrue(file[1][i] == calls.calls[i].runTime)
                    self.assertTrue(file[2][i] == calls.calls[i].src)
                    self.assertTrue(file[3][i] == calls.calls[i].dest)
                    self.assertTrue(file[4][i] == calls.calls[i].status)
                    self.assertTrue(file[5][i] != - 1)
        print("test succeeded")
        for building in range(15, ind):
            if os.path.exists(f'output{building}'):
                os.remove(f'output{building}')
            else:
                print(f'The file output{building} does not exist')


if __name__ == '__main__':
    unittest.main()
