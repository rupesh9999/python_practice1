def describe_city(city, country='iceland'):
    """Display information about a city."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('reykjavik')
describe_city('paris')
describe_city('tokyo', 'japan')