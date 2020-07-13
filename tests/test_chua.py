import pytest
from src.chua import chua


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


test_coordinates_with_defaults = [
    ((0, 0, 0), (0, 0, 0)),
    ((0, 0, 1), (0, 1, 0)),
    ((0, 1, 0), (15.6, -1, -28)),
    ((1, 0, 0), (2.2308, 1, 0)),
    ((1e-3, 1e-4, 1e-5), (3.7908e-03, 9.1e-04, -2.8e-03)),
    ((1., 2., 3.), (33.4308, 2.0, -56.0)),
    ((-1000, 2000, -3000), (35654.9076, -6000, -56000)),
    ((1000000, 2000000, 3000000), (26738406.6924, 2000000, -56000000)),
]


@pytest.mark.parametrize("inputs, outputs", test_coordinates_with_defaults)
def test_chua_with_default_kwargs(inputs, outputs):
    xi, yi, zi = inputs
    xo, yo, zo = chua(xi, yi, zi)

    err_sum = calc_absolute_error(test=(xo, yo, zo), pred=outputs)
    assert err_sum < 1e-10, f"Outputs: {xo, yo, zo}, Error: {err_sum :.3f}"


test_coordinates_with_kwargs = [
    ((1, 2, 3), (25.3, 2, -86), {"alpha": 11, "beta": 43, "mu0": -1.3, "mu1": -0.9, "alternate": None}),
    ((1, 2, 3), (12.0, 2, -34), {"alpha": 4, "beta": 17, "mu0": -2, "mu1": -3, "alternate": None}),
    ((1, 2, 3), (0.0, 2.00001, 0), {"alpha": 0, "beta": 0, "mu0": 0, "mu1": 0, "alternate": None}),
    ((1, 2, 3), (0.6, 4, 2), {"alpha": 11, "beta": 43, "mu0": -1.3, "mu1": -0.9, "alternate": True}),
    # ((1, 2, 3), (0.6, 4, 2), {"alpha": 4, "beta": 17, "mu0": -2, "mu1": -3, "alternate": True}),
    # ((1, 2, 3), (0.6, 4, 2), {"alpha": 15, "beta": 24, "mu0": 0, "mu1": 0, "alternate": True}),
]


@pytest.mark.parametrize("inputs, outputs, kwargs", test_coordinates_with_kwargs)
def test_chua_with_kwargs(inputs, outputs, kwargs):
    xi, yi, zi = inputs
    xo, yo, zo = chua(xi, yi, zi, **kwargs)

    err_sum = calc_absolute_error(test=(xo, yo, zo), pred=outputs)
    assert err_sum < 1e-8, f"Outputs: {xo, yo, zo}, Error: {err_sum :.3f}"
