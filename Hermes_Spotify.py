import spotipy

sp = spotipy.Spotify()

def Search(queryString):
    results = sp.search(q=queryString, limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print ' ', i, t['name']
