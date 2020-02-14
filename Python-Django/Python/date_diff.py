start_date = input("Enter a start date (dd-mm-yyy): ")
end_date = input("Enter a end date (dd-mm-yyy): ")

start_date = list(start_date.split('-'))
start_date = [int(i) for i in start_date]

end_date = list(end_date.split('-'))
end_date = [int(i) for i in end_date]

date_diff, month_diff, year_diff = 0, 0, 0

if start_date[0] > end_date[0]:
    date_diff = start_date[0] - end_date[0]
else:
    date_diff = end_date[0] - start_date[0]

if start_date[1] > end_date[1]:
    month_diff = start_date[1] - end_date[1]
else:
    month_diff = end_date[1] - start_date[1]

if start_date[2] > end_date[2]:
    year_diff = start_date[2] - end_date[2]
else:
    year_diff = end_date[2] - start_date[2]

days = date_diff + month_diff * 30 + year_diff * 12 * 30
print("Number of days: ", days)