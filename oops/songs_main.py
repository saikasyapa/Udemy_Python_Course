# ####### DocStrings



class Song:
    """ Class to represent song

    Attributes:
        title (str) : The title of the song
        artist (str) : An artist object representing the song creator.
        duration (int) : the duration of the song in seconds. maybe zero
    """
    def __init__(self,title,artist,duration=0):
        """
        Song init method

        :param title: Initialised the 'title' attribute
        :param artist: An artist object representation of song creator
        :param duration:the duration of the song in seconds.
              will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration
class Album:
    """ Class to represent an album, using it's track list

    Attributes:
        name (str) : The name of the album.
        year (int) : the year of the album.
        artist (Artist) : The artist responsible for album
        tracks(List(songs)): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the albums track list

    """


    def __init__(self,name, year,artist = None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position = None):
        """ Add a song to the track list
        Args:
            song (song): A song to add
            position (opitional[int] : If specified, the song will be added to the position
            in the tracklist - insert it between songs if necessary.
            otherwise, the sone is added to last.
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position,song)

class Artist:
    """ basic class to store artist details

    Attributes:
        name (str) : The name of the artist.
        albums (list(albums)) : A list of the albums by this artist.
            The list includes on those albums in this collection, it is
            not an exhaustive list of the artist's published albums.
    Methods:
        add_album:Use to add a new album to the artist's album list

    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self,album):
        """ Add a new album to the list

        Args:
            album(Albums): Album object to add to the list.
            if the album is already present, it will not added again
        """
        self.albums.append(album)

# def load_data():
#     new_artist = None
#     new_album = None
#     artist_list = []
#
#     with open('albums.txt','r',encoding='utf-8') as albums:
#         for line in albums:
#             artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
#             year_field = int(year_field)
#             print(artist_field,album_field,year_field,song_field)
#             if new_artist is None:
#                 new_artist = Artist(artist_field)
#             elif new_artist.name != artist_field:
#                 ### we just read details for a new artist
#                 ### store the current album in the currents artists collection then create a new artist object
#                 new_artist.add_album(new_album)
#                 artist_list.append(new_artist)
#                 new_artist = Artist(artist_field)
#                 new_album = None
#
#             if new_album is None:
#                 new_album = Album(album_field, year_field, new_artist)
#             elif new_album.name != album_field:
#                 # we just read a new album for the current artist
#                 # store the current album in the artist's collection than create a new album object
#                 new_artist.add_album(new_album)
#                 new_album = Album(album_field, year_field, new_artist)
#
#             # create a new song object and add it to the current album's collection
#             new_song = Song(song_field, new_artist)
#             new_album.add_song(new_song)
#
#         #After read the last line of the text file, we will have ana artist and album that haven't
#         # been store-process then now
#         if new_artist is not None:
#             if new_album is not None:
#                 new_artist.add_album(new_album)
#             artist_list.append(new_artist)
#     return artist_list
#
#
# if __name__ == "__main__":
#     artistss = load_data()
#     print(len(artistss))


def load_data():
    artist_list = []
    current_artist, current_album = None, None

    with open('albums.txt', 'r', encoding='utf-8') as albums:
        for line in albums:
            artist_name, album_name, year, song_title = line.strip('\n').split('\t')
            year = int(year)

            # Check if we're dealing with a new artist
            if current_artist is None or current_artist.name != artist_name:
                if current_artist:
                    artist_list.append(current_artist)
                current_artist = Artist(artist_name)
                current_album = Album(album_name, year, current_artist)
                current_artist.add_album(current_album)

            # Check if we're dealing with a new album
            if current_album.name != album_name:
                current_album = Album(album_name, year, current_artist)
                current_artist.add_album(current_album)

            # Add the song to the current album
            current_album.add_song(Song(song_title, current_artist))

        # Add the last artist
        if current_artist:
            artist_list.append(current_artist)

    return artist_list



if __name__ == "__main__":
    artists = load_data()
    print(f"Loaded {len(artists)} artists.")















