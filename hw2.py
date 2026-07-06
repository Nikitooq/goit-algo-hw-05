import re

def generator_numbers(text: str):
    pattern = r" [+-]?\d+(?:\.\d+)? "
    numbers = [float(x) for x in re.findall(pattern, text)]
    yield numbers




def sum_profit(text: str, func):
    counter = 0
    for numbers in func(text):
        for number in numbers:
            counter += number
    return counter



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
