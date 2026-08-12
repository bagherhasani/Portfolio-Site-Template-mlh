import yaml
orignial_data={
"name": "Baker Hassani",
"job":"Developer",
"foods":[
    "apple","orange"
],
"language": {
    "perl":"naive",
    "python":"Elite"
}

}


with open("data.yaml","w") as file:
    yaml.dump(orignial_data,file)


with open("data.yaml","r") as file:
    received_data=yaml.load(file,Loader=yaml.FullLoader)