import unittest
from city_functions import city_country

def city_country(city, country, population=None):
    """Return a string representing the city and country, with optional population."""
    formatted_city = city.title()
    formatted_country = country.title()
    if population is not None:
        formatted_population = f"{population:,}"
        return f"{formatted_city}, {formatted_country} - population {formatted_population}"
    else:
        return f"{formatted_city}, {formatted_country}"

class TestCityCountry(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country_without_population(self):
        """Test the function without providing population."""
        self.assertEqual(city_country('santiago', 'chile'), 'Santiago, Chile')
        self.assertEqual(city_country('new york', 'united states'), 'New York, United States')
        self.assertEqual(city_country('Paris', 'France'), 'Paris, France')

    def test_city_country_with_population(self):
        """Test the function with population provided."""
        self.assertEqual(city_country('santiago', 'chile', 5000000), 'Santiago, Chile - population 5,000,000')
        self.assertEqual(city_country('new york', 'united states', 8000000), 'New York, United States - population 8,000,000')
        self.assertEqual(city_country('Paris', 'France', 2000000), 'Paris, France - population 2,000,000')
        self.assertEqual(city_country('Nowhere', 'Noland', 0), 'Nowhere, Noland - population 0')

if __name__ == '__main__':
    unittest.main()
