from bs4 import BeautifulSoup
from pathlib import Path
import re
from typing import List

messages_path = Path(r"data\messages.html")

with open(messages_path, 'r', encoding="utf-8") as html_doc:
    soup = BeautifulSoup(html_doc, "html.parser")


raw_messages = [m.find(class_='text') for m in soup.find_all(id=re.compile("^message"))]
filtered_messages = [msg for m in raw_messages if m for msg in m.contents]
water_messages = [m for m in filtered_messages if 'ГУПС' in m]
electro_messages = [m for m in filtered_messages if 'Севастопольэнерго' in m]

def filter_topos(messages:List) -> List:
    op = []
    for message in messages:
        message = message.replace(". ", ".")
        message = message.split(" ")
        op += [street.strip().replace("-", "").replace(",", "") \
                for street in message if street.startswith("ул.")]
    return op

water_streets = filter_topos(water_messages)
electro_streets = filter_topos(electro_messages)

def write_to_file(fname:str, data:List) -> None:
    with open(fname, "w", encoding="utf-8") as f:
        f.writelines("%s\n" % item for item in data)

write_to_file("water_streets.txt", water_streets)
write_to_file("electro_streets.txt", electro_streets)