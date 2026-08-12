if __name__=="__main__":

    users={}
    stat={}

    #read user.csv
    with open("user.csv","r") as file:
        next(file)
        for line in file:
            parts=line.strip().split(",")

            user_id=parts[0]
            user_name=parts[1]
            user_department=parts[2]

            users[user_id]={
                "name":user_name,
                "department":user_department

            }

    #print(users)

    #open activity
    with open("activity.csv","r") as file:
        next(file)
        for line in file:
            parts=line.strip().split(",")
            user_id=parts[0]
            user_action=parts[1]
            user_duration=parts[2]

            if user_action=="login":
                continue

            if user_id in users:
                if user_id not in stat:

                    stat[user_id]={
                        "count":0,
                        "total":0
                    }

                stat[user_id]["count"]+=1
                stat[user_id]["total"]+=int(user_duration)


    for user_id in stat:
        print(user_id)


        