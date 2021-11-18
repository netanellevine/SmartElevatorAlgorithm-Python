import Json
import numpy as np


def main():
    buildings = ["B1.json", "B2.json", "B3.json", "B4.json", "B5.json"]
    calls_cases = ["calls_a.csv", "calls_b.csv", "calls_c.csv", "calls_d.csv"]
    buildings = ["B1.json", "B2.json", "B3.json", "B4.json", "B5.json"]
    calls_cases = ["calls_a.csv", "calls_b.csv", "calls_c.csv", "calls_d.csv"]
    Json.read_calculate_write(buildings[1], calls_cases[0], "_B1_a")
    Json.read_calculate_write(buildings[0], calls_cases[0], "_B2_a")
    ind = 3
    for i in range(2, 5):
        ch = chr(97)
        ind1 = 1
        for j in calls_cases:
            st = "_B" + str(ind) + "_" + ch
            Json.read_calculate_write(buildings[i], j, st)
            ch = chr(97 + ind1)
            ind1 += 1
        ind += 1


if __name__ == "__main__":
    main()
