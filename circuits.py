import numpy as np
import sympy as sp


def parallel(*xs):
    '''
    Calculates parallel impedance/resistance.
    
    Parameters:
        xs: seperate or list of components.
        
    Returns
        sympy expression.
            Use 'lamdify' with this result to get a numerical value.
    '''
    import sympy as sp
    import numpy as np

    # Flatten if the user passes a single list or array
    if len(xs) == 1 and isinstance(xs[0], (list, np.ndarray)):
        xs = xs[0]

    r = sum(1/x for x in xs)
    return sp.simplify(1/r)