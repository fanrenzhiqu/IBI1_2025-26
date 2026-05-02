"""
Practical 9: stochastic SIR model with vaccination.

This script extends the simple SIR model by adding a vaccinated group.  Vaccinated
people are counted separately from recovered people, but they behave similarly in
one important way: they cannot become infected.  The total population remains
10000 in every simulation.
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ.setdefault("MPLCONFIGDIR", os.path.join(SCRIPT_DIR, ".mplconfig"))

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm


# -----------------------------
# Define the model parameters.
# -----------------------------

N = 10000
initial_infected = 1
beta = 0.3
gamma = 0.05
time_points = 1000

# The practical asks for infected curves for 0, 10, 20, ..., 100 percent
# vaccination.
vaccination_percentages = range(0, 101, 10)


def run_vaccination_simulation(vaccination_percentage):
    """
    Run one stochastic SIRV simulation and return the infected history.

    Pseudocode:
      1. Convert the vaccination percentage into a number of vaccinated people.
      2. Keep one infected person at the start of the outbreak.
      3. Put the remaining non-vaccinated people into the susceptible group.
      4. Repeat for 1000 time points:
           a. Calculate infection probability from beta and I / N.
           b. Randomly choose which susceptible people become infected.
           c. Randomly choose which infected people recover.
           d. Update S, I, R, and keep V constant.
           e. Record I so it can be plotted.
    """

    # If 100% vaccination is requested, keep the single initial infected case and
    # vaccinate everyone else.  This preserves the required population size while
    # still allowing the outbreak to start from one infected individual.
    vaccinated = min(round(N * vaccination_percentage / 100), N - initial_infected)
    susceptible = N - vaccinated - initial_infected
    infected = initial_infected
    recovered = 0

    infected_history = [infected]

    for _ in range(time_points):
        infection_probability = beta * (infected / N)
        infection_probability = min(max(infection_probability, 0), 1)
        recovery_probability = min(max(gamma, 0), 1)

        infection_events = np.random.choice(
            range(2),
            susceptible,
            p=[1 - infection_probability, infection_probability],
        )
        new_infections = int(np.sum(infection_events))

        recovery_events = np.random.choice(
            range(2),
            infected,
            p=[1 - recovery_probability, recovery_probability],
        )
        new_recoveries = int(np.sum(recovery_events))

        susceptible = susceptible - new_infections
        infected = infected + new_infections - new_recoveries
        recovered = recovered + new_recoveries

        # This check documents the model invariant and catches accidental edits.
        assert susceptible + infected + recovered + vaccinated == N

        infected_history.append(infected)

    return infected_history


# ----------------
# Plot the result.
# ----------------

times = range(time_points + 1)

plt.figure(figsize=(7, 4.5), dpi=150)

for percentage in vaccination_percentages:
    infected_history = run_vaccination_simulation(percentage)
    colour = cm.viridis(percentage / 100)
    plt.plot(
        times,
        infected_history,
        label=f"{percentage}% vaccinated",
        color=colour,
    )

plt.xlabel("Time point")
plt.ylabel("Number of infected people")
plt.title("Effect of vaccination on a stochastic SIR outbreak")
plt.legend(title="Vaccination", fontsize=7)
plt.tight_layout()
output_path = os.path.join(SCRIPT_DIR, "SIR_vaccination_plot.png")
plt.savefig(output_path, format="png")
