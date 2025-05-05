# from dotenv import load_dotenv
# import httpx
# import os
# load_dotenv()
# ORS_API_KEY = os.getenv("ORS_API_KEY")

# def test_ors_api():
#     url = "https://api.openrouteservice.org/v2/directions/driving-car"
#     headers = {"Authorization": f"Bearer {ORS_API_KEY}"}
#     params = {
#         "start": "-46.57421, -23.61713",  # Example starting point (lat, lon)
#         "end": "-46.63338, -23.5475"  # Example destination (lat, lon)
#     }
#     response = httpx.get(url, params=params, headers=headers)
#     if response.status_code == 200:
#         print("OpenRouteService API Response:")
#         print(response.json())
#     else:
#         print(f"Error {response.status_code}: {response.text}")

# test_ors_api()

import requests

GEOAPIFY_API_KEY = "3c55174be87b47f6800fe947cf913515"

url = "https://api.geoapify.com/v1/geocode/search"
params = {
    "text": "DWARAKA TIRUMALA",
    "apiKey": GEOAPIFY_API_KEY,
    "limit":20
}

response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print("✅ Geoapify API Key is working!")
#     print("First result:", data['features']['properties']['formatted'])
# else:
#     print("❌ Geoapify Error:", response.status_code, response.text)
if response.status_code == 200:
    data = response.json()
    print("✅ Geoapify API Key is working!")
    print("length of the data[features]",len(data['features']))

    features = data.get('features', []) # data.get() gives the values in list ane each value is in dict form 
    for i, feature in enumerate(features):
        print(f"{i + 1} result:", feature['properties']['formatted'])
else:
    print("❌ Geoapify Error:", response.status_code, response.text)
# import requests

# OTM_API_KEY = "5ae2e3f221c38a28845f05b6bb9590e891f0bc2d12a81c474ae395c5"

# url = "https://api.opentripmap.com/0.1/en/places/radius"
# params = {
#     "radius": 500,
#     "lon": 81.0952431,
#     "lat": 16.7106604,
#     "apikey": OTM_API_KEY,
#     "format": "json"
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     print("✅ OTM API Key is working!")
#     print("Found places:", len(data))
#     if data:
#         print("Sample place:", data[0]['name'])
# else:
#     print("❌ OTM Error:", response.status_code, response.text)
