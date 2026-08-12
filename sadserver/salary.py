
if __name__=="__main__":
    #read employees
    employees={}
    with open("employees.csv") as file:
        #skip the header
        next(file)
        for line in file:
            parts=line.strip().split(",")
            id=parts[0]
            name=parts[1]
            employees[id]=name


    #read salary
    with open("salary.csv") as file:
        next(file)
        for line in file:
            parts=line.strip().split(",")
            id=parts[0]
            salary=parts[1]

            if id in employees:
                print(employees[id],salary)

    

