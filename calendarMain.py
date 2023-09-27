import datetime

def get_first_day_of_week_thing():
    while True:
        choice = input("Enter the first day of the week (Monday or Sunday): ").strip().lower()
        if choice in ['monday', 'sunday']:
            return choice
        else:
            print("Invalid choice. Please enter 'Monday' or 'Sunday'.")

year = int(input("Enter a year: "))
disp_per_row = int(12 / int(input("Months to display in a single row: ")))
first_day_which = get_first_day_of_week_thing()

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

calendar_output = []

for month in range(1, 13):
    final_output = ""
    first_day_of_month = datetime.date(year, month, 1)
    month_name = months[month - 1]

    final_output += f"{month_name} {year}\n"

    if first_day_which == 'monday':
        final_output += "Mo Tu We Th Fr Sa Su\n"
        weekday_offset = (first_day_of_month.weekday() - 1) % 7 
    else:
        final_output += "Su Mo Tu We Th Fr Sa\n"
        weekday_offset = first_day_of_month.weekday()

    final_output += " " * 3 * weekday_offset

    day = 1
    while day <= 31:
        final_output += f"{day:2} "
        day += 1
        weekday_offset += 1

        if weekday_offset == 7:
            final_output += "\n"
            weekday_offset = 0

    final_output += "\n" + "-" * 20 + "\n"
    calendar_output.append(final_output)

print(calendar_output)

for el, item in enumerate(calendar_output):
    if (el + 1) % disp_per_row == 0:
        print(item)
    else:
        print(item, end=' ')
