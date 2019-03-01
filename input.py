class Current:
      def Input_constant_current(self):
            print("Enter the magnitude of current ")
            self.current= float(input())
            if not isinstance(self.current,float):
                raise TypeError("NOT A NUMBER")
            else:
                return self.current

      def Input_step_current(self):
            print("Enter the magnitude of current")
            self.current=float(input())
            if not isinstance(self.current,float):
                raise TypeError("NOT A NUMBER")
            else:
                return self.current

      def Input_time_step(self):
            print("Enter the time step")
            self.time_step = float(input())
            if not isinstance(self.time_step, float):
                raise TypeError("NOT A NUMBER")
            else:
                return self.time_step

      def Simulation_current(self):
          


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
        input_current = current.Input_constant_current()
    elif choice==2:
        input_current = current.Input_step_current()
        time_step = current.Input_time_step()
    else:
        print("ERROR:INVALID CURRENT")
        sys.exit()
    print(input_current)
    print(time_step)
main()
