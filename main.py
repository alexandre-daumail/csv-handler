import fire
import csv
import json


def make_json(csv_file_path: str, json_file_path):
    """
        Convert a CSV to JSON
        :param csv_file_path: path string. Needs to be a csv
        :param json_file_path: path string.
        :return: sum of a and b
    """
    data = {}

    # Open a csv reader called DictReader
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        link_id = 0
        for rows in csvReader:
            link_id += 1
            data[link_id] = rows

    print(json.dumps(data, indent=4))
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    fire.Fire({
        "import": make_json
    })
