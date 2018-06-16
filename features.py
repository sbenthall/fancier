from datetime import datetime

def is_active(user_object,active_days):
    """
    Test to see if user has been active within
    number of days.
    """
    
    if 'status' not in user_object:
        return False
    
    n = datetime.now()
    sdt = datetime.strptime(user_object['status']['created_at'], \
                            '%a %b %d %H:%M:%S +0000 %Y')
    
    delta = n - sdt
    delta_days = delta.total_seconds() / (24 * 60 * 60)
        
    if delta_days > active_days:
        return False
    else:
        return True
