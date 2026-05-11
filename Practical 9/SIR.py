# Pseudocode for the SIR model:
#
# 1. Initialize the population:
#    - Set total population N = 10000
#    - Start with 1 infected person (I = 1), 0 recovered (R = 0), and the rest susceptible (S = N - 1)
#    - Set infection rate beta = 0.3 and recovery rate gamma = 0.05
#
# 2. For each of 1000 time points:
#    a. Calculate the infection probability for a susceptible person: infection_probability = beta * (I / N)
#    b. For each susceptible person, randomly decide if they become infected based on infection_probability
#    c. For each infected person, randomly decide if they recover based on gamma
#    d. Update the counts: S -= new_infections, I += new_infections - new_recoveries, R += new_recoveries
#    e. Record the current S, I, R values for plotting
#
# 3. Plot the time series of S, I, R over the 1000 time points


# Import necessary libraries.
import os

# Absolute path of this script's folder.  All output files are saved here, even
# if the script is run from the repo root, the Practical 9 folder, or an IDE.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Matplotlib sometimes tries to write a font cache in the home directory.  
# This practical folder is writable, so we tell Matplotlib to keep its cache here.
os.environ.setdefault("MPLCONFIGDIR", os.path.join(SCRIPT_DIR, ".mplconfig"))

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# -----------------------------
# Define the model parameters.
# -----------------------------

# Total population size required by the practical.
N = 10000

# At time 0, one person is infected and nobody has recovered yet.
initial_infected = 1
initial_recovered = 0
initial_susceptible = N - initial_infected - initial_recovered

# Infection probability upon contact (beta) and recovery probability (gamma).
beta = 0.3
gamma = 0.05

# Number of time points required by the practical.
time_points = 1000


# ----------------------------------------
# Create variables that change over time.
# ----------------------------------------

S = initial_susceptible
I = initial_infected
R = initial_recovered

# Arrays used to record the history of the model.  We record time 0 before the
# loop, then append one new value after each time point.
S_history = [S]
I_history = [I]
R_history = [R]


# --------------------
# Pseudocode for loop.
# --------------------
#
# For each time point:
#   1. Calculate the proportion of the population that is currently infected.
#   2. Convert that into the infection probability for one susceptible person:
#          infection_probability = beta * (I / N)
#      This combines the chance of infection on contact with the chance that the
#      contact is with an infected person.
#   3. For every susceptible person, randomly choose 0 or 1:
#          0 means "does not become infected"
#          1 means "becomes infected"
#   4. For every infected person, randomly choose 0 or 1:
#          0 means "does not recover"
#          1 means "recovers"
#   5. Count the new infections and new recoveries.
#   6. Update S, I, and R simultaneously using those counts.
#   7. Store the new S, I, and R values for plotting.

for _ in range(time_points):
    # A susceptible person can only be infected if they meet an infected person.
    proportion_infected = I / N
    infection_probability = beta * proportion_infected

    # Keep probabilities safely inside [0, 1].  This is not usually needed with
    # the values in the practical, but it makes the simulation robust.
    infection_probability = min(max(infection_probability, 0), 1)
    recovery_probability = min(max(gamma, 0), 1)

    # Pick which susceptible individuals become infected at this time point.
    # np.random.choice(range(2), S, p=[...]) returns S zeroes/ones.
    infection_events = np.random.choice(
        range(2),
        S,
        p=[1 - infection_probability, infection_probability],
    )
    new_infections = int(np.sum(infection_events))

    # Pick which infected individuals recover at this time point.
    recovery_events = np.random.choice(
        range(2),
        I,
        p=[1 - recovery_probability, recovery_probability],
    )
    new_recoveries = int(np.sum(recovery_events))

    # Update all three groups.  The total population remains constant:
    # S + I + R should always equal N.
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    # Record the output of this time step.
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)


# ----------------
# Plot the result.
# ----------------

times = range(time_points + 1)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(times, S_history, label="Susceptible", color="tab:blue")
plt.plot(times, I_history, label="Infected", color="tab:red")
plt.plot(times, R_history, label="Recovered", color="tab:green")
plt.xlabel("Time point")
plt.ylabel("Number of people")
plt.title("Stochastic SIR model")
plt.legend()
plt.tight_layout()

# Save the plot in the same folder as this script.
output_path = os.path.join(SCRIPT_DIR, "SIR_plot.png")
plt.savefig(output_path, format="png")

print("SIR simulation completed.")
print(f"Plot saved as {output_path}")
