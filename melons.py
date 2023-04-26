import csv

class Melon:
    def __init__(self,melon_id,common_name,price,image_url,color,seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row["melon_id"]
        melon = Melon(melon_id,row["common_name"],float(row["price"]),row["image_url"],row["color"],eval(row["seedless"]))

        melon_dict[melon_id] = melon
