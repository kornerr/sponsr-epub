from selenium.webdriver.common.by import By
from constants import *
import re

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

def generateNavPoints(dates):
    i = 0
    items = ""
    for dt in dates:
        i += 1
        item = TEMPLATE_TOC_NAV_POINT\
            .replace("%ID%", dt)\
            .replace("%ORDER%", str(i))\
            .replace("%TITLE%", dt)
        items += item
    return items

def lineToDate(ln):
    lnt = ln.strip()
    parts = lnt.split(" ")
    inverseDt = parts[0]
    dps = inverseDt.split(".")
    return f"{dps[2]}-{int(dps[1])}-{int(dps[0])}"

# Find next article id
def nextArticleId(cd, currentDate):
    for id in cd:
        dt = cd[id]
        if dt == currentDate:
            return int(id) + 1
    return None

# Extact page date from HTML source
def pageDate(html):
    lines = html.split("\n")
    isDate = False
    currentDate = None
    for ln in lines:
        # Parse date
        if isDate:
            return lineToDate(ln)
        # Find date marker
        if ARTICLE_DATE_MARKER in ln:
            isDate = True
    return None

# Extract list of dates of articles
def parseArticleDates(lines):
    dts = []
    for ln in lines:
        lnt = ln.strip()
        if lnt.startswith(ARTICLE_PREFIX_DATE):
            prefixLen = len(ARTICLE_PREFIX_DATE)
            dt = lnt[prefixLen:]
            dts.append(dt)
    return dts

# Extract dictonary of articles: "Date/Title" -> Text
def parseArticles(lines):
    d = {}
    currentDate = None
    currentTitle = None
    isDate = False
    isExpectingContents = False
    for ln in lines:
        # Date
        if isDate:
            isDate = False
            currentDate = lineToDate(ln)

        # Title
        if ARTICLE_DATE_MARKER in ln:
            isDate = True
        # Look for a title
        # Example: <a href="/marahovsky/654/Tushenka_i_svoboda_laifhak_ot_geniya/">Тушёнка и свобода: лайфхак от гения</a>
        rtitle = re.search("<a href=\"\/.*\/\d*\/.*>(.*)</a>", ln)
        if rtitle:
            currentTitle = rtitle.group(1)

        # Contents
        if (
            isExpectingContents and
            ARTICLE_TEXT_UNICODE_MARKER1 in ln
        ):
            text = ln.strip()\
                .replace(ARTICLE_TEXT_UNICODE_MARKER1, "")\
                .replace(ARTICLE_TEXT_UNICODE_MARKER2, "")\
                .replace(ARTICLE_TEXT_PBRP, "")
            # Add dictionary item
            key = f"{currentDate}/{currentTitle}"
            d[key] = text

        if (
            isExpectingContents and
            ARTICLE_TEXT_END_MARKER in ln
        ):
            isExpectingContents = False
        if ARTICLE_TEXT_START_MARKER in ln:
            isExpectingContents = True

    return d

# Read file and return it as a list of strings
def readFileLines(fileName):
    lines = []
    with open(fileName) as file:
        lines = file.readlines()
    return lines

# Accept list of strings and save it
def writeFileLines(fileName, lines):
    with open(fileName, "w") as file:
        file.write("\n".join(lines))
