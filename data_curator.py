import csv

INPUT_CSV = './data/daily_sales_data_{}.csv'
OUTPUT_CSV = './curated_data.csv'
csv_data = []


def curate_data(store_array, reader):
    for row in reader:
        if row[0] == "pink morsel":
            price = float(row[1].replace("$", ""))
            amount = int(row[2])
            date = row[3]
            region = row[4]

            sales = price * amount
            store_array.append([sales, date, region])


for i in range(3):
    with open(INPUT_CSV.format(i)) as csv_file:
        curate_data(csv_data, csv.reader(csv_file, delimiter=','))

with open(file=OUTPUT_CSV, mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['sales', 'date', 'region'])
    csv_writer.writerows(csv_data)


