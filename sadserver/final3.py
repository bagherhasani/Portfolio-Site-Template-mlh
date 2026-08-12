if __name__=="__main__":
    user={}
    stat={}
    with open("user.csv") as file:
        next(file)
        for line in file:
            parts=line.strip().split(",")
            id=int(parts[0])
            name=parts[1]

            user[id]=name

    #print(user)


    #second file opening 
    with open("activity.csv","r") as file:
        next(file)
        for line in file:
            parts=line.strip().split(",")
            id=int(parts[0])
            action=parts[1]
            duration=int(parts[2])

            if action=="login":
                continue

            if id in user:
                if user not in stat:
                    stat[id]={
                        "count":0,
                        "total":0
                    }
                
