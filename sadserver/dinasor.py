import math


def calculate_speed(leg_length, stride_length):
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)

if __name__=="__main__":

    list_dinasor1={}
    with open("dataset1.csv") as file:
    # skip the header
        next(file)


        for line in file:
            parts=line.strip().split(",")
            name=parts[0]
            leg_length=parts[1]
            diet=parts[2]

            list_dinasor1[name]=float(leg_length)

    print(list_dinasor1)

    speeds={}
    print("part2------------------------------------")
    with open("dataset2.csv") as file:
        next(file)

        for line in file:
        
            parts=line.strip().split(",")
            name=parts[0]
            stride_length=float(parts[1])
            stance=parts[2]


            if name in list_dinasor1 and stance=="bipedal":
                leg_length=list_dinasor1[name]
                speed=calculate_speed(leg_length,stride_length)
                speeds[name]=speed


    for name in sorted(speeds,key=speeds.get,reverse=True):
        print(name)