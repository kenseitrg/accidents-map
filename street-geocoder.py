import pandas as pd
import geocoder as geo
from typing import Tuple
from tqdm import tqdm

def read_data(fname:str) -> pd.DataFrame:
    df = pd.read_csv(fname, header=None, names=["street", "accidents"])
    return df

def get_lat_long(topo:str) -> Tuple[int, int]:
    gcode = geo.yandex(f"{topo}, Севастополь")
    return (gcode.lat, gcode.lng)

def update_coordinates(data:pd.DataFrame) -> pd.DataFrame:
    for i in tqdm(range(data.shape[0])):
        row = data.iloc[i, :]
        str_name = row["street"]
        (lat, lng) = get_lat_long(str_name)
        data.loc[data["street"] == str_name, "latitude"] = lat
        data.loc[data["street"] == str_name, "longtitude"] = lng
    return data

if  __name__ == "__main__":
    electro_df = read_data("electro_count.csv")
    electro_df = update_coordinates(electro_df)
    electro_df.to_pickle("electro_df.pkl")
    bad_names = electro_df[electro_df.duplicated(subset=["latitude", "longtitude"])]
    bad_names.to_csv("bad_names_electro.csv")
    water_df = read_data("water_count.csv")
    water_df = update_coordinates(water_df)
    water_df.to_pickle("water_df.pkl")
    bad_names = water_df[water_df.duplicated(subset=["latitude", "longtitude"])]
    bad_names.to_csv("bad_names_water.csv")