hourly_rate = 100  
extra_hour_rate = 15  
overtime_rate = 25  
saturday_bonus = 0.25 
sunday_bonus = 0.5  
hours_worked = []
for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    hours = int(input(f"Hours worked on {day}: "))
    hours_worked.append(hours)
daily_salaries = []
for hours in hours_worked:
    if hours == 0:
        daily_salaries.append(0)
    elif hours == 8:
        daily_salaries.append(hours * hourly_rate)
    else:
        daily_salaries.append(hours * (hourly_rate + (hourly_rate * sunday_bonus)))
total_hours = sum(hours_worked)
extra_hour_salary = sum([(hours - 8) * extra_hour_rate for hours in hours_worked if hours > 8])
overtime_salary = (total_hours - 40) * overtime_rate if total_hours > 40 else 0
weekly_salary = sum(daily_salaries) + extra_hour_salary + overtime_salary
print("Jeevitha's weekly salary: Rs.", int(weekly_salary))