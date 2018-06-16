from base import t
import configparser
import twitter.follow as follow
import utils

config = configparser.ConfigParser()
config.read('config.ini')

def my_friend_objects():
    """
    Returns an iterator over objects for all my friends.
    """
    # List everyone I follow
    my_friend_ids = follow.follow(t,
                                  config['PARAMETERS']['MY_SCREENNAME'],
                                  followers=False)

    return utils.api_chunker(my_friend_ids,
                             t.users.lookup,
                             'user_id',
                             100)
