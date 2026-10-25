import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    size = x.size
    v = 0.0

    for n in x:
        v += (n - mean) ** 2
    var = float(v / (size - 1))
    std = float(var ** 0.5)

    return {
        "variance": var,
        "standard_deviation": std
    }
        