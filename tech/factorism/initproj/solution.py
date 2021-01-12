class FactorHandler:

    def __init__(self):
        self.list = []

    def fix_time_format(self, time_format, time):
        time_format = time_format.split('/')
        time = time.split('/')
        time_reserve = [0, 0, 0]
        for i in range(len(time_format)):
            if time_format[i] == 'dd':
                time_reserve[2] = time[i]
            elif time_format[i] == 'mm':
                time_reserve[1] = time[i]
            elif time_format[i] == 'yyyy':
                time_reserve[0] = time[i]

        # print(time_reserve)
        return "".join(time_reserve)



    def add_factor(self, time_format, time, value):
        formats = self.fix_time_format(time_format, time)
        for i in self.list:
            if i[0] == formats:
                # print("begin")
                # print(i[1])
                # print('finish')
                i[1] += value

                return
        self.list.append([formats, value])

    def remove_all_factors(self, time_format, time):
        formats = self.fix_time_format(time_format, time)
        for i in self.list:
            if i[0] == formats:
                i[1] = 0
        

    def get_sum(self, time_format, start_time, finish_time):
        start = self.fix_time_format(time_format, start_time)
        finish = self.fix_time_format(time_format, finish_time)
        calc = 0
        for i in self.list:
            if i[0] <= finish and i[0] >= start:
                calc += i[1]

        return calc

# fh = FactorHandler()
# fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
# fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10"))


