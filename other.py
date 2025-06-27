from selenium.webdriver.common.by import By
from constants import *

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

# Extact page date from HTML source
def pageDate(html):
    lines = html.split("\n")
    isDate = False
    currentDate = None
    for ln in lines:
        # Parse date
        if isDate:
            isDate = False
            lnt = ln.strip()
            parts = lnt.split(" ")
            inverseDt = parts[0]
            dps = inverseDt.split(".")
            currentDate = f"{dps[2]}-{int(dps[1])}-{int(dps[0])}"
            return currentDate
        # Find date marker
        if ARTICLE_DATE_MARKER in ln:
            isDate = True
    return None

