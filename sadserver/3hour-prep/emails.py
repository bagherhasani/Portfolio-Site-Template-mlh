
if __name__=="__main__":
    emails={}

    with open("emails.txt") as file:
        for line in file:
            email=line.strip()
            if "@" in email:
                if email not in emails:
                    emails[email]=1
                else:
                    emails[email]+=1

    max_email=max(emails,key=emails.get)
    print(max_email,emails[max_email])