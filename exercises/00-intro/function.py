import numpy as np

peak_vals = [3.5, 7.0492199266, 6.5054867]
widths = [1, 1e-7, 1e-7]
magnitudes = [0.2, 10, 10]

def f(x):
    """
    A continuous function defined over (1, 10)

    Parameters
    ----------
    x : float
      Input value. Expected to be > 1.

    Returns
    -------

    float
    """
    if x < 1 or x > 10:
        return 0
    val = 1/x

    for i in range(len(peak_vals)):
        peak_loc = peak_vals[i]
        width = widths[i]
        magnitude = magnitudes[i]

        peak_min = peak_loc - 0.5 * width
        peak_max = peak_loc + 0.5 * width
        if peak_min < x and x < peak_max:
            val += magnitude * np.exp(-(x-peak_loc)**2 / (width/6)**2)

    return val