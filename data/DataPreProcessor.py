import csv
import numpy as np
from datetime import datetime, timedelta

def ugly_pre_processing():
    m = {}
    with open('measurement.csv', newline='') as csvfile:
        csvReader = csv.reader(csvfile)

        i = -1
        for row in csvReader:
            i += 1
            if i == 0:
                continue
            d = datetime.strptime(row[0], '%Y-%m-%d')
            d = d - timedelta(days=1)
            m[d.strftime('%Y-%m-%d')] = float(row[1])


    with open('nutrition_summary.csv', newline='') as csvfile:
        csvReader = csv.reader(csvfile)
        dict_data = []
        average_day_data = np.zeros(18)
        csv_columns = []
        act_csv_columns = []
        last_date = ''
        i = -1
        c = 0
        for row in csvReader:
            i += 1
            if i == 0:
                csv_columns = row
                act_csv_columns = row[3:-1]
                act_csv_columns.insert(0, "date")
                act_csv_columns.append("weight")
                continue

            row = np.array(row)


            if last_date == '' or last_date == row[0]:
                c += 1
                average_day_data[:17] = average_day_data[:17] + row[3:-1].astype(float)

            else: 
                average_day_data = average_day_data / c
                day = {"date" : last_date, "weight": 0}
                for i, x in enumerate(average_day_data[:17]):
                    day[csv_columns[i+3]] = x
                c = 1
                dict_data.append(day)
                average_day_data = row[3:-1].astype(float)

            last_date = row[0]

        last_weight = 0
        for row in dict_data[::-1]:
            date = row["date"]
            if date in m:
                row["weight"] = m[date]
                last_weight = m[date]
            else:
                row["weight"] = last_weight + np.random.uniform(-2,0,2)[0]


        csv_file = "nutrition_summary_day_average.csv"
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=act_csv_columns)
                writer.writeheader()
                for data in dict_data[:-1]:
                    writer.writerow(data)
        except IOError:
            print("I/O error") 

        


if __name__ == "__main__":
    ugly_pre_processing()