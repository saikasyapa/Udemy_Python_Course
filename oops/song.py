# class Song:
#     """ Class to represent song
#
#     Attributes:
#         title (str) : The title of the song
#         artist (str) : An artist object representing the song creator.
#         duration (int) : the duration of the song in seconds. maybe zero
#     """
#     def __init__(self,title,artist,duration=0):
#         self.title = title
#         self.artist = artist
#         self.duration = duration
#
# # help(Song)
# print(Song.__doc__)
# print(Song.__init__.__doc__)
# Song.__init__.__doc__ = """
#         Song init method
#
#         :param title: Initialised the 'title' attribute
#         :param artist: An artist object representation of song creator
#         :param duration:the duration of the song in seconds.
#               will default to zero if not specified
#         """
# help(Song)



# ####### DocStrings and
#
# class Song:
#     """ Class to represent song
#
#     Attributes:
#         title (str) : The title of the song
#         artist (str) : An artist object representing the song creator.
#         duration (int) : the duration of the song in seconds. maybe zero
#     """
#     def __init__(self,title,artist,duration=0):
#         """
#         Song init method
#
#         :param title: Initialised the 'title' attribute
#         :param artist: An artist object representation of song creator
#         :param duration:the duration of the song in seconds.
#               will default to zero if not specified
#         """
#         self.title = title
#         self.artist = artist
#         self.duration = duration
#
# # help(Song)
# print(Song.__doc__)
# print(Song.__init__.__doc__)
#
# # Songs1 = Song('Believe','Justin Biber',2.60)
# # print(Songs1.duration)
# # print(Songs1.artist)
# # print(Songs1.title)




