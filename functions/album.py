def make_album(artist, title, songs=None):
    """Create a dictionary describing a music album."""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

# Interactive loop to build albums
while True:
    print("\nEnter album details (or 'q' to quit):")
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    title = input("Album title: ")
    if title.lower() == 'q':
        break
    songs = input("Number of songs (optional, press Enter to skip): ")
    if songs.lower() == 'q':
        break
    
    # Convert songs to integer if provided, otherwise leave as None
    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)
    
    print("Album created:", album)

print("Goodbye!")