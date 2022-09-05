import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


for record in csvfile:
    record[3] = float(record[3])
    record[4] = float(record[4])
    totalpay = record[3] * (1 + record [4])
    print('ID: ', record[0])
    print('Employee Fname: ', record[1])
    print('Employee Lname: ', record[2])
    print('Salary: ',  record[3])
    print('Bonus: ', record[4])
    print('Total Pay: ', round(totalpay,2))

    input()
