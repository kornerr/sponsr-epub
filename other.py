from selenium.webdriver.common.by import By

# Returns calendar: Counter -> Date
def countedDays(picker):
    out = {}
    days = picker.find_elements(By.CSS_SELECTOR, "*")
    counter = 0
    for day in days:
        if day.tag_name == "div":
            dt = day.get_attribute("data-date")
            month = day.get_attribute("data-month")
            year = day.get_attribute("data-year")
            counter = counter + 1
            out[counter] = f"{year}-{month}-{dt}"
    return out
