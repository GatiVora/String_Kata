import re

def add(numbers):
    if not numbers:
        return 0

    delimiter = ','
    numbers = re.split(rf'[{delimiter}\n]', numbers)
    total = 0
    negatives = []
    for number in numbers:
        if number:
            try:
                num = int(number)
                if num < 0:
                    negatives.append(num)
                else:
                    total += num
            except Exception as e:
                raise ValueError("Kindly provide a string of valid integers separated using a single delimiter")
        else:
            raise ValueError("Invalid input")

    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return total