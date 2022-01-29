import pandas as pd
from pathlib import Path

def fixed_dataset() -> pd.DataFrame:
	flight_list = pd.concat(
		pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
		for file in Path("/Users/neyirerdeser/Documents/MIAE Workshops/FlightTracker/data_set").glob("flightlist_*.csv.gz")
	)
	return flight_list