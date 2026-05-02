"""
Practical 9: simple stochastic SIR model.

This script models one outbreak in a well-mixed population.  The population is
split into three groups:
    S = susceptible people who can become infected
    I = infected people who can infect others and can recover
    R = recovered people who are assumed to be immune

The model is stochastic because every susceptible/infected person is tested with
random probabilities at every time point.  Running the file several times should
therefore give similar overall behaviour, but not exactly the same curve.
"""

# Import necessary libraries.
import os

# Absolute path of this script's folder.  All output files are saved here, even
# if the script is run from the repo root or another terminal directory.
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
output_path = os.path.join(SCRIPT_DIR, "SIR_plot.png")
plt.savefig(output_path, format="png")
