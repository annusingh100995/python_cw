class Current:
      def constant_current(self):
            print("Enter the magnitude of current ")
            self.current= float(input())

            if not isinstance(self.current,float):
                raise TypeError("NOT A NUMBER")
            else:
                return self.current

      def step_current(t):
            print("Enter the magnitude of current")
            self.current=float(input())
            if not isinstance(self.current,float):
                raise TypeError("NOT A NUMBER")
            else:
                return self.current

      def time_step(self):
            print("Enter the time step")
            self.time_step = input()
            return self.time_step

      def Step_current(t):
          current = np.zeros(len(T))
          current_length = len(current)
          window_size = self.time_step
          number_of_windows = current_length/window_size
          updated_current = current
          number_list = np.arange(1,number_of_windows,2)
          for i in number_list:
              for j in range(1,window_size):
                  temp = int(((i*window_size)+j))
                  updated_current[temp] = 10
                  return updated_current




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
