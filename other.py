from selenium.webdriver.common.by import By

# Returns calendar: Counter -> Date
def countedDays(picker):
    out = {}
    days = picker.find_elements(By.CSS_SELECTOR, "*")
    counter = 0
    for day in days:
        if day.tag_name == "div":
            dt = day.get_attribute("data-date")
            month = int(day.get_attribute("data-month")) + 1
            year = day.get_attribute("data-year")
            counter = counter + 1
            out[counter] = f"{year}-{month}-{dt}"
    return out

# Count pages per month based on counted days (cd)
def countPagesPerMonth(cd):
    monthCounts = { }
    for item in cd:
        strday = cd[item]
        month = strday.split("-")[1]
        if month in monthCounts:
            monthCounts[month] += 1
        else:
            monthCounts[month] = 0
    return monthCounts

# Find month with most pages based on pages per month (ppm)
def detectCurrentMonth(ppm):
    result = None
    for month in ppm:
        if result is None:
            result = month
        if ppm[month] > ppm[result]:
            result = month
    return result

# Find next month following the current one
def detectNextMonth(ppm, currentMonth):
    takeIt = False
    for month in ppm:
        if takeIt:
            return month
        if month == currentMonth:
            takeIt = True
    return None
