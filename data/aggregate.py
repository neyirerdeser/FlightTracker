import pandas as pd
from pathlib import Path
from api import fetcher
from data import utils

def fixed_dataset() -> pd.DataFrame:
    # https://zenodo.org/record/4601480
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in
        Path("/Users/neyirerdeser/Documents/MIAE Workshops/FlightTracker/data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list

def formed_dataset(*, start_time:str, end_time:str) -> pd.DataFrame:
    start_dt_dt, start_dt_unix = utils.converter(dt=start_time)
    end_dt_dt, end_dt_unix = utils.converter(dt=end_time)
    flights_json = fetcher.flights_accessor(int(start_dt_unix), int(end_dt_unix))

    df = pd.DataFrame(data=flights_json)
    df.drop(labels=[], axis=1, inplace=True)