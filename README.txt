

CSC8311- Advanced Python Programming 

**CSC8311_Final_Submission.Py ** Is My Final Submission. 

I tried to model Hodgkin Huxley equations. The Hodgkin Huxley model is a set of equations that models the potential of single neuron. The basic idea is that, the neuron is stimulated with a simulation current provided by the user and the resulting action potential is measured with respect to time.

The simulation current is time dependent.It can be constant or varying in step function.

I tried to implement the HH model. 

The current version, takes in the input (either 1 or 2 ). If “1” is given as the input the step current is used for simulating the neuron and the corresponding figures are plotted.

If “2” is given as an input the step current is used for simulation and the corresponding figures are plotted.

The program as of now, plots the simulation current with respect to time, the action potential measured with respect to time and the trajectories.

The user can edit the code and change the magnitude of the step and constant current according to their experiment.

The program has two methods for calcutating the solving the differential equations and based on the user input , the program selects the either the constant current system or the step curernt system. 


I have included the version control file in the folder.



I tried to generalise my code, so that the user can select the type of current for simulation (constant/step) and then input the magnitude of current .I did try implement this,but was not able to debug the code and make the functions compatible with each other and the ode function.



I tried to make a method that will take in the magnitude of current, time step from the user and raise error if the input is not a float type.


class Current:
      def constant_current(self):
            print("Enter the magnitude of current ")
            self.current= float(input())

            if not isinstance(self.current,float):
                raise TypeError("NOT A NUMBER")
            else:
                return self.current

      def step_current(self):
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



In the following piece of code, I tried to make a method that will return an array of current values. I made the code work to give me a step current. But was not able to make it compatible with the ode funcion.

In this piece fo code,
1. I divide the simulation time in number of windows , given a user defined time step.
2. Take all the odd numbered windows and set them to the current magnitude (given by user) to give  me an array with alternative/step current.
3. I take the odd numbered window, (which is of size = window size) and set every element of the window to be equal to the current givenby yser.

      def Step_current(self):
	  current_magnitude = current.step_current
          current = np.zeros(len(T))
          current_length = len(current)

		
          window_size = current.time_step
          number_of_windows = current_length/window_size
          updated_current = current
		# number list stores the odd numbered window
          number_list = np.arange(1,number_of_windows,2)
          for i in number_list:
              for j in range(1,window_size):
                  temp = int(((i*window_size)+j))
                  updated_current[temp] = current_magnitude
                  return updated_current



