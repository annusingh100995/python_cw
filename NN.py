class Current:
      def constant_current(self):
          while True:
              print("Enter the value of current")
              self.current=input()
              if not isinstance(self.current,int):
                  raise TypeError("Input integars only")
              else:
                  break
          return self.current

      def step_current(self):
            print("Enter the magnitude of current")
            self.current=input()
            return self.current
      def time_step(self):
            print("Enter the time step")
            self.time_step = input()
            return self.time_step


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


