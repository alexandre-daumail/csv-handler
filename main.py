import fire
import csv
import json


def make_json(file: str):
    """
        Convert a CSV to JSON
        :param file: path string. Needs to be a csv
        :return: sum of a and b
    """
    data = {}

    # Open a csv reader called DictReader
    with open(file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        link_id = 0
        for rows in csvReader:
            link_id += 1
            data[link_id] = rows

    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    fire.Fire({
        "import": make_json
    })
