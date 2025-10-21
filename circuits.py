import numpy as np
import sympy as sp

def voltageDivder(Vin, Z1, Z2):
    '''
    Calculates voltage divider
    
    Parameters:
        Vin: input voltage
        Z1: impedance of first component.
        Z2: impedance of second component.
        (Note: Vo is between Z1 and Z2, https://en.wikipedia.org/wiki/Voltage_divider).
        
    Returns:
        sympy expression.
            Use 'lamdify' with this result to get a numerical value.
    '''
    return sp.simplify(Vin*(Z1/Z2))

def parallel(*xs):
    '''
    Calculates parallel impedance/resistance.
    
    Parameters:
        xs: seperate or list of components.
        
    Returns
    '''
    import sympy as sp
    import numpy as np

    # Flatten if the user passes a single list or array
    if len(xs) == 1 and isinstance(xs[0], (list, np.ndarray)):
        xs = xs[0]

    r = sum(1/x for x in xs)
    return sp.simplify(1/r)