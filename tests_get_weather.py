import unittest

from get_weather import get_weather_data, get_weather_message


class GetWeatherTestCase(unittest.TestCase):
    """Tests for get_weather.py"""

    def test_get_weather_data_connection(self):
        result = get_weather_data()
        self.assertEqual(type(result), dict)

    def test_get_weather_message(self):
        result = get_weather_message()
        self.assertEqual(type(result), str)


unittest.main()
