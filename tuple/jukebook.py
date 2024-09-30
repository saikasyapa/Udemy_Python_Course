

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
while True:

    for number,value in enumerate(albums):
        title,artist,year,songs = value
        print(number + 1,title)
    choice = int(input("select the any album from the above"))
    if (choice >=1) and  (choice <= len(albums)):
        songs_list = albums[choice - 1][3]
        for j,k in enumerate(songs_list):
            m,n = k
            print(m,n)
        print(40 * "*")
        print()
    elif choice == 0:
        print("Thank you")
        break
    else:
        print("Enter valid playlist or select '0' to exit")
    choice1 = int(input("select the song you want to play"))
    if choice1 >=0 or choice1 <= len(songs_list):
        song = songs_list[choice1 -1][1]
        print(f"You selected song is {song}")
    else:
        print(number + 1,title)


