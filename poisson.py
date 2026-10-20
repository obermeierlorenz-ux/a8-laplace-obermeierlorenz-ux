from relaxation import relax
import numpy as np

#creat inital V


#Length 
L = 1.0
N = 100
h = L/N

#creates a empty Field NxN
nx, ny = N, N
V = np.zeros((nx, ny))


# create mask 
mask = np.zeros((N, N), dtype=bool)

mask[0, :] = True
mask[-1, :] = True
mask[:, 0] = True
mask[:, -1] = True

#coordinats at the cell midpoint
x = np.linspace(h / 2, L - h / 2 , N)
y = np.linspace(h / 2, L - h / 2, N)

#creats a two dimantional coordinate grid
X, Y = np.meshgrid(x, y, indexing="ij")

#Source

sigma = 0.08 * L
S0 = 100.0

source = S0 * np.exp(-((X-L / 2 )**2) + (Y-L / 2)**2) / (2*sigma**2)

#solver
V_final, sweeps, max_change = relax(V, source, mask)

#save cell-center coordination and final potential
data = np.column_stack((
    X.ravel(),
    Y.ravel(),
    V_final.ravel()
))

np.savetxt(
    'data/poisson.csv',
    data,
    delimiter=',',
    header='x,y,V',
    comments=''
)

print('number of sweeps: ', sweeps)
print('final maximum cheanges:', max_change)
print('minimum potential:', np.min(V_final))
print('maximum potential:', np.max(V_final))
print()
