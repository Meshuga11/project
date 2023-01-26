import csv


def get_list_dicts_from_csv(file_path: str):
    with open(file_path, encoding='utf-8-sig') as f:
        return [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]