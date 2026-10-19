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

#for a better overview
V_top = 5.0
V_bottom = 5.0
V_left = 5.0
V_right = 5.0

#Edges of my Field/Matrix have fixed values, they dont get changed during calculations
V[0, :] = V_left
V[-1,:] = V_right
V[:, 0] = V_bottom
V[:,-1] = V_top

#corner values: average

V[0, 0] = 0.5 * (V_left + V_bottom)
V[0, -1] = 0.5 * (V_left + V_top)
V[-1, 0] = 0.5 * (V_right + V_bottom)
V[-1, -1] = 0.5 * (V_right + V_top)

#circular shell settings
x0 = L / 2
y0 = L / 2

R = L / 3 
thickness = 0.05 * L
# distance of every cell center from the shell center
r = np.sqrt((X- x0)**2 + (Y - y0)**2)

#Cells inside the physical shell thickness

shell_mask = (( r >= R - thickness / 2) & (r<= R + thickness / 2 ))

#fix the shell cells
mask[shell_mask] = True

#upper and lower shell potential

upper_shell = shell_mask & (Y >= y0)
lower_shell = shell_mask & (Y < y0)

V[upper_shell] = 10.0
V[lower_shell] = -10.0

#solver
V_final, sweeps, max_change = relax(V, mask)

#save cell-center coordination and final potential
data = np.column_stack((
    X.ravel(),
    Y.ravel(),
    V_final.ravel()
))

np.savetxt(
    'data/split_shell.csv',
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
