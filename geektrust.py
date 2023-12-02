import sys

class vehicle_train:
    def __init__(self, data_input):
        self.data_input = data_input
        self.station_after_hyb = {"HYB": 0, "NGP": 400, "ITJ": 700, "BPL": 800,
                                  "AGA": 2500, "NDL": 2700, "PTA": 3800, "NJP": 4200, "GHY": 4700}
        self.dept_train = []

    def print_train_a(self, input_data):
        arr_a = ['ARRIVAL', 'TRAIN_A', 'ENGINE']
        arr = []
        temp_boggie = []
        for i in range(2, len(input_data)):
            if input_data[i].strip() in self.station_after_hyb:
                arr.append(input_data[i])
                train_obj = {"name": input_data[i].strip(),
                             "id": self.station_after_hyb[input_data[i].strip()]}
                temp_boggie.append(train_obj)

        boggie_list = arr_a + arr
        boggie = ' '.join(map(str, boggie_list)).replace(",", "")
        print(boggie.strip())
        return temp_boggie

    def print_train_b(self, input_data):
        arr_a = ['ARRIVAL', 'TRAIN_B', 'ENGINE']
        arr = []
        temp_boggie = []
        for i in range(2, len(input_data)):
            if input_data[i].strip() in self.station_after_hyb:
                arr.append(input_data[i])
                train_obj = {"name": input_data[i].strip(),
                             "id": self.station_after_hyb[input_data[i].strip()]}
                temp_boggie.append(train_obj)

        boggie_list = arr_a + arr
        boggie = ' '.join(map(str, boggie_list)).replace(",", "")
        print(boggie.strip())
        return temp_boggie


class Vehicle:
    def __init__(self, data_input):
        self.data_input = data_input
        self.station_after_hyb = {"HYB": 0, "NGP": 400, "ITJ": 700, "BPL": 800,
                                  "AGA": 2500, "NDL": 2700, "PTA": 3800, "NJP": 4200, "GHY": 4700}
        self.dept_train = []
        self.dept_train1 = []
        self.dept_train2 = []
        self.vehicle_train = vehicle_train(data_input)

    def main(self):
        input_lines = self.data_input.split("\n")
        input_lines = list(filter(lambda s: len(s.strip()) != 0, input_lines))

        for line in input_lines:
            if line:
                input_data = line.split(' ')
                if input_data[0] == 'TRAIN_A':
                    self.dept_train1 = self.vehicle_train.print_train_a(input_data)
                elif input_data[0] == 'TRAIN_B':
                    self.dept_train2 = self.vehicle_train.print_train_b(input_data)

        start_boggie = ['DEPARTURE', 'TRAIN_AB', 'ENGINE', 'ENGINE']
        self.dept_train = self.dept_train1 + self.dept_train2
        self.dept_train.sort(key=lambda x: x['id'], reverse=True)

        boggie_list_to_array = [b['name'] for b in self.dept_train if b['id'] != 0]
        boggie_list = start_boggie + boggie_list_to_array
        boggie = ' '.join(boggie_list).replace("HYB", "").strip()
        print(boggie)


if __name__ == "__main__":
    filename = sys.argv[1]
    data = open(sys.argv[1]).read()
    train1 = Vehicle(data)
    train1.main()

