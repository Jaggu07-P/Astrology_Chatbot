import requests

def get_astrology_data(dob, tob, place):
    url = "https://aztro.sameerkumar.website?sign=aries&day=today"  # dummy fallback
    response = requests.post(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Astro API Error: Failed to fetch astrology data")
