import os
winter_files=os.listdir("Data/Winter")
summer_files=os.listdir("Data/Summer")
for i in range(len(summer_files)):
    summer_files[i]=summer_files[i].replace(".csv","")
for i in range(len(winter_files)):
    winter_files[i]=winter_files[i].replace(".csv","")
print(winter_files)
print(summer_files)
with open("olympic.txt","w") as f:
    for file in summer_files:
        f.write(file+"\n")
    for file in winter_files:
        f.write(file+"\n")
f.close()