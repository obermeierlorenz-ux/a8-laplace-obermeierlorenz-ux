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

V_final_1, sweeps_1, max_change_1 = relax(V_1, mask_1)

# Compare inner values with the expected constant solution V = 1
error_1 = np.max(np.abs(V_final_1[1:-1, 1:-1] - 1.0))

boundary_change_1 = np.max(np.abs(V_final_1[mask_1] - boundary_before_1))

print('Test 1: Constant solution V = 1')
print('Number of sweeps:', sweeps_1)
print('Final maximum change:', max_change_1)
print('Maximum interior error:', error_1)
print('Maximum boundary change:', boundary_change_1)
print()

#linear solution

V_2 = np.zeros((N, N))

mask_2 = np. zeros((N, N), dtype=bool)

mask_2[0, :] = True
mask_2[-1, :] = True
mask_2[:, 0] = True
mask_2[:, -1] = True

#Set boundary values from the exact linear solution
V_2[mask_2] = X[mask_2] / L

boundary_before_2 = V_2[mask_2].copy()

V_final_2, sweeps_2, max_change_2 = relax(V_2, mask_2)

#exact solution at every cell center 
V_exact = X / L 

#compare the inner calls
error_2 = np.max(
    np.abs(V_final_2[1:-1, 1:-1] - V_exact[1:-1, 1:-1])
)
# Check that fixed values did not change
boundary_change_2 = np.max(
    np.abs(V_final_2[mask_2] - boundary_before_2)
)

print('Test 2: Linear solution V(x, y) = x / L')
print('Number of sweeps:', sweeps_2)
print('Final maximum change:', max_change_2)
print('Maximum interior error:', error_2)
print('Maximum boundary change:', boundary_change_2)