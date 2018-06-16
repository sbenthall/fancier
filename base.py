import configparser
from twitter import *

config = configparser.ConfigParser()
config.read('config.ini')

t = Twitter(
    auth=OAuth(config['OAUTH']['TOKEN'],
               config['OAUTH']['TOKEN_SECRET'],
               config['OAUTH']['CONSUMER_KEY'],
               config['OAUTH']['CONSUMER_SECRET']))
