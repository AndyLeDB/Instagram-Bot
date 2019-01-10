from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')

    # this function will log us into instagram
    def login(self):
        # instagram homepage
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)

        # this will click on the login button
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        # this will login using a username and password
        user_name_login = driver.find_element_by_xpath("//input[@name='username']")
        user_name_login.clear()
        user_name_login.send_keys(self.username)
        password_login = driver.find_element_by_xpath("//input[@name='password']")
        password_login.clear()
        password_login.send_keys(self.password)
        password_login.send_keys(Keys.RETURN)
        time.sleep(2)
        # "not now" for instagram app pop up
        not_now_app_button = driver.find_element_by_xpath("//a[@class='_3m3RQ _7XMpj']")
        not_now_app_button.click()
        time.sleep(3)
        # "no notification" for instagram desktop popup
        not_now_button = driver.find_element_by_xpath("//button[@tabindex='0']")
        not_now_button.click()
        time.sleep(3)

    # this function opens a new instagram page with a specific hashtag,and goes to the most recent post by clicking right 9x
    def recent_post(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        click_on_picture = driver.find_element_by_xpath("//div[@class='eLAPa']")
        time.sleep(2)
        click_on_picture.click()
        time.sleep(2)
        for i in range(9):
            click_on_right_arrow = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
            click_on_right_arrow.click()
            time.sleep(random.randint(1,3))

    # this function will like, generate a random comment from the list, and follow new posts
    def like_comment_follow(self):
        driver = self.driver
        count_likes = 0
        count_comments = 0
        count_followers = 0
        count_loop = 0
        comments = ['comment1', 'comment2', 'comment3', 'comment 4', 'etc']

        for i in range(9):
            # find the like button and like it
            click_on_like = driver.find_element_by_xpath("//span[@aria-label='Like']")
            click_on_like.click()
            time.sleep(random.randint(3, 6))
            count_likes += 1
            # find the text box and comment
            click_on_comment = driver.find_element_by_xpath("//textarea[@class='Ypffh']")
            ActionChains(driver).move_to_element(click_on_comment).send_keys_to_element(click_on_comment, random.choice(comments)).send_keys(Keys.RETURN).perform()
            time.sleep(random.randint(3, 6))
            count_comments += 1
            # find the follow button and follow
            click_on_follow = driver.find_element_by_xpath("//button[@class='oW_lN _0mzm- sqdOP yWX7d        ']")
            click_on_follow.click()
            count_followers += 1
            time.sleep(random.randint(4, 7))
            # find the right arrow and click on it to move onto the next post
            click_on_right_arrow = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
            click_on_right_arrow.click()
            time.sleep(random.randint(51, 58))
            count_loop += 1
            print(count_loop)
        print('The amount of likes this session is ', count_likes)
        print('The amount of followed accounts this session is ', count_followers)
        print('The amount of comments this sessions is ', count_comments)


# giving arguments the information to login
testing = InstagramBot('username','password')
# calls our function to login
testing.login()

# calling this function will open up a new instagram page given a specific hastag
testing.recent_post('hashtag')

# testing.like_comment_follow(comments[random.ranint(0,5)])
testing.like_comment_follow()
