import csv

companies = []
sales = []


with open('output.csv', 'r') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        companies.append(row[0])
        sales.append(row[1:])
        
print(companies)
print(sales)

#with open ....
#    reader = csv.reader("output.csv")
#    skip for the first line
#    for loop:
#        append to companies
#        append sales data to sales # need to convert to int want a list of tuples
        
#monthly sum (zip)

#yearly_sum = {} #make it a dictionary
#for ...

#print monthly sales
#print yearly sales  # .items()
