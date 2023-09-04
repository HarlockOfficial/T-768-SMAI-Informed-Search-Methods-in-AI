import enum
from typing import Union


class DataType(enum.Enum):
    BT_SOLVER = "SolverType.BT"
    BJ_SOLVER = "SolverType.BJ"
    CBJ_SOLVER = "SolverType.CBJ"


def load_file(filename: str) -> Union[list[str], str]:
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    base_file_name = filename.split('/')[-1].split('.')[0]
    return lines, base_file_name


def data_to_list(lines: list) -> list[str]:
    data = []
    for line in lines:
        data.append([entry.strip() for entry in line.split()[1:-1]])
    return data


def split_data_in(data, column_index, data_categories) -> dict[str, list[str]]:
    split_data = dict()
    for category in data_categories:
        split_data[category.value] = []
    for row in data:
        split_data[row[column_index]].append(row)
    return split_data


def extract_data(filename: str) -> Union[dict[str, list[str]], str]:
    lines, base_file_name = load_file(filename)
    data = data_to_list(lines)
    data = split_data_in(data, 0, [DataType.BT_SOLVER, DataType.BJ_SOLVER, DataType.CBJ_SOLVER])
    return data, base_file_name
