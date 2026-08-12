

from itertools import count


if __name__=="__main__":

    stat = {}

with open("access2.log") as file:
    for item in file:
        parts = item.split()

        path = parts[3]
        status = parts[4]
        latency = int(parts[5])

        if path not in stat:
            stat[path] = {
                "count": 1,
                "total": latency,
                "min": latency,
                "max": latency
            }
        else:
            stat[path]["count"] += 1
            stat[path]["total"] += latency
            stat[path]["min"] = min(stat[path]["min"], latency)
            stat[path]["max"] = max(stat[path]["max"], latency)

for path in stat:
    count = stat[path]["count"]
    total = stat[path]["total"]
    minimum = stat[path]["min"]
    maximum = stat[path]["max"]
    average = total / count

    print(path, "count=", count, "avg=", average, "min=", minimum, "max=", maximum)