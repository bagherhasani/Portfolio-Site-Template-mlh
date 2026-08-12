

if __name__=="__main__":
    ips={}
    malformed=0

    try:
        with open("input.txt") as file:
            for line in file:
                parts=line.strip().split("|")


                # malformed
                if len(parts)!=3:
                    malformed+=1
                    continue

                ip=parts[0].strip()
                latency=int(parts[1].strip())
                status=parts[2].strip()

                # if ip not in ips add it 
                if ip not in ips:
                    ips[ip]={
                        "count":1,
                        "latency":latency,
                        "failure":0
                    }

                # if ip in ips add count
                else:
                    ips[ip]["count"]+=1
                    ips[ip]["latency"]+=latency

                if status=="FAIL":
                    ips[ip]["failure"]+=1


            #calculate average latency for each ip 
             #write result to summary.txt
            with open("summary.txt","w") as output:
                print("IP reports",file=output)

                for ip in ips:
                    average=ips[ip]["latency"]/ips[ip]["count"]
                    print(
                        ip,
                        "count="+str(ips[ip]["count"]),
                        "average="+str(average),
                        "failure="+str(ips[ip]["failure"]),
                        file=output)

                print(file=output)
                print("malformed:",malformed,file=output)
                                                   
                             



    except FileNotFoundError:
        print("file not found")