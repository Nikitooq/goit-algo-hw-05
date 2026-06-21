import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    line = line.split()
    message = " ".join(line[3:])
    line_dict = {"date": line[0], "time": line[1], "level": line[2], "message": message}
    return line_dict

def load_logs(file_path: str) -> list:
    logs = list()
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            logs.append(parse_log_line(line))
    return logs

def filter_logs_by_level(logs: list, level:str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log["level"] for log in logs))

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

if __name__ == "__main__":
    file_path = sys.argv[1]

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()

        filtered = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")
