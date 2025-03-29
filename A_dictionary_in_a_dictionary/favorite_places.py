favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['canada', 'alaska', 'greenland'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
