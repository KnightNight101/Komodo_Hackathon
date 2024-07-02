import csv

with open("output_dataframe.csv" , "r") as source: 
    reader = csv.reader(source) 

    with open("GrafanaData.csv", "w") as result: 
        writer = csv.writer(result) 
        for r in reader: 
           
            writer.writerow((r[1], r[2],r[3],r[4],r[5],r[6],r[7]))


#2024-06-02
#2024-07-01