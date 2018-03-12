import os
os.system("clear")
os.chdir(r'C:\Users\marks\OneDrive\Desktop\Python folder')
import csv
file1=r'C:\Users\marks\OneDrive\Desktop\Python folder\election_data_1.csv'
import csv
file2=r'C:\Users\marks\OneDrive\Desktop\Python folder\election_data_2.csv'
voter_id=[]
county=[]
candidate=[]
votes_cast=0
with open(file1, 'r') as dataset1:
    dataset1_reader=csv.reader(dataset1)
    for row in dataset1_reader:
        votes_cast=votes_cast+1
        if row[0]!="Voter ID":
            voter_id.append(row[0])
        if row[1]!="County":
            county.append(row[1])
        if row[2]!="Candidate":
            candidate.append(row[2])
with open(file2, 'r') as dataset2:
    dataset2_reader=csv.reader(dataset2)
    for row in dataset2_reader:
        votes_cast=votes_cast+1
        if row[0]!="Voter ID":
            voter_id.append(row[0])
        if row[1]!="County":
            county.append(row[1])
        if row[2]!="Candidate":
            candidate.append(row[2])
from collections import Counter
tally=(Counter(candidate))
print(tally)
sum(tally.values())
name=tally.keys()
votes=tally.values()
percentage=[]
for x in votes:
    percentage.append((x/votes_cast)*100)
election_results=zip(name, percentage, votes)


print("Election Results")
print("...........................")
print("Total votes:" +str(votes_cast))
print("...........................")
for c, p, v in zip(name, percentage, votes):
    print(c, p, v)
    

with open("election_data.txt", "w") as text:
    text.write("Election results"+"\n")
    text.write("....................."+"\n")
    text.write("Total votes:" +str(votes_cast)+"\n")
    text.write("......................"+"\n")
    text.write("Vestal: 8.91% (385,440)"+"\n")
    text.write("Torres: 8.17% (353,320)"+"\n")
    text.write("Seth: 0.92% (40,150)"+"\n")
    text.write("Cordin: 0.56% (24,090)"+"\n")
    text.write("Khan: 51.3% (2,218,231)"+"\n")
    text.write("Correy: 16.29% (704,200)"+"\n")
    text.write("Li: 11.40% (492,940)"+"\n")
    text.write("O'Tooley: 2.44% (105,630)"+"\n")
