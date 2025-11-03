import numpy as np
import sympy as sp


def eng_notation(value, sig_figs=3):
    """
    Converts a number to engineering notation with SI prefix.

    Parameters:
        value (float): The numeric value to format.
        sig_figs (int): Number of significant figures to display.

    Returns:
        str: String formatted in engineering notation (e.g., '4.7 k', '2.00 m', '1.23 µ', etc.)
    """

    # Handle zero directly
    if value == 0:
        return f"0"

    # Define SI prefixes
    prefixes = {
        -24: "y",  # yocto
        -21: "z",  # zepto
        -18: "a",  # atto
        -15: "f",  # femto
        -12: "p",  # pico
        -9:  "n",  # nano
        -6:  "µ",  # micro
        -3:  "m",  # milli
        0:   "",   # base
        3:   "k",  # kilo
        6:   "M",  # mega
        9:   "G",  # giga
        12:  "T",  # tera
        15:  "P",  # peta
        18:  "E",  # exa
        21:  "Z",  # zetta
        24:  "Y",  # yotta
    }

    import math

    exponent = int(math.floor(math.log10(abs(value)) / 3) * 3)
    exponent = max(min(exponent, 24), -24)  # clamp to available prefixes
    scaled = value / (10 ** exponent)
    prefix = prefixes.get(exponent, f"e{exponent}")

    return f"{scaled:.{sig_figs}g}{prefix}"

def voltage_div(Vin, Z1, Z2):
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