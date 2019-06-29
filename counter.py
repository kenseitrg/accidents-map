from collections import Counter
from typing import List
import csv

def read_data(fname:str) -> List:
    with open(fname, "r", encoding="utf-8") as ip:
        data =[street.replace("\n", "") for street in ip.readlines()]
    return data

def count_occuarances(data: List) -> Counter:
    cnt = Counter(data)
    return cnt

water_data = read_data("water_streets.txt")
electro_data = read_data("electro_streets.txt")

water_count = count_occuarances(water_data)
electro_count = count_occuarances(electro_data)

def write_to_csv(fname:str, data:Counter) -> None:
    with open(fname, "w", encoding="utf-8") as op:
        writer = csv.writer(op)
        writer.writerows([(k, v) for k,v in data.items()])

write_to_csv("water_count.csv", water_count)
write_to_csv("electro_count.csv", electro_count)