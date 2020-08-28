
def is_number(string):
    if string.count(',') > 0:
        string = string[:string.index(','):] + \
            '.' + string[string.index(',')+1:]
    elif not string.count('.') > 0:
        return
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_data_of_cours(driver):
    def find_element(selector):
        return driver.find_element_by_css_selector(selector).text

    book = {}
    title = find_element(
        'div.udlite-focus-visible-target.udlite-heading-md.course-card--course-title--2f7tE')
    link = driver.find_element_by_css_selector(
        'a.udlite-custom-focus-visible.course-card-link--link--3uQEZ')
    try:
        price = find_element(
            "div[data-purpose='course-price-text'] span:nth-of-type(2)")
    except:
        price = 'error'
    try:
        old_price = find_element(
            "div[data-purpose='course-old-price-text'] s")
    except:
        old_price = '-'
    author = find_element(
        'div.udlite-text-xs.course-card--instructor-list--lIA4f')
    try:
        rate = find_element(
            'span.udlite-heading-sm.star-rating--rating-number--3lVe8')
    except:
        rate = '-'
    hours = find_element('span.course-card--row--1OMjg')

    hours = [el for el in hours.split() if is_number(el) or el.isnumeric()]

    book['title'] = [title]
    book['price'] = [price]
    book['old_price'] = [old_price]
    book['author'] = [author]
    book['rate'] = [rate]
    book['hours'] = hours
    book['link'] = [link.get_attribute('href')]
    # print(book)

    return book
