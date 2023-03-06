import csv

all_data = []

def curate_data(store_array, csv_reader):
    for row in csv_reader:
        if row[0] == "pink morsel":
            price = float(row[1].replace("$", ""))
            amount = int(row[2])
            date = row[3]
            region = row[4]

            sales = price * amount
            store_array.append([sales, date, region])

for i in range(3):
    with open(f'./data/daily_sales_data_{i}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        curate_data(all_data, csv_reader)

with open(file='./data/curated_data.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['sales', 'date', 'region'])
    csv_writer.writerows(all_data)


