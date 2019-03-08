CSC8311 Advanced Python Prgramming 

CSC8311- Advanced Python Programming 

I tried to model Hodgkin Huxley equations. The Hodgkin Huxley model is a set of equations that models the potential of single neuron. The basic idea is that, the neuron is stimulated with a simulation current provided by the user and the resulting action potential is measured with respect to time.

The simulation current is time dependent.It can be constant or varying in step function.

I tried to implement the HH model. 

The current version, takes in the input (either 1 or 2 ). If “1” is given as the input the step current is used for simulating the neuron and the corresponding figures are plotted.

If “2” is given as an input the step current is used for simulation and the corresponding figures are plotted.

The program as of now, plots the simulation current with respect to time, the action potential measured with respect to time and the trajectories.

The user can edit the code and change the magnitude of the step and constant current according to their experiment.

I have included the version control file in the folder.

I tried to generalise my code, so that the user can select the type of current for simulation (constant/step) and then input the magnitude of current .I did try implement this,but was not able to debug the code and make the functions compatible with each other and the ode function.


