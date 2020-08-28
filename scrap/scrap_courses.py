import pandas as pd
import openpyxl
from scrap.scrap_data_cours import *
from time import sleep


def get_courses_data(driver):
    courses = driver.find_elements_by_css_selector(
        'div.course-list--container--3zXPS div.popover--popover--t3rNO.popover--popover-hover--14ngr')
    print('dst: {}'.format(len(courses)))
    writer = pd.ExcelWriter('file.xlsx', engine='openpyxl')
    i = 0
    for cours_number in range(len(courses)):

        try:
            cours = driver.find_element_by_css_selector(
                "div.course-list--container--3zXPS div.popover--popover--t3rNO.popover--popover-hover--14ngr:nth-of-type({})".format(cours_number + 1))
        except:
            continue
        try:
            exist_file = pd.read_excel('file.xlsx')
            exist_data_frame = pd.DataFrame(exist_file)
            new_data = pd.DataFrame(get_data_of_cours(cours))
            data = exist_data_frame.append(new_data)
        except:
            data = pd.DataFrame(get_data_of_cours(cours))

        data.to_excel(writer, sheet_name='none', index=False)
        writer.save()
        i += 1
    print('do: {}'.format(i))
    next_page = driver.find_element_by_css_selector(
        "div.pagination--container--2wc6Z a[data-page='+1']")
    try:
        driver.execute_script("arguments[0].click();", next_page)
    except:
        return False
    sleep(5)
    return True
