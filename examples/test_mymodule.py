# test_mymodule.py
import mymodule
import pytest


def test_f():
    assert mymodule.f() == "This is f"


@pytest.mark.skip(reason="g is not implemented yet")
def test_g():
    assert mymodule.g() == "This is g"


@pytest.mark.xfail(reason="f is implemented incorrectly")
def test_f_fail():
    assert mymodule.f() == "This is the function f"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 5.0),
        (5, 12, 13.0),
        (8, 15, 17.0),
    ],
)
def test_pyt(a, b, expected):
    assert mymodule.pyt(a, b) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial(n, expected):
    assert mymodule.factorial(n) == expected


def test_negative_factorial():
    with pytest.raises(ValueError):
        mymodule.factorial(-1)


def test_get_yr_weather_temperature_real():
    temperature = mymodule.get_yr_weather_temperature(55.68888, 12.5)
    assert isinstance(temperature, float)
    assert -50.0 < temperature < 60.0  # Reasonable temperature range


def test_get_yr_weather_temperature_mock(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {"properties": {"timeseries": [
                {"data": {"instant": {"details": {"air_temperature": 20.5}}}}
            ]}}
        @staticmethod
        def raise_for_status():
            pass
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(mymodule.requests, "get", mock_get)
    temperature = mymodule.get_yr_weather_temperature(55.68888, 12.5)
    assert temperature == 20.5
