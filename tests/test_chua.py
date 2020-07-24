"""Testing for Chua system.
"""

import pytest
from src.attractors.chua import Chua


@pytest.fixture
def chaotic_system():
    return Chua


@pytest.fixture(scope="module")
def model():
    chua = Chua(num_points=100)
    return chua.attractor


@pytest.mark.parametrize(
    "inputs, outputs",
    [
        ((0, 0, 0), (0, 0, 0)),
        ((0, 0, 1), (0, 1, 0)),
        ((0, 1, 0), (15.6, -1, -28)),
        ((1, 0, 0), (2.2308, 1, 0)),
        ((1e-3, 1e-4, 1e-5), (3.7908e-03, 9.1e-04, -2.8e-03)),
        ((1.0, 2.0, 3.0), (33.4308, 2.0, -56.0)),
        ((-1000, 2000, -3000), (35654.9076, -6000, -56000)),
        ((1000000, 2000000, 3000000), (26738406.6924, 2000000, -56000000)),
    ],
)
def test_chua_with_default_kwargs(model, inputs, outputs, assert_threshold):
    xi, yi, zi = inputs
    xo, yo, zo = model(xi, yi, zi)

    assert_threshold((xo, yo, zo), outputs)


@pytest.mark.parametrize(
    "inputs, outputs, kwargs",
    [
        ((1, 2, 3), (25.3, 2, -86), {"alpha": 11, "beta": 43, "mu0": -1.3, "mu1": -0.9}),
        ((1, 2, 3), (12.0, 2, -34), {"alpha": 4, "beta": 17, "mu0": -2, "mu1": -3}),
        ((1, 2, 3), (0.0, 2.00001, 0), {"alpha": 0, "beta": 0, "mu0": 0, "mu1": 0}),
        ((-0.01, 0.2, 100), (2.167, 99.79, -8.6), {"alpha": 11, "beta": 43, "mu0": -1.3, "mu1": -0.9}),
    ],
)
def test_chua_with_kwargs(model, inputs, outputs, kwargs, assert_threshold):
    xi, yi, zi = inputs
    xo, yo, zo = model(xi, yi, zi, **kwargs)

    assert_threshold((xo, yo, zo), outputs)


def test_output_length(model):
    outputs = model(0, 0, 0)
    assert len(outputs) == 3, "Should return 3 values as a tuple"
