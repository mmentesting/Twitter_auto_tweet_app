from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def internet_speed(self, speed_url):
        self.driver.get(speed_url)
        sleep(2)
        cookies = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        cookies.click()
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        sleep(45)
        speed_result = self.driver.find_elements(By.CSS_SELECTOR, ".result-container-data .result-data span")
        self.up = round(float(speed_result[0].text))
        self.down = round(float(speed_result[1].text))
        sleep(2)
        return f"Internet speed test (Mbps): download: {self.up}, upload: {self.down}!"

    def tweet(self, twitter_url, user_email, user_password, user_tweet):
        self.driver.get(twitter_url)
        sleep(5)
        email = self.driver.find_element(By.CSS_SELECTOR, "input[autocomplete='username']")
        email.send_keys(user_email, Keys.ENTER)
        sleep(3)
        try:
            verification = self.driver.find_element(By.CSS_SELECTOR, "input[autocorrect='off']")
        except NoSuchElementException:
            pass
        else:
            verification.send_keys("####", Keys.ENTER)
        sleep(3)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(user_password, Keys.ENTER)
        sleep(3)
        tweet = self.driver.find_element(By.CSS_SELECTOR, ".DraftEditor-root div[aria-label='Tweet text']")
        tweet.send_keys(user_tweet)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")
        # tweet_button.click()
        sleep(3)
        self.driver.quit()
