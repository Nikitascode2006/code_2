def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...
    overtime = hours_worked - 35
    overtime_pay = overtime * 18
    regular_pay = 35 * 12
    total_pay  = regular_pay + overtime_pay  
#print the result
    
    return total_pay

print(calculate_weekly_pay(36))
print(calculate_weekly_pay(40))
print(calculate_weekly_pay(35))
# # Code Example
# overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
# print(overtime_pay)
