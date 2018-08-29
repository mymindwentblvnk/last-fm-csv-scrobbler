import csv

import pylast

import settings


NETWORK = pylast.LastFMNetwork(api_key=settings.API_KEY,
                               api_secret=settings.API_SECRET,
                               username=settings.USER_NAME,
                               password_hash=pylast.md5(settings.PASSWORD))


class Song(object):

    def __init__(self, artist, title, timestamp, album=None):
        self.artist = artist
        self.title = title
        self.timestamp = timestamp
        self.album = album

    def __repr__(self):
        return """
Artist:    {artist}
Title:     {title}
Album:     {album}
Timestamp: {timestamp}
""".format(artist=self.artist,
           title=self.title,
           album=self.album,
           timestamp=self.timestamp)


def chunks(l, chunk_size=50):
    for i in range(0, len(l), chunk_size):
        yield l[i:i + chunk_size]


def scrobble_songs(songs):
    for index, chunk in enumerate(chunks(songs), 1):
        print(index, " - Scrobbeling", len(chunk), "songs.")
        song_dicts = [{
            'title': s.title,
            'artist': s.artist,
            'timestamp': s.timestamp,
            'album': s.album
        } for s in chunk]
        NETWORK.scrobble_many(song_dicts)


def get_songs_from_csv(csv_path, artist_column_name, title_column_name,
                       album_column_name, timestamp_column_name):
    with open(csv_path, 'r') as csv_file_handler:
        rows = csv.DictReader(csv_file_handler)
        songs = [Song(artist=r[artist_column_name],
                      title=r[title_column_name],
                      album=r[album_column_name],
                      timestamp=int(r[timestamp_column_name])) for r in rows]
        return songs


if __name__ == '__main__':
    print("Last.fm CSV Scrobbler")
    print("*********************")
    songs = list()
    for info in settings.CSV_FILE_INFO:
        print("Loading", info['csv_path'])
        songs.extend(get_songs_from_csv(**info))
        print("Last song loaded")
        print(songs[-1])
    scrobble_songs(songs)
    print("Done")
