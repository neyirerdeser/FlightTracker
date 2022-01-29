import requests
from api.config import settings

ROOT_URL = settings.ROOT_URL

def states_accessor():
	url = "/states/all"
	r = requests.get(url)
	if not r.ok: raise RuntimeError(r)
	print(r.json())

def tracks_accessor():
	url="/tracks/all?icao24=3c4b26&time=0"
	r = requests.get(url)
	if not r.ok: raise RuntimeError(r)
	print(r.json())

