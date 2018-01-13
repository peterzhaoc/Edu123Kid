def permission_check(user):
    if user.is_authenticated():
        return True
    else:
        return False

def mentor_permission_check(user):
    if user.is_authenticated():
        if user.userprofile.type == 1:
            return True
        else:
            return False
    else:
        return False
