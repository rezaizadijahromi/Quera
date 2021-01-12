class FactorHandler:
    def __init__(self):
        self.list = []

    def add_factor(self, fmt, time, val):
        local = self.__internal_format__(fmt, time)
        for i in self.list:
            if i[0] == local:
                i[1] += val
                return
        self.list.append([local, val])

    def remove_all_factors(self, fmt, time):
        local = self.__internal_format__(fmt, time)
        for i in self.list:
            if i[0] == local:
                i[1] = 0

    def get_sum(self, fmt, start, finish):
        start = self.__internal_format__(fmt, start)
        finish = self.__internal_format__(fmt, finish)
        res = 0
        for i in self.list:
            if i[0] >= start and i[0] <= finish:
                res += i[1]
        return res

    def __internal_format__(self, fmt, time):
        fmt = fmt.split("/")
        time = time.split("/")
        res = [0, 0, 0]
        for i in range(len(fmt)):
            if fmt[i] == "dd":
                res[2] = time[i]
            elif fmt[i] == "mm":
                res[1] = time[i]
            else:
                res[0] = time[i]
        return "".join(res)