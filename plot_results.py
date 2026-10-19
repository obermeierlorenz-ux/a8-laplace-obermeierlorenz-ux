import numpy as np
import matplotlib.pyplot as plt 
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
    'data/four_edge.csv',
    'Four Different Edge Values',
    'Four edge',
    vmin=-0.5,
    vmax=1.0
)


plot_potential(
    'data/split_shell.csv',
    'Split shell',
    'Four edge',
    vmin=-0.5,
    vmax=1.0
)