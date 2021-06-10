from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def instagram_login(browser, username, pw):
    print("Loggin in...")

    accept_cookies_button = browser.find_element_by_xpath("//button[text()='Accept All']")
    accept_cookies_button.click()
    sleep(2)
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(pw)
    sleep(2)

    login_button = browser.find_element_by_css_selector("button[type=submit]")
    login_button.click()
    
    print("Successfully logged in as 'tagesschaasch'")

def get_recent_post(browser):
    url_path = browser.find_element_by_css_selector('div[class="v1Nh3 kIKUG  _bz0w"] > a').get_attribute('href')
    return url_path

def fetch_postcount(browser):
    post_count_span = browser.find_element_by_css_selector('span.-nal3 > span.g47SY')
    new_post_count = post_count_span.get_attribute('innerHTML')
    replaced_post_count = new_post_count.replace(',', '')
    return int(replaced_post_count)

def comment_post(browser):
    comment_input_field = browser.find_element_by_css_selector('textarea[placeholder="Add a comment…"]')
    comment_input_field.click()
    sleep(1)
    actions = ActionChains(browser)
    actions.send_keys('Wichtig und Richtig')
    actions.perform()
    sleep(1)

    comment_submit_button = browser.find_element_by_xpath("//button[text()='Post']")
    comment_submit_button.click()

    browser.get('https://www.instagram.com/tagesschau/')