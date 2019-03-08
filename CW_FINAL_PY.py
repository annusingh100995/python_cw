import numpy as np
import tkinter
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt

np.random.seed(1000)

# Start and end time (in milliseconds)
tmin = 0.0
tmax = 50.0

# Average potassium channel conductance per unit area (mS/cm^2)
gK = 36.0

# Average sodoum channel conductance per unit area (mS/cm^2)
gNa = 120.0

# Average leak channel conductance per unit area (mS/cm^2)
gL = 0.3

# Membrane capacitance per unit area (uF/cm^2)
Cm = 1.0

# Potassium potential (mV)
VK = -12.0

# Sodium potential (mV)
VNa = 115.0

# Leak potential (mV)
Vl = 10.613

# Time values
T = np.linspace(tmin, tmax, 10000)



class Current:

    def Current_Magnitude(self):
        print("Enter the magnitude of current ")
        current_mag = float(input())


        if not isinstance(current_mag,float):
            raise TypeError("NOT A NUMBER")
        else:
            return current_mag

    def Time_step(self):
        print("Enter the time step")
        time_step = float(input())
        if not isinstance(time_step,float):
            raise TypeError("NOT A NUMBER")
        else:
            return time_step

def Constant_currnet(t):

    return 55

def Step_current(t):
    if 0.0 < t < 10.0:
        return 0.0
    elif 10.0 < t < 20.0:
        return 150.0
    elif 20.0 < t < 30.0:
        return 0.0
    elif 30.0 < t < 40.0:
        return 150.0
    elif 40.0 < t < 50.0:
        return 0.0
    elif 50.0 < t < 60.0:
        return 50.0
    elif 60.0 < t < 70.0:
        return 50.0
    return 0.0


def alpha_n(Vm):
    return (0.01 * (10.0 - Vm)) / (np.exp(1.0 - (0.1 * Vm)) - 1.0)

def beta_n(Vm):
    return 0.125 * np.exp(-Vm / 80.0)

# Sodium ion-channel rate functions

def alpha_m(Vm):
    return (0.1 * (25.0 - Vm)) / (np.exp(2.5 - (0.1 * Vm)) - 1.0)

def beta_m(Vm):
    return 4.0 * np.exp(-Vm / 18.0)

def alpha_h(Vm):
    return 0.07 * np.exp(-Vm / 20.0)

def beta_h(Vm):
    return 1.0 / (np.exp(3.0 - (0.1 * Vm)) + 1.0)

# n, m, and h steady-state values

def n_inf(Vm=0.0):
    return alpha_n(Vm) / (alpha_n(Vm) + beta_n(Vm))

def m_inf(Vm=0.0):
    return alpha_m(Vm) / (alpha_m(Vm) + beta_m(Vm))

def h_inf(Vm=0.0):
    return alpha_h(Vm) / (alpha_h(Vm) + beta_h(Vm))



# Compute derivatives
def compute_derivatives(y, t0):

    dy = np.zeros((4,))

    Vm = y[0]
    n = y[1]
    m = y[2]
    h = y[3]

    # dVm/dt
    GK = (gK / Cm) * np.power(n, 4.0)
    GNa = (gNa / Cm) * np.power(m, 3.0) * h
    GL = gL / Cm

   # Current_type = Current_type()

    #if Current_type == 1:
    dy[0] = (Constant_currnet(t0)/ Cm) - (GK * (Vm - VK)) - (GNa * (Vm - VNa)) - (GL * (Vm - Vl))

   # elif Current_type == 2:
        #dy[0] = (Step_current(t0) / Cm) - (GK * (Vm - VK)) - (GNa * (Vm - VNa)) - (GL * (Vm - Vl))

    # dn/dt
    dy[1] = (alpha_n(Vm) * (1.0 - n)) - (beta_n(Vm) * n)

    # dm/dt
    dy[2] = (alpha_m(Vm) * (1.0 - m)) - (beta_m(Vm) * m)

    # dh/dt
    dy[3] = (alpha_h(Vm) * (1.0 - h)) - (beta_h(Vm) * h)

    return dy


def compute_derivatives_step(y, t0):
    dy = np.zeros((4,))

    Vm = y[0]
    n = y[1]
    m = y[2]
    h = y[3]

    # dVm/dt
    GK = (gK / Cm) * np.power(n, 4.0)
    GNa = (gNa / Cm) * np.power(m, 3.0) * h
    GL = gL / Cm

    # Current_type = Current_type()

    # if Current_type == 1:
    dy[0] = (Step_current(t0) / Cm) - (GK * (Vm - VK)) - (GNa * (Vm - VNa)) - (GL * (Vm - Vl))

    # elif Current_type == 2:
    # dy[0] = (Step_current(t0) / Cm) - (GK * (Vm - VK)) - (GNa * (Vm - VNa)) - (GL * (Vm - Vl))

    # dn/dt
    dy[1] = (alpha_n(Vm) * (1.0 - n)) - (beta_n(Vm) * n)

    # dm/dt
    dy[2] = (alpha_m(Vm) * (1.0 - m)) - (beta_m(Vm) * m)

    # dh/dt
    dy[3] = (alpha_h(Vm) * (1.0 - h)) - (beta_h(Vm) * h)

    return dy

def plot_current_density(Time,Current):
    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(Time, Current)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel(r'Current density (uA/$cm^2$)')
    ax.set_title('Stimulus (Current density)')
    fig = plt.grid()
    return fig

def plot_neuron_potential(Time,Voltage,Current_type):

    test = Current_type
    if test == 1:
        Vy = odeint(compute_derivatives, Voltage, Time)
    else:
        Vy = odeint(compute_derivatives_step, Voltage, Time)


    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(T, Vy[:, 0])
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Vm (mV)')
    ax.set_title('Neuron potential with two spikes')
    fig = plt.grid()
    return fig

def Plot_Trajectories(Y,Time,Current_type):

    test = Current_type
    if test == 1:
        Vy = odeint(compute_derivatives, Y, Time)
    else:
        Vy = odeint(compute_derivatives_step,Y, Time)

    Vy = odeint(compute_derivatives, Y, Time)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(Vy[:, 0], Vy[:, 1], label='Vm - n')
    ax.plot(Vy[:, 0], Vy[:, 2], label='Vm - m')
    ax.set_title('Limit cycles')
    ax.legend()
    fig = plt.grid()
    return fig


def main():
    current = Current()
    Simulation_current = []
    time_step = 0
    current_mag = 0
    Current_type = 0
    print(""" ======CURRENT MENU=======
                      1. Constant Current 
                      2. Step Current
                      """)
    choice = int(input("Enter Choice:"))
    if choice == 1:
        current_mag = current.Current_Magnitude()

        Simulation_current = [Constant_currnet(t) for t in T]
        Current_type = 1
    elif choice == 2:
        Simulation_current = [Step_current(t) for t in T]
        time_step = current.Time_step()
        Current_type = 2
        current_mag = current.Current_Magnitude()
    else:
        print("ERROR:INVALID CURRENT")
        sys.exit()
    #print(input_current)
    #print(time_step)
    #pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
    #figs = plt.figure()

    # State (Vm, n, m, h)
    Y = np.array([0.0, n_inf(), m_inf(), h_inf()])

    # Solve ODE system
    # Vy = (Vm[t0:tmax], n[t0:tmax], m[t0:tmax], h[t0:tmax])
    #Vy = odeint(compute_derivatives, Y, T)

    #Idv = [Id(t) for t in T]


    plot_current_density(T,Simulation_current)
    plot_neuron_potential(T,Y,Current_type)
    Plot_Trajectories(Y,T,Current_type)
    plt.show()


main()

