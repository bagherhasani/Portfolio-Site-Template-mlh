import json


servers={}
highest_cpu=-1
highes_cpu_name=""
highest_mem_name=""
highest_mem=-1
if __name__=="__main__":
    with open("servers.json") as file:
        data=json.load(file)
        for line in data:
            s_name=line["name"]
            s_status=line["status"]
            s_cpu=line["cpu"]
            s_memory=line["memory"]

            if s_status!="running":
                continue

            if s_cpu>80:
                print(s_name,s_cpu)

            if s_cpu>highest_cpu:
                highest_cpu=s_cpu
                highes_cpu_name=s_name

            if s_memory>highest_mem:
                highest_mem=s_memory
                highest_mem_name=s_name

    print("highest cpu:",highest_cpu,highes_cpu_name)
    print("highest mem:",highest_mem,highest_mem_name)