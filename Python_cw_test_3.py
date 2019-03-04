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
    def Constant_current(t):
        print("Enter the magnitude of current ")
        input_current = float(input())
        if not isinstance(input_current, float):
            raise TypeError("NOT A NUMBER")
        else:
            current = np.zeros(len(T))
            current_length = len(current)
            for t in range(1,current_length):
                temp = int(t)
                current[temp] = input_current
                return current

    def time_step(self):
        print("Enter the time step")
        self.time_step = input()
        return self.time_step

    def Step_current(t):
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
                return updated_current


# Potassium ion-channel rate functions

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

    dy[0] = (Id(t0) / Cm) - (GK * (Vm - VK)) - (GNa * (Vm - VNa)) - (GL * (Vm - Vl))

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

def plot_neuron_potential(Time,Voltage):
    Vy = odeint(compute_derivatives, Voltage, Time)

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(T, Vy[:, 0])
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Vm (mV)')
    ax.set_title('Neuron potential with two spikes')
    fig = plt.grid()
    return fig

def Plot_Trajectories(Y,Time):

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
    input_current = 0
    time_step = 0

    print(""" ======CURRENT MENU=======
                      1. Constant Current
                      2. Step Current
                      """)
    choice = int(input("Enter Choice:"))
    if choice == 1:
        Id = current.Constant_current()
    elif choice == 2:
        Id = current.Step_current()
        time_step = current.time_step()
    else:
        print("ERROR:INVALID CURRENT")
        sys.exit()
    print(input_current)
    print(time_step)
    #pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
    #figs = plt.figure()

    # State (Vm, n, m, h)
    Y = np.array([0.0, n_inf(), m_inf(), h_inf()])

    # Solve ODE system
    # Vy = (Vm[t0:tmax], n[t0:tmax], m[t0:tmax], h[t0:tmax])
    #Vy = odeint(compute_derivatives, Y, T)

    Idv = [Id(t) for t in T]

    plot_current_density(T, Idv)
    plot_neuron_potential(T,Y)
    Plot_Trajectories(Y,T)
    plt.show()


main()