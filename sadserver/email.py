
if __name__==__name__:

    emails={}
    with open("email.log") as file:
        for item in file:
            words=item.split()

            for word in words:
                if "@" in word:
                    if word in emails:
                        emails[word]+=1
                    else:
                        emails[word]=1

    biggest = max(emails,key=emails.get)
    print(biggest,emails[biggest])


            
        