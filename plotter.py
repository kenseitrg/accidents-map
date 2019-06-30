import pandas as pd
import matplotlib.pyplot as plt
import mplleaflet

def generate_map(data_name:str, op_name:str) -> None:
    data = pd.read_pickle(data_name)
    fig, ax = plt.subplots()
    ax.scatter(data["longtitude"], data["latitude"], c=data["accidents"], cmap="jet")
    mplleaflet.show(fig=fig, path=op_name)

if __name__ == "__main__":
    generate_map("electro_df.pkl", "electro_map.html")
    generate_map("water_df.pkl", "water_map.html")