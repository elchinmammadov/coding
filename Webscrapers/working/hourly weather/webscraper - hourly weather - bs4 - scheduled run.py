# this code runs 'webscraper - hourly weather - bs4.py' script every hour

import time

while True:
    exec(open('/Users/elchi/Dropbox/Coding/Webscrapers/working/webscraper - hourly weather - bs4.py').read())
    time.sleep(3600)

