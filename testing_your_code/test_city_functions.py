import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests fir tge city_countrt function"""

    def test_city_country(self):
        """Test that the function works with santioago and chile"""
        self.assertEqual(city_country('santiago', 'chile'), 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()