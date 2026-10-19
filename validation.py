import numpy as np
from relaxation import relax


#Length 
L = 1.0
N = 100
h = L/N


#coordinats at the cell midpoint
x = np.linspace(h / 2, L - h / 2 , N)
y = np.linspace(h / 2, L - h / 2, N)

#creats a two dimantional coordinate grid
X, Y = np.meshgrid(x, y, indexing="ij")

V_1 = np.zeros((N, N))

mask_1 = np.zeros((N, N), dtype=bool) 

mask_1[0, :] = True
mask_1[-1, :] = True
mask_1[:, 0] = True
mask_1[:, -1] = True

#set ervery fixe boundary cell to 1
V_1[mask_1] = 1.0

#store the boundry values befor relaxation
boundary_before_1 = V_1[mask_1].copy()

V_final_1, sweep_1, max_change_1 = relax(V_1, mask_1)

# Compare inner values with the expected constant solution V = 1
error_1 = np.max(np.abs(V_final_1[1:-1, 1:-1] - 1.0))

boundary_change_1 = np.max(np.abs(V_final_1[mask_1] - boundary_before_1))

