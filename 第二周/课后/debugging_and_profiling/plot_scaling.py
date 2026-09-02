import csv
import matplotlib.pyplot as plt

with open("queue_scaling.csv") as file:
    rows = list(csv.DictReader(file))

for mode in ("list", "deque"):
    selected = [row for row in rows if row["mode"] == mode]
    x = [int(row["n"]) for row in selected]
    y = [float(row["median_seconds"]) for row in selected]
    plt.plot(x, y, marker="o", label=mode)

plt.xlabel("Queue size")
plt.ylabel("Median time (s)")
plt.title("list.pop(0) vs deque.popleft()")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("queue_scaling.png", dpi=180)