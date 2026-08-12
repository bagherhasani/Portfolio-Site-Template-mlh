
if __name__=="__main__":

    seen={}
    with open("actions.log") as file:
        for line in file:
            parts=line.split()
            name=parts[0]

            if name not in seen:
                seen[name]=1
            else:
                seen[name]+=1

    print(seen)

            