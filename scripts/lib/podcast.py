
from bs4 import BeautifulSoup
import requests

channels = ["Apple", "Google", "Spotify"]

urls = {
    "Apple": "https://podcasts.apple.com/th/podcast/codeclub-podcast/id1485111503",
    "Google": "https://podcasts.google.com/?feed=aHR0cHM6Ly9jb2RlY2x1Yi5iaWdiZWFycy5pby9wb2RjYXN0L3Jzcy8",
    "Spotify": "https://open.spotify.com/show/7z1p407E9M7huVVqojLia1"
}

def _parse_apple_links(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    return [x['href'] for x in soup.select('a.tracks__track__link--block') ] 

def _parse_google_links(html_doc):
    return ["TODO -- parse: https://podcasts.google.com/?feed=aHR0cHM6Ly9jb2RlY2x1Yi5iaWdiZWFycy5pby9wb2RjYXN0L3Jzcy8"] * 100   

def _parse_spotify_links(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    #<meta property="music:song" content="https://open.spotify.com/episode/3cm0w2ZElG9vHXUsGLCy87">
    return [x["content"] for x in soup.select('meta[property="music:song"]') ] 

parsers = {
    "Apple": _parse_apple_links,
    "Google": _parse_google_links,
    "Spotify": _parse_spotify_links
}
    

def latest_episode_links():
    contents = {k: requests.get(v).text for k, v in urls.items()}
    episode_links = {k: parsers[k](v) for k, v in contents.items()}

    return [ (c,episode_links[c]) for c in channels ]
