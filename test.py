import time
import random
from selenium import webdriver

driver = webdriver.Chrome('.\chromedriver.exe')

videos = [
'https://www.youtube.com/watch?v=B_e7DM8iyUU&ab_channel=Nguy%E1%BB%85nHo%C3%A0ngDuyOffical',
'https://www.youtube.com/watch?v=B_e7DM8iyUU&ab_channel=Nguy%E1%BB%85nHo%C3%A0ngDuyOffical',
'https://www.youtube.com/watch?v=B_e7DM8iyUU&ab_channel=Nguy%E1%BB%85nHo%C3%A0ngDuyOffical',
'https://www.youtube.com/watch?v=B_e7DM8iyUU&ab_channel=Nguy%E1%BB%85nHo%C3%A0ngDuyOffical'
]

sleep_time = 0

for i in range(1000):
    print("Watching for {} time".format(i))
    random_video = random.randint(0,3)
    driver.get(videos[random_video])
    time.sleep(sleep_time) # Let the user actually see something!
    sleep_time = random.randint(50, 60)

time.sleep(5) # Let the user actually see something!
driver.quit()