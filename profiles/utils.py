def permission_check(user):
    if user.is_authenticated():
        return True
    else:
        return False
