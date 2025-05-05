# Shiva
from mcp.server.fastmcp import FastMCP
from typing import List
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

# ORS_API_KEY = os.getenv("ORS_API_KEY")
# GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
# OTM_API_KEY = os.getenv("OPENTRIPMAP_API_KEY")
ORS_API_KEY="5b3ce3597851110001cf6248242468606374428f88f4763f2aea5552"
GEOAPIFY_API_KEY="3c55174be87b47f6800fe947cf913515"
OTM_API_KEY="5ae2e3f221c38a28845f05b6bb9590e891f0bc2d12a81c474ae395c5"

mcp = FastMCP("AmazonTravelGuide")

# Helper to get coordinates
def get_coordinates(place: str):
    url = "https://api.opentripmap.com/0.1/en/places/geoname"
    params = {"name": place, "apikey": OTM_API_KEY}
    r = httpx.get(url, params=params)
    data = r.json()
    if "lat" in data and "lon" in data:
        return data["lat"], data["lon"]
    else:
         raise ValueError(f"Coordinates not found for {place}")


@mcp.tool()
def get_travel_route(from_location: str) -> str:
    """Get route distance and time from source to Amazon Rainforest (Manaus)"""
    try:
        src_lat, src_lon = get_coordinates(from_location)
        dest_lat, dest_lon = get_coordinates("Manaus, Brazil")
        url = "https://api.openrouteservice.org/v2/directions/driving-car"
        headers = {"Authorization": ORS_API_KEY}
        params = {"start": f"{src_lon},{src_lat}", "end": f"{dest_lon},{dest_lat}"}
        r = httpx.get(url, params=params, headers=headers)
        route = r.json()
        summary = route["features"][0]["properties"]["summary"]
        return f"From {from_location} to Manaus: ~{summary['distance'] / 1000:.1f} km, ~{summary['duration'] / 3600:.1f} hours by car."
    except Exception as e:
        return f"Unable to calculate route. Error: {str(e)}"


@mcp.tool()
def get_nearby_hotels(location: str) -> List[str]:
    """Find hotels near a location using Geoapify"""
    try:
        lat, lon = get_coordinates(location)
        url = "https://api.geoapify.com/v2/places"
        params = {
            "categories": "accommodation.hotel",
            "filter": f"circle:{lon},{lat},5000",
            "limit": 5,
            "apiKey": GEOAPIFY_API_KEY
        }
        r = httpx.get(url, params=params)
        
        # Check if the response is OK
        if r.status_code != 200:
            print(f"Geoapify API error: {r.status_code} - {r.text}")
            return ["No hotels found or API error occurred."]
        
        hotels = r.json()
        print(f"Geoapify response: {hotels}")
        
        return [place["properties"]["name"] for place in hotels.get("features", []) if "name" in place["properties"]]

    except Exception as e:
        print("Error in get_nearby_hotels:", str(e))
        return ["No hotels found or error occurred."]


@mcp.tool()
def get_precautions() -> List[str]:
    """Precautions and suggestions before traveling to Amazon"""
    return [
        "Get vaccinated for yellow fever and malaria.",
        "Carry insect repellent and mosquito nets.",
        "Travel with a local guide or group.",
        "Avoid swimming in unknown water bodies.",
        "Stay hydrated and pack waterproof gear."
    ]

@mcp.tool()
def get_adventure_spots(location: str) -> List[str]:
    """Get nearby adventure spots like hiking and nature sites"""
    try:
        lat, lon = get_coordinates(location)
        url = "https://api.opentripmap.com/0.1/en/places/radius"
        headers = {"Authorization": f"Bearer {OTM_API_KEY}"}
        params = {
            "radius": 10000,
            "lon": lon,
            "lat": lat,
            "rate": 2,
            "kinds": "natural,hiking",
            "format": "json",
            "limit": 5,
            "apikey": OTM_API_KEY
        }
        r = httpx.get(url, params=params)
        data = r.json()
        return [place["name"] for place in data if "name" in place and place["name"]]
    except:
        return ["No adventure spots found."]

@mcp.tool()
def get_monuments_and_food(location: str) -> List[str]:
    """Get famous foods or cultural places near location"""
    try:
        lat, lon = get_coordinates(location)
        url = f"https://api.opentripmap.com/0.1/en/places/radius"
        headers = {"Authorization": f"Bearer {OTM_API_KEY}"}
        params = {
            "radius": 10000,
            "lon": lon,
            "lat": lat,
            "kinds": "foods,cultural,historic",
            "limit": 5,
            "format": "json",
            "apikey": OTM_API_KEY
        }
        r = httpx.get(url, params=params)
        data = r.json()
        return [place["name"] for place in data if "name" in place and place["name"]]
    except:
        return ["Could not retrieve local attractions."]

@mcp.resource("hello://{name}")
def greet_user(name: str) -> str:
    """Greet user"""
    return f"Hello {name}! Ready for your Amazon rainforest adventure?"

if __name__ == "__main__":
    mcp.run()
