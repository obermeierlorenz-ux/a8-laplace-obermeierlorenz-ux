import relaxation
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

#Edges of my Field/Matrix have fixed values, they dont get changed during calculations
V[0, :] = 1.0
V[-1,:] = 0.0
V[:, 0] = 0.0
V[:,-1] = 0.0


