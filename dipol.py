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



#Electrods

a = 0.05 * L

x_plus = L / 3
y_plus = L / 2
x_minus = 2 * L / 3
y_minus = L / 2

r_plus = np.sqrt((X - x_plus)**2 + (Y - y_plus)**2)
r_minus = np.sqrt((X - x_minus)**2 + (Y - y_minus)**2)

#filled circular electrodes
plus_electrode = r_plus <= a
minus_electrode = r_minus <= a

#fix the electrodes
mask[plus_electrode] = True
mask[minus_electrode] = True

# Fixed electrode potentials
V[plus_electrode] = 1.0
V[minus_electrode] = -1.0

#solver
V_final, sweeps, max_change = relax(V, mask)

#save cell-center coordination and final potential
data = np.column_stack((
    X.ravel(),
    Y.ravel(),
    V_final.ravel()
))

np.savetxt(
    'data/dipole.csv',
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
