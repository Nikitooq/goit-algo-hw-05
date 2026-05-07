import sys

file_path = sys.argv[1]

def parse_log_line(line: str) -> dict:
    pass


def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="UTF-8") as file:
        line = file.readlines()
    return line

def filter_logs_by_level(logs: list, level:str) -> list:
    pass

def coun_logs_by_level(logs: list) -> dict:
    pass


def display_log_counts(counts: dict):
    pass

print(load_logs(file_path))