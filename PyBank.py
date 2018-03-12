import os
os.system("clear")
os.chdir(r'C:\Users\marks\OneDrive\Desktop\Python folder')
file=r'C:\Users\marks\OneDrive\Desktop\Python folder\budget_data_2.csv'
import csv
with open(file, "r") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    date=[]
    revenue=[]
    count=0
    total_revenue=0
    for row in csvreader: 
        if row[0]!="Date":
            count=count+1
            date.append(row[0])
            revenue.append(row[1])
            total_revenue=total_revenue+int(row[1])
            average_revenue=total_revenue/count
total_months=len(set(date))
revenue=list(map(int, revenue))
greatest_increase=max(revenue)
greatest_decrease=min(revenue)

print("Financial Analysis")
print(".....................")
print("Total Months:"+ str(total_months))
print("Total Revenue:$"+ str(total_revenue))
print("Average revenue:$"+ str(average_revenue))
with open(file, "r") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    for row in csvreader: 
        if row[1]==str(greatest_increase):
            print("Greatest increase in revenue:$"+str(row[1])+ str(row[0]))
            monthincrease=str(row[0])
        if row[1]==str(greatest_decrease):
            print("Greatest decrease in revenue:$"+str(row[1])+ str(row[0]))
            monthdecrease=str(row[0])
with open("revenue_data.txt", "w") as text:
    text.write("Finanacial Analysis\n")
    text.write("Total Months:"+ str(total_months)+"\n")
    text.write("Total Revenue:$"+ str(total_revenue)+"\n")
    text.write("Average revenue:$"+ str(average_revenue)+"\n")
    text.write("Greatest increase in revenue:$"+ str(greatest_increase)+str(monthincrease)+"\n")
    text.write("Greatest increase in revenue:$"+ str(greatest_decrease)+str(monthdecrease)+"\n")