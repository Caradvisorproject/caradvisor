import unittest

from get_weather import get_weather_data, get_weather_message
from holidays import get_holiday


class GetWeatherTestCase(unittest.TestCase):
    """Tests for get_weather.py"""

    def test_get_weather_data_connection(self):
        result = get_weather_data()
        self.assertEqual(type(result), dict)

    def test_get_weather_message(self):
        result = get_weather_message()
        self.assertEqual(type(result), str)


class GetHolidaysTestCase(unittest.TestCase):
    """Tests for holidays.py"""

    def test_get_holidays(self):
        result_true = get_holiday(day='09-05')
        result_false = get_holiday(day='10-07')
        self.assertTrue(result_true)
        self.assertFalse(result_false)


if __name__ == '__main__':
    unittest.main()
