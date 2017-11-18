def permission_check(user):
    if user.is_authenticated():
        return user.myuser.permission > 0
    else:
        return False
