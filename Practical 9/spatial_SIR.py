"""
Practical 9: spatial stochastic SIR model.

This version places the population on a 100 x 100 grid:
    0 = susceptible
    1 = infected
    2 = recovered / resistant

Unlike the well-mixed SIR model, infection can only pass from an infected cell to
one of its eight neighbouring cells.  This lets the outbreak spread through space
rather than instantly mixing across the whole population.
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ.setdefault("MPLCONFIGDIR", os.path.join(SCRIPT_DIR, ".mplconfig"))

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# -----------------------------
# Define the model parameters.
# -----------------------------

grid_size = 100
beta = 0.3
gamma = 0.05
time_points = 100
snapshot_times = [0, 10, 50, 100]

SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2


# ---------------------------------------
# Create the all-susceptible population.
# ---------------------------------------

population = np.zeros((grid_size, grid_size), dtype=int)

# Randomly choose the x and y coordinates of the first infected individual.
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = INFECTED


def plot_population(state, time_point, filename=None):
    """Plot one heatmap of the spatial model."""

    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(state, cmap="viridis", interpolation="nearest", vmin=0, vmax=2)
    plt.title(f"Spatial SIR model at time {time_point}")
    plt.xlabel("Column")
    plt.ylabel("Row")
    colour_bar = plt.colorbar(ticks=[SUSCEPTIBLE, INFECTED, RECOVERED])
    colour_bar.ax.set_yticklabels(["Susceptible", "Infected", "Recovered"])
    plt.tight_layout()

    if filename is not None:
        output_path = os.path.join(SCRIPT_DIR, filename)
        plt.savefig(output_path, format="png")


def plot_snapshots(snapshots):
    """Plot the requested time points on one figure."""

    fig, axes = plt.subplots(2, 2, figsize=(7, 6), dpi=150)
    axes = axes.ravel()

    for ax, time_point in zip(axes, snapshot_times):
        image = ax.imshow(
            snapshots[time_point],
            cmap="viridis",
            interpolation="nearest",
            vmin=0,
            vmax=2,
        )
        ax.set_title(f"Time {time_point}")
        ax.set_xlabel("Column")
        ax.set_ylabel("Row")

    colour_bar = fig.colorbar(
        image,
        ax=axes.tolist(),
        ticks=[SUSCEPTIBLE, INFECTED, RECOVERED],
        shrink=0.85,
    )
    colour_bar.ax.set_yticklabels(["Susceptible", "Infected", "Recovered"])
    fig.suptitle("Spatial SIR spread through time")
    output_path = os.path.join(SCRIPT_DIR, "spatial_SIR_snapshots.png")
    plt.savefig(output_path, format="png", bbox_inches="tight")


def valid_neighbour_coordinates(row, column):
    """
    Return all valid neighbour coordinates around one grid cell.

    A cell can have up to eight neighbours: north, south, east, west, and the
    four diagonals.  Edge and corner cells have fewer neighbours, so this helper
    checks that every candidate coordinate remains inside the 100 x 100 grid.
    """

    neighbours = []

    for row_offset in [-1, 0, 1]:
        for column_offset in [-1, 0, 1]:
            if row_offset == 0 and column_offset == 0:
                continue

            neighbour_row = row + row_offset
            neighbour_column = column + column_offset

            row_is_inside_grid = 0 <= neighbour_row < grid_size
            column_is_inside_grid = 0 <= neighbour_column < grid_size

            if row_is_inside_grid and column_is_inside_grid:
                neighbours.append((neighbour_row, neighbour_column))

    return neighbours


# --------------------
# Pseudocode for loop.
# --------------------
#
# For each time point:
#   1. Copy the current population into next_population.
#      This means infection and recovery decisions are based on the same old
#      time point instead of being affected by earlier updates in the loop.
#   2. Use np.where(population == INFECTED) to find all infected cells.
#   3. For each infected cell:
#        a. Visit each of its valid neighbouring cells.
#        b. If the neighbour is susceptible, randomly decide whether infection
#           spreads to that neighbour with probability beta.
#        c. If infection happens, mark that neighbour infected in next_population.
#        d. Randomly decide whether the original infected cell recovers with
#           probability gamma.
#        e. If recovery happens, mark that original cell recovered.
#   4. Replace population with next_population.
#   5. Save a snapshot for time points 10, 50, and 100 so the spread can be seen.

snapshots = {0: population.copy()}

# Save the first random infected point as its own plot, as requested.
plot_population(population, 0, filename="spatial_SIR_initial.png")
plt.close()

for time_point in range(1, time_points + 1):
    next_population = population.copy()

    infected_rows, infected_columns = np.where(population == INFECTED)

    for row, column in zip(infected_rows, infected_columns):
        for neighbour_row, neighbour_column in valid_neighbour_coordinates(row, column):
            neighbour_is_susceptible = (
                population[neighbour_row, neighbour_column] == SUSCEPTIBLE
            )

            if neighbour_is_susceptible:
                infection_event = np.random.choice(range(2), p=[1 - beta, beta])

                if infection_event == 1:
                    next_population[neighbour_row, neighbour_column] = INFECTED

        recovery_event = np.random.choice(range(2), p=[1 - gamma, gamma])

        if recovery_event == 1:
            next_population[row, column] = RECOVERED

    population = next_population

    if time_point in snapshot_times:
        snapshots[time_point] = population.copy()


plot_snapshots(snapshots)
