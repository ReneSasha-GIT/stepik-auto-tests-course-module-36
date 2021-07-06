import time

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_exist(browser):
    browser.get(url)
    #time.sleep(30)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "Add to basket button doesn't exist"
