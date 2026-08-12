





if __name__=="__main__":

    users={}
    with open("requests.csv") as file:
        #skip the header
        next(file)

        #parse data
        for line in file:
            parts=line.strip().split(",")
            user_id=parts[0]
            user_activity=parts[1].lstrip("/")
            user_request=int(parts[2])
            #print(user_id,user_activity,user_request)

            #add to users dictionary
            if user_id not in users:

                users[user_id]={
                    "count":0,
                    "failure":0
                }
            else:
                users[user_id]["count"]+=1
                if user_request>=400:
                    users[user_id]["failure"]+=1



    # get the most failture 
    hightest=0
    hightes_id=-1
    for user_id in users:
        if users[user_id]["failure"]>hightest:
            hightest=users[user_id]["failure"]
            hightes_id=user_id
    print(hightes_id)



