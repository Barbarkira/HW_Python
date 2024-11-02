import json
from typing import List, Union

class FlowersDataset:
    def __init__(self, json_file: str):
        self.flowers = []

        with open(json_file, 'r') as f:
            self.flowers = json.load(f)

    def get_items(self, properties: dict) -> Union[List[str], str]:
        result = []


        flower_types = properties.get("type", [])
        colors = properties.get("color", [])


        if isinstance(flower_types, str):
            flower_types = [flower_types]
        if isinstance(colors, str):
            colors = [colors]


        for flower in self.flowers:
            flower_type = flower['path'].split('/')[1]  # Assumes path format: "flowers/{type}/{filename}"
            flower_color = flower['path'].split('/')[-1].split('_')[1]  # Assumes filename format: "flower_color.jpeg"

            type_check = flower_type in flower_types if flower_types else True
            color_check = flower_color in colors if colors else True

            if type_check and color_check:
                result.append(flower['path'])

        return result if result else []

# Usage example
# dataset = FlowersDataset("flowers.json")
# print(dataset.get_items({"type": "rose", "color": "red"}))
# print(dataset.get_items({"type": ["rose", "tulip"], "color": "red"}))
# print(dataset.get_items({"type": "tulip", "color": ["red", "blue"]}))
# print(dataset.get_items({"type": "tulip", "color": "magenta"}))