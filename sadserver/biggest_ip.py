


if __name__=="__main__":
    print("hello")

    seen={}
    with open("access.log") as file:
        for item in file:
            parts=item.split()
            ip= parts[1]
            if ip in seen:
                seen[ip]+=1
            else:
                seen[ip]=1

        biggest=max(seen,key=seen.get)
        print(biggest,seen[biggest])

