"""
/* ### requests.log ###
10:00:00 | OPEN | R1 | /search
10:00:01 | OPEN | R2 | /order
10:00:02 | CLOSE | R1 | OK
10:00:03 | OPEN | R3 | /pay
10:00:04 | CLOSE | R3 | FAIL
10:00:05 | OPEN | R4 | /search
10:00:06 | CLOSE | R4 | OK
10:00:07 | CLOSE | R2 | OK
10:00:08 | OPEN | R5 | /order
10:00:09 | OPEN | R6 | /pay
10:00:11 | CL
10:00:12 | CLOSE | R6 | OK

### Expected Output (summary.txt): ###
Endpoint stats (completed requests):
    /order   count=1  avg_seconds=6.0
    /pay     count=2  avg_seconds=2.0
    /search  count=2  avg_seconds=1.5
Failed requests: 1
Stuck requests (opened, never closed): 1
Malformed lines: 1
*/


"""


malformed=0
requests={}
completed={}
faild={}
stuck={}

if __name__=="__main__":
    try:
        with open("requests.log") as file:
            for line in file:
                
                parts=line.strip().split("|")
                if len(parts)!=4:
                    malformed+=1
                    continue



                s_time=parts[0].strip()
                s_status=parts[1].strip()
                s_request=parts[2].strip()
                s_status_endpoint=parts[3].strip().lstrip("/")

                if s_status=="OPEN":
                   requests[s_request] = {
                        "timestamp": s_time,
                        "endpoint": s_status_endpoint 
                        }
                   print("opened: ",s_request)

                elif s_status=="CLOSE":
                        if s_request in requests:
                            print("closed: ",s_request)
                    



        #print(requests,end="")



            
    except FileNotFoundError:
        print("file not found")