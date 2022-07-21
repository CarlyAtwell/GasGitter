"""Receives and interprets gas price data"""
import json
from pathlib import Path

curr_loc = {"x":62739, "y": 28339}
curr_gals = 12
mpg = 25

def main():
    """_summary_"""
    gas_data = json.loads(Path("gas_data.json").read_text(encoding="utf-8"))
    cheap_reg = cheapest(gas_data, "regular")
    cheap_mid = cheapest(gas_data, "mid_grade")
    cheap_prem = cheapest(gas_data, "premium")
    cheap_dies = cheapest(gas_data, "diesel")

    if can_make_it(cheap_reg):
        station_type = cheap_reg["station_type"]
        station_loc = cheap_reg["location"]
        print(f"Cheapest regular gas within reach is at the {station_type} located here: {station_loc}")
    else:
        print("Cheapest regular gas out of reach")

    if can_make_it(cheap_mid):
        station_type = cheap_mid["station_type"]
        station_loc = cheap_mid["location"]
        print(f"Cheapest mid-grade gas within reach is at the {station_type} located here: {station_loc}")
    else:
        print("Cheapest mid-grade gas out of reach")

    if can_make_it(cheap_prem):
        station_type = cheap_prem["station_type"]
        station_loc = cheap_prem["location"]
        print(f"Cheapest premium gas within reach is at the {station_type} located here: {station_loc}")
    else:
        print("Cheapest premium gas out of reach")

    if can_make_it(cheap_dies):
        station_type = cheap_dies["station_type"]
        station_loc = cheap_dies["location"]
        print(f"Cheapest diesel gas within reach is at the {station_type} located here: {station_loc}")
    else:
        print("Cheapest diesel gas out of reach")


def can_make_it(station: dict) -> bool:
    xdif = station["location"]["x"] - curr_loc["x"]
    ydif = station["location"]["x"] - curr_loc["x"]
    miles_left = curr_gals*mpg
    return miles_left>(xdif+ydif)

def cheapest(stations: dict, gas_type: str) -> dict:
    cheapest = list(stations.values())[0]
    for station in list(stations.values()):
        if float(station["prices"][gas_type]) < float(cheapest["prices"][gas_type]):
            cheapest = station
    return cheapest

if __name__ == '__main__':
    main()
