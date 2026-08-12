import csv

if __name__=="__main__":
    with open("dataset2.csv") as file:
        next(file)
        for line in file:
            print(line)
            parts=line.strip().split(",")
            name = parts[0]
            heigh= parts[1]
            print(name,heigh)
        