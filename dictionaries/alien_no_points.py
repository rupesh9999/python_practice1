#alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])
# The code above will raise a KeyError because 'points' is not a key in alien_0.


alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)