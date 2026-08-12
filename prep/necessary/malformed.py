
if __name__=="__main__":
    malformed=0

    try:
        with open("input.txt","r") as file:
            for line in file:
                 parts=line.strip().split("|")
                 #malformed
                 if len(parts)!=3:
                     malformed+=1
                     continue

                 ip=parts[0].strip()
                 latency=parts[1].strip()
                 status=parts[2].strip()

                 print(ip,latency,status)

            print("malformed:",malformed)



    except FileNotFoundError:
        print("file not found")