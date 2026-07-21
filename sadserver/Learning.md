## how to find a file  from root 
sudo find / -name "pg_hba.conf"

## search for something 
grep -R "something"


## compare if 100 files content are identical
md5sum *
diff file1 file2

# reading a file and iterating over
with open("/home/admin/scores.txt","r") as file:
    for line in file:
        print(line.split()[0])