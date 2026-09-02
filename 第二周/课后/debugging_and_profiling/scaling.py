import csv
import statistics
import timeit

from queue_bench import deque_queue, list_queue

sizes = [5000, 10000, 20000, 40000]
methods = [("list", list_queue), ("deque", deque_queue)]

with open("queue_scaling.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["mode", "n", "median_seconds"])

    for n in sizes:
        for name, function in methods:
            times = timeit.repeat(lambda: function(n), number=1, repeat=5)
            median = statistics.median(times)
            writer.writerow([name, n, median])
            print(f"{name:5} n={n:5} median={median:.6f}s")