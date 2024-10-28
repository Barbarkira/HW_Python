import os
import json


def convert_to_json(path_to_dataset: str = "class_3/hw2/t2_data/flowers",
                    json_path: str = "class_3/hw2/t2_data/flowers/flowers.json") -> str:
    flowers = []

    for flower_type in os.listdir(path_to_dataset):
        flower_type_path = os.path.join(path_to_dataset, flower_type)

        if os.path.isdir(flower_type_path):
            for filename in os.listdir(flower_type_path):
                if filename.endswith('.jpeg'):
                    color_info = filename.split('_')[1]
                    flower_path = os.path.join(flower_type, filename)


                    flowers.append({
                        "path": flower_path,
                        "color": color_info,
                        "type": flower_type
                    })

    result = {"flowers": flowers}

    with open(json_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)
    return json_path


# Пример использования
json_output_path = convert_to_json()
print(f"JSON output saved to: {json_output_path}")