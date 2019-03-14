import csv
import sys

infile = open(sys.argv[1], "r", encoding='cp437')
outfile = open(sys.argv[2], "w")
lines = csv.reader(infile)
writer = csv.writer(outfile)
for line in lines:
    rowOk = True
    for column in line:
        if not column.isdigit():
            rowOk = False
    if rowOk:
        writer.writerow(line)


infile.close()
outfile.close()
                    
