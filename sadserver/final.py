from re import I


if __name__=="__main__":
    counts={}

    with open ("final.log","r") as file:
        for line in file:
            ip=line.strip()
            if ip not in counts:
                counts[ip]=0
            else:
                counts[ip]+=1
        largets=max(counts,key=counts.get)
        ip=max(counts)

    print(ip,counts[largets])
