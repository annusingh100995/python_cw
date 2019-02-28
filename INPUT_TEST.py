class Step_Current:
    def Step_Current(self):
        print("Enter the current and time step:")
        self.current, self.timestep  = input().split()
        print("The current is : ",self.current )
        print("The current is : ", self.timestep)
        return Step_Current()