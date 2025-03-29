cities = {
    'tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'area': 2191,
    },
    'delhi': {
        'country': 'India',
        'population': 1380004385,
        'area': 3287,
    },
    'shanghai': {
        'country': 'China',
        'population': 24183300,
        'area': 6340,
    },
}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    area = info['area']
    population_density = population / area
    print(f"\nCity: {city.title()}")
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Area: {area} km²")
    print(f"Population Density: {population_density:.2f} people/km²")
    print(f"Population Density: {population / area:.2f} people/km²")
    print(f"Population Density: {population_density:.2f} people/km²")
    print(f"Population Density: {population_density:.2f} people/km²")
    print(f"Population Density: {population_density:.2f} people/km²")
    print(f"Population Density: {population_density:.2f} people/km²")
    print(f"Population Density: {population_density:.2f} people/km²")