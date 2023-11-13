from twitterbot import InternetSpeedTwitterBot
import os

SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"
EMAIL = os.environ["TWITTER_EMAIL"]
PASSWORD = os.environ["TWITTER_PASSWORD"]

tweet_bot = InternetSpeedTwitterBot()
tweet_text = tweet_bot.internet_speed(SPEED_URL)
tweet_bot.tweet(TWITTER_URL, EMAIL, PASSWORD, tweet_text)
