from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def goto_category(driver):
    sleep(1)
    category = driver.find_element_by_css_selector(
        'label.udlite-btn.udlite-btn-large.udlite-btn-ghost.udlite-heading-md.js-header-button.header--dropdown-button--1BviY').click()
    category_elements = driver.find_elements_by_css_selector(
        'a.udlite-btn.udlite-btn-large.udlite-btn-ghost.udlite-text-sm.list-menu--item--1crtM.udlite-block-list-item.udlite-block-list-item-small.udlite-block-list-item-neutral')
    category_in = 'Programowanie'  # input()
    for element in category_elements:
        if element.text == category_in:
            element.click()
            break
    sleep(2)
    return
