import argparse
import time
import tracemalloc
from collections import deque


def list_queue(n):
    queue = list(range(n))
    total = 0
    while queue:
        total += queue.pop(0)
    return total


def deque_queue(n):
    queue = deque(range(n))
    total = 0
    while queue:
        total += queue.popleft()
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["list", "deque"])
    parser.add_argument("n", type=int)
    args = parser.parse_args()

    function = list_queue if args.mode == "list" else deque_queue
    tracemalloc.start()
    start = time.perf_counter()
    result = function(args.n)
    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(
        f"mode={args.mode} result={result} "
        f"elapsed={elapsed:.6f} peak_kib={peak / 1024:.1f}"
    )


if __name__ == "__main__":
    main()