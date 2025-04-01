def make_album(artist_name, album_title, number_of_songs_on_album=None):
    """Return a dictionary of information about an album."""
    album = {
        'artist': artist_name,
        'album': album_title,
    }
    if number_of_songs_on_album:
        album['number_of_songs'] = number_of_songs_on_album
    return album

# Example usage:
album_1 = make_album('Taylor Swift', '1989')
album_2 = make_album('Ed Sheeran', 'Divide', 12)
album_3 = make_album('Adele', '25', 11)
print(album_1)
print(album_2)
print(album_3)