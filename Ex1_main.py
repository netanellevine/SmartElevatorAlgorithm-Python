import Reader_writer
import sys

def main():
    try:
        building_file = sys.argv[1]
        csv_file = sys.argv[2]
        file_name = sys.argv[3]
        Reader_writer.read_calculate_write(building_file, csv_file, file_name)
    except:
        output = ""
        try:
            output = sys.argv[1]
        except:
            output = "output"
        buildings = ["./building_files/B1.json", "./building_files/B2.json", "./building_files/B3.json", "./building_files/B4.json", "./building_files/B5.json"]
        calls_cases = ["./call_files/calls_a.csv", "./call_files/calls_b.csv", "./call_files/calls_c.csv", "./call_files/calls_d.csv"]
        Reader_writer.read_calculate_write(buildings[0], calls_cases[0], f'{output}_B1_a.csv')
        Reader_writer.read_calculate_write(buildings[1], calls_cases[0], f'{output}_B2_a.csv')
        ind = 3
        for i in range(2, 5):
            ch = chr(97)
            ind1 = 1
            for j in calls_cases:
                st = output+"_B" + str(ind) + "_" + ch + ".csv"
                Reader_writer.read_calculate_write(buildings[i], j, st)
                ch = chr(97 + ind1)
                ind1 += 1
            ind += 1

if __name__ == "__main__":
    main()
