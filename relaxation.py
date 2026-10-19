import numpy as np





def relax(V, mask, tol: float = 1e-4, max_iter: int = 100000):

    #copy of the inital patential
    V = V.copy()

    for sweep in range(1, max_iter + 1):
        V_new = V.copy()

        # Go through every inner cell one by one
        for i in range(1, V.shape[0] - 1):
            for j in range(1, V.shape[1] - 1):

                # Only update non-fixed cells
                if not mask[i, j]:

                    V_new[i, j] = 0.25 * (
                            V[i + 1, j] +
                            V[i - 1, j] +
                            V[i, j + 1] +
                            V[i, j - 1]
                    )
        #jede Zellen bei der die maske True ist werden wieder auf ihren alten Wert gesetz
        V_new[mask] = V[mask]


        #prüft wie stark sich ein feld in einem sweep verändert
        #ist die großte änderung klein trifft if unten zu
        max_change = np.max(np.abs(V_new[~mask] - V[~mask]))
                #~mask bedeutet alle nicht festen Zeillen also die freien Zellen

        #neues Feld wird zum alten Feld für den nächsten Sweep
        V = V_new

        if max_change < tol : 
            return V, sweep, max_change

    raise RuntimeError('Jacobi relaxation did not converge.d')





