from base import t
import configparser
from features import is_active
from lookup import my_friend_objects
from pprint import pprint as pp
import utils

# Number of days within which a friend has posted
# to be 'active'
active_days = 90

inactive_friend_ids = [fo['id']
                    for fo in my_friend_objects()
                    if not is_active(fo, active_days)]

inactive_friendships = utils.api_chunker(inactive_friend_ids,
                                         t.friendships.lookup,
                                         'user_id',
                                         100)

assymetric_inactive_friendships = [fro
                                   for fro
                                   in inactive_friendships
                                   if 'followed_by'
                                   not in fro['connections']]

pp(assymetric_inactive_friendships)
    
for aif in assymetric_inactive_friendships:
    t.friendships.destroy(user_id=aif['id'])
