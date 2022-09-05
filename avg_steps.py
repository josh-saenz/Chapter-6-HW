import csv

infile = open('steps.csv', 'r' )

csvfile = csv.reader(infile, delimiter=',')

outfile = open('avg_steps.csv', 'w')

next(csvfile)
outfile.write('Month, Avg. Steps\n')

JanSum = 0
JanDays = 0
FebSum = 0
FebDays = 0
MarchSum= 0
MarchDays = 0
AprilSum= 0
AprilDays = 0
MaySum = 0
MayDays = 0
JuneSum = 0
JuneDays = 0
JulySum = 0
JulyDays = 0
AugSum = 0
AugDays = 0
SepSum = 0
SepDays = 0
OctSum = 0
OctDays = 0
NovSum = 0
NovDays = 0
DecSum = 0
DecDays = 0
for record in csvfile:
    if int(record[0]) == 1:
        JanSum += int(record[1])
        JanDays += 1
    elif int(record[0]) == 2:
        FebSum += int(record[1])
        FebDays += 1
    elif int(record[0]) == 3:
        MarchSum += int(record[1])
        MarchDays += 1
    elif int(record[0]) == 4:
        AprilSum += int(record[1])
        AprilDays += 1
    elif int(record[0]) == 5:
        MaySum += int(record[1])
        MayDays += 1
    elif int(record[0]) == 6:
        JuneSum += int(record[1])
        JuneDays += 1
    elif int(record[0]) == 7:
        JulySum += int(record[1])
        JulyDays += 1
    elif int(record[0]) == 8:
        AugSum += int(record[1])
        AugDays += 1
    elif int(record[0]) == 9:
        SepSum += int(record[1])
        SepDays += 1   
    elif int(record[0]) == 10:
        OctSum += int(record[1])
        OctDays += 1
    elif int(record[0]) == 11:
        NovSum += int(record[1])
        NovDays += 1
    elif int(record[0]) == 12:
        DecSum += int(record[1])
        DecDays += 1

JanAvg = JanSum/JanDays
FebAvg = FebSum/FebDays
MarchAvg = MarchSum/MarchDays
AprilAvg = AprilSum/AprilDays
MayAvg = MaySum/MayDays
JuneAvg = JuneSum/JuneDays
JulyAvg = JulySum/JulyDays
AugAvg = AugSum/AugDays
SepAvg = SepSum/SepDays
OctAvg = OctSum/OctDays
NovAvg = NovSum/NovDays
DecAvg = DecSum/DecDays

outfile.write('Januray, ' + str(format(JanAvg, '.2f')))
outfile.write('\nFebruary, ' + str(format(FebAvg, '.2f')))
outfile.write('\nMarch, ' + str(format(MarchAvg, '.2f')))
outfile.write('\nApril, ' + str(format(AprilAvg, '.2f')))
outfile.write('\nMay, ' + str(format(MayAvg, '.2f')))
outfile.write('\nJune, ' + str(format(JuneAvg, '.2f')))
outfile.write('\nJuly, '+ str(format(JulyAvg, '.2f')))
outfile.write('\nAugust, '+ str(format(AugAvg, '.2f')))
outfile.write('\nSeptemer, ' + str(format(SepAvg, '.2f')))
outfile.write('\nOctober, ' + str(format(OctAvg, '.2f')))
outfile.write('\nNovember, ' + str(format(NovAvg, '.2f')))
outfile.write('\nDecember, ' + str(format(DecAvg, '.2f')))

outfile.close()
