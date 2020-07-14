"""Useful methods and attributes for testing.

"""


def calc_absolute_error(test: tuple = None, pred: tuple = None) -> float:
    """Calculate absolute error for test checking.

    Parameters
    ----------
    test : tuple
        coordinates array of theoretical values.
    pred : tuple
        coordinates array of calculated values.

    Returns
    -------
    err: float
        Absolute error: sum[(Xi - Yi) / Xi] / 3.

    """
    err_sum = 0
    for e1, e2 in zip(test, pred):
        div = e2 if e1 == 0 else e1
        try:
            err_sum += (e1 - e2)**2 / div**2
        except ZeroDivisionError:
            pass
    return err_sum / 3
