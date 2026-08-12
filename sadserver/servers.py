import json
if __name__=="__main__":
    with open("servers.json") as file:
        data=json.load(file)
        for item in data:
            host=item["host"]
            cpu=int(item["cpu"])
            status=item["status"]

            if cpu>80:
                print(host,cpu,status)


    with open("servers.json") as file:
        data=json.load(file)
        for line in data:
            host=line["host"]
            cpu=int(item["cpu"])
            status=item["status"]

            if cpu>80:
                print(host,cpu,status)