
if __name__=="__main__":
    try:
        with open("input.txt") as file:
            for line in file:
                parts=line.strip().split("|")
                ip=parts[0].strip()
                latency=int(parts[1].strip())
                status=parts[2].strip()
        
                
                print(ip,latency,status)




    except FileNotFoundError:
        print("file not found")