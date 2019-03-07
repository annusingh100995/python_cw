def Id(t):
    for t in T:
        return current[t]
class Current:
    def Constant_current(t):
        print("Enter the magnitude of current ")
        input_current = float(input())
        if not isinstance(input_current, float):
            raise TypeError("NOT A NUMBER")
        # else:
            #current = np.zeros(len(T))
            current_length = len(current)
            # for t in range(0,current_length):
            #    temp = int(t)
            #    current[temp] = input_current
        return input_current


    def time_step(self):
        print("Enter the time step")
        self.time_step = input()
        return self.time_step

    def Step_current(self):
        current = np.zeros(len(T))
        current_length = len(current)
        window_size = self.time_step
        number_of_windows = int((current_length/window_size))
        updated_current = current
        number_list = np.arange(1, number_of_windows, 2)
        for i in number_list:
            for j in range(1, window_size):
                temp = int(((i * window_size) + j))
                updated_current[temp] = 10

        for t in T:
            return updated_current(t)


    def CC(t):
        if tmin < t < tmax:
            return 15
 idv = [CC(t) for t in T]
