import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

outfile = open('customer_country.csv', 'w')

next(csvfile)
count=0
outfile.write('Full Name, Country\n')

for record in csvfile: 
    outfile.write(f' {record[1]} {record[2]},  {record[4]}\n')
    count +=1 

outfile.close()

print(f'Total number of customers: {count}')
