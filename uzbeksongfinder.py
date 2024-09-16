import requests

class UzbekSongFinder:
    def __init__(self, track):
        self.track = track

    def search(self):
        response = requests.get("https://api.rizanova.uz/v2/search/all?include_premiere=1&query=" + self.track)
        if response.status_code == 200:
            return response.json()
        else:
            return f"ERROR: {response.status_code}"
