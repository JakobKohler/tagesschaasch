from time import sleep, time
from selenium import webdriver
import configparser
import sched

from functions import *

cfg = configparser.ConfigParser()
cfg.read('credentials.cfg')

event_scheduler = sched.scheduler(time, sleep)

username = cfg.get('KEYS', 'instagram_username', raw='')
pw = cfg.get('KEYS', 'instagram_password', raw='')

browser = webdriver.Firefox()

browser.get('https://www.instagram.com')

sleep(1)

instagram_login(browser, username, pw)

sleep(3)

browser.get('https://www.instagram.com/tagesschau/')

sleep(1)

# initial postcount fetch
current_post_count = fetch_postcount(browser)

def refresh_loop():
    global current_post_count
    new_post_count = fetch_postcount(browser)
    
    if new_post_count > current_post_count: # repace with >
        post_url = get_recent_post(browser)
        sleep(1)
        browser.get(post_url)
        sleep(3)
        comment_post(browser)
        current_post_count = new_post_count        

    event_scheduler.enter(3, 1, refresh_loop)

event_scheduler.enter(3, 1, refresh_loop)
event_scheduler.run()
