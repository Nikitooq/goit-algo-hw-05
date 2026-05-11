import sys
from collections import namedtuple

file_path = sys.argv[1]
level = sys.argv[2]

def parse_log_line(line: str) -> dict:
    named_lines_dict = namedtuple("Log_infos", ["date", "time", "level", "message"])
    line = line.split()
    message = " ".join(line[3:])
    line_dict = named_lines_dict(line[0], line[1], line[2], message)
    return line_dict


def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="UTF-8") as file:
        line = file.readline()
    logs = parse_log_line(line)
    return logs

def filter_logs_by_level(logs: list, level:str) -> list:
    print(
        f"""Рівень логування | Кількість\n
        INFO info\n
        DEBUG debug\n
        ERROR error\n
        WARNING warning\n
        """
            )

def count_logs_by_level(logs: list) -> dict:
    pass


def display_log_counts(counts: dict):
    pass

print(load_logs(file_path))