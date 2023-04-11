# Step 1
import csv
data = []
with open('/Users/gxy/Downloads/Data.csv', mode='r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    next(fCSV)
    for line in fCSV:
        print(line)
        data.append(line)
# Step 2
yearly_sales = {}
for line in data:
    year = line[0]
    monthly_sales = [int(sales) for sales in line[1:]]
    yearly_sales[year] = sum(monthly_sales)
    print('Total sales in ' f'{year} is: {yearly_sales[year]}\n')
with open('stats.txt', mode='w') as file:
    for year in yearly_sales:
        file.write(f'Total sales in {year} is: {yearly_sales[year]}\n')
# Step 3
import matplotlib.pyplot as plt

x = list(yearly_sales.keys())
y = list(yearly_sales.values())
plt.figure(1)
plt.bar(x, y)
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Vehicle Yearly Sales (2012-2021)')
plt.show()

# Step 4
sales_2021_first_half = sum(int(data[-2][i]) for i in range(1, 7))
sales_2022_first_half = sum(int(data[-1][i]) for i in range(1, 7))
SGR = (sales_2022_first_half - sales_2021_first_half) / sales_2021_first_half
estimated_sales_2022_second_half = [int(data[-2][i]) * (1 + SGR) for i in range(7, 13)]
with open('stats.txt', mode='a') as file:
    file.write(f'Sales Growth Rate (SGR): {SGR}\n')
    print(f'Sales Growth Rate (SGR) is : {SGR}\n')
    months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for month, est_sales in zip(months, estimated_sales_2022_second_half):
        file.write(f'Estimated sales in {month} 2022:{est_sales}\n')
        print(f'Estimated sales in {month} 2022:{est_sales}\n')
# Step 5
x = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y = [int(data[-2][i]) * (1 + SGR) for i in range(7, 13)]
plt.figure(2)
plt.barh(x, y)
plt.title("Estimated Vehicle Sales for the Last Six Months of 2022")
plt.xlabel("Sales")
plt.ylabel("Months")
plt.grid()
plt.show()