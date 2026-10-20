import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
from pathlib import Path

def plot_potential(data_file, plot_name, case_name ,vmin, vmax):

    #Load saved x, y and potential values
    data = np.loadtxt(data_file, 
                      delimiter=',', 
                      skiprows=1)

    N = int(np.sqrt(len(data)))

    #convert teh one-dimensional colums back into N x N arrays

    X = data[:, 0].reshape(N, N)
    Y = data[:, 1].reshape(N, N)
    V = data[:, 2].reshape(N, N)

    # Create plots folder if it does not exist
    Path('plots').mkdir(exist_ok=True)

    #heatmap
    fig1, ax1 = plt.subplots()

    heatmap = ax1.pcolormesh(X, Y, V, shading = 'nearest',
                             cmap = 'viridis',
                             vmin=vmin,
                             vmax=vmax)

    fig1.colorbar(heatmap, ax=ax1, label= ' Potential V')

    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title(f'Potential Heatmap: {case_name}')
    ax1.set_aspect('equal')
    ax1.grid()

    fig1.savefig(f'plots/{plot_name}_heatmap.png', 
                dpi=300, #
                bbox_inches = 'tight')

    plt.show()

    #contour plot

    fig2, ax2 = plt.subplots()

    levels = np.linspace(vmin, vmax, 16)

    contours = ax2.contour(
        X,
        Y,
        V,
        levels=levels,
        cmap='viridis'
    )

    ax2.clabel(contours, inline=True, fontsize=8)

    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title(f'Potential Contours: {case_name}')
    ax2.set_aspect('equal')
    ax2.grid()

    fig2.savefig(
        f'plots/{plot_name}_contours.png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.show()


plot_potential(
    'data/one_edge.csv',
    'one_edge',
    'One Nonzero Edge',
    vmin=-0.5,
    vmax=1.0
)

plot_potential(
    'data/four_edges.csv',
    'four_edges',
    'Four Different Edge Values',
    vmin=-0.5,
    vmax=1.0
)


plot_potential(
    'data/split_shell.csv',
    'split_shell',
    'Split Circular Shell',
    vmin=-10.0,
    vmax=10.0
)


def plot_dipole():

    # Load saved dipole data
    data = np.loadtxt(
        'data/dipole.csv',
        delimiter=',',
        skiprows=1
    )

    N = int(np.sqrt(len(data)))

    X = data[:, 0].reshape(N, N)
    Y = data[:, 1].reshape(N, N)
    V = data[:, 2].reshape(N, N)

    # Electrode locations
    x_plus = 1.0 / 3.0
    y_plus = 1.0 / 2.0

    x_minus = 2.0 / 3.0
    y_minus = 1.0 / 2.0

    a = 0.05

    fig1, ax1 = plt.subplots()

    heatmap = ax1.pcolormesh(
        X,
        Y,
        V,
        shading='nearest',
        cmap='coolwarm',
        vmin=-1.0,
        vmax=1.0
    )

    fig1.colorbar(heatmap, ax=ax1, label='Potential V')

    # Mark zero-potential contour
    zero_contour = ax1.contour(
        X,
        Y,
        V,
        levels=[0.0],
        colors='black',
        linewidths=1.5
    )

    ax1.clabel(zero_contour, fmt='V = %.1f', fontsize=8)

    # Mark electrodes
    plus_circle = Circle(
        (x_plus, y_plus),
        a,
        fill=False,
        color='black',
        linewidth=1.5
    )

    minus_circle = Circle(
        (x_minus, y_minus),
        a,
        fill=False,
        color='black',
        linewidth=1.5
    )

    ax1.add_patch(plus_circle)
    ax1.add_patch(minus_circle)

    ax1.text(x_plus, y_plus, '+',
             ha='center', va='center',
             fontsize=12, fontweight='bold')

    ax1.text(x_minus, y_minus, '-',
             ha='center', va='center',
             fontsize=12, fontweight='bold')

    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Potential Heatmap: Electrode Dipole')
    ax1.set_aspect('equal')
    ax1.grid()

    fig1.savefig(
        'plots/dipole_heatmap.png',
        dpi=300,
        bbox_inches='tight'
    )

    fig2, ax2 = plt.subplots()

    levels = np.linspace(-1.0, 1.0, 21)

    contours = ax2.contour(
        X,
        Y,
        V,
        levels=levels,
        cmap='coolwarm'
    )

    ax2.clabel(contours, inline=True, fontsize=8)

    # Mark V = 0 more strongly
    zero_contour = ax2.contour(
        X,
        Y,
        V,
        levels=[0.0],
        colors='black',
        linewidths=2.0
    )

    ax2.clabel(zero_contour, fmt='V = %.1f', fontsize=8)

    # Mark electrodes
    plus_circle = Circle(
        (x_plus, y_plus),
        a,
        fill=False,
        color='black',
        linewidth=1.5
    )

    minus_circle = Circle(
        (x_minus, y_minus),
        a,
        fill=False,
        color='black',
        linewidth=1.5
    )

    ax2.add_patch(plus_circle)
    ax2.add_patch(minus_circle)

    ax2.text(x_plus, y_plus, '+',
             ha='center', va='center',
             fontsize=12, fontweight='bold')

    ax2.text(x_minus, y_minus, '-',
             ha='center', va='center',
             fontsize=12, fontweight='bold')

    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Potential Contours: Electrode Dipole')
    ax2.set_aspect('equal')
    ax2.grid()

    fig2.savefig(
        'plots/dipole_contours.png',
        dpi=300,
        bbox_inches='tight'
    )

    plt.show()

plot_dipole()
