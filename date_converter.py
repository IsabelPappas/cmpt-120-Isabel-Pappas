from symbol import yield_arg


def convert(date):
    '''
    Enter date as this format "Month Day, Year"
    
    @Example "September 1, 2010"
    '''
    
    months = [
              "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"
    ]
    
    # ["May", "24", "2022"]
    month, day, year = date.split()
    
    day_number = day[:2]
    
    
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        raise Exception("Invalid date, please enter number 1-31!")
    
    print(month)
    print(day)
    print(year)
    
    formatted_month = month.capitalize()
    
    index = -1
    for index in range(len(months)):
        if months [index].startswith(formatted_month):
            index = i + 1
            break
        
    if index == -1:
        raise Exception("Invalid month! Must be one of", months)
    
    month_number = index    
    if index < 10:
        month_number = "0{0}".format(index)
        
    
    print("Formatted month:", month_number)
    
    
    if not year.isdigit():
        raise Exception("Invalid year format; must be digit!")
    
    print(str(month_number) + "/" + str(day_number) + "/" + str(year))
    
    
    convert("mAy 24, 2022")
    
    