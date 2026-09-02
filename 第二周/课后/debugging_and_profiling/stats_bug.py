import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG, format="%(levelname)s:%(message)s")


def mean(values):
    total = 0
    for value in values:
        total += value
        logging.debug("value=%s total=%s", value, total)
    return total / len(values)


def report(values):
    return f"mean={mean(values):.2f}"


if __name__ == "__main__":
    print(report([10, 20, 30, 40]))