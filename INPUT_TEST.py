class Current:

    def constant_current(self):
        print("Enter the magnitude of current ")
        self.current = input()
        return self.current

    def step_current(self):
        print("Enter the magnitude of current")
        self.current = input()
        return self.current

    def Step_Current(self):
        print("Enter the current and time step:")
        self.current, self.timestep  = input().split()
        print("The current is : ",self.current )
        print("The current is : ", self.timestep)



        return Step_Current()








def main():
    current = Current()
    input_current = 0
    time_step = 0

    print(""" ======CURRENT MENU=======
                  1. Constant Current
                  2. Step Current
                  """)
    choice=int(input("Enter Choice:"))
    if choice==1:
        input_current = current.constant_current()
    elif choice==2:
        input_current = current.step_current()
        time_step = current.time_step()
    else:
        print("ERROR:INVALID CURRENT")
        sys.exit()
    print(input_current)
    print(time_step)
main()
