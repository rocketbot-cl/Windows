import platform


def only_supported_for(*args):
    """
    Utility function for checking platform support
    Example usage:
    only_supported_for("Windows", "Linux")
    """

    if platform.system() not in args:
        raise NotImplementedError(
            "This activity is currently only supported for {}.".format(
                ", ".join(args)
            )
        )


def get_username():
    """Get Windows username
    Get current logged in user's username
    :return: Username
        :Example:
    >>> get_username()
    'Automagica'
    Keywords
        windows, login, logged in, lockscreen, user, password, account, lock, locked, freeze, hibernate, sleep
    Icon
        las la-user
    """
    only_supported_for("Windows")

    import getpass

    return getpass.getuser()


def set_user_password(username, password):
    """Set Windows password
    Sets the password for a Windows user.
    :parameter username: Username
    :type username: string
    :parameter password: New password
    :type password: string
        :Example:
    >>> set_user_password('SampleUsername', 'SamplePassword')
    Keywords
        windows, user, password, account
    Icon
        las la-passport
    """
    only_supported_for("Windows")

    from win32com import adsi

    user = adsi.ADsGetObject("WinNT://localhost/%s,user" % username)
    user.SetPassword(password)


def is_logged_in():
    """Check if Windows logged in
    Checks if the current user is logged in and not on the lockscreen. Most automations do not work properly when the desktop is locked.
    :return: True if the user is logged in, False if not
        :Example:
    >>> is_logged_in()
    True
    Keywords
        windows, login, logged in, lockscreen, user, password, account, lock, freeze, hibernate, sleep
    Icon
        lar la-user
    """
    only_supported_for("Windows")

    import subprocess  # nosec

    output = subprocess.check_output("TASKLIST")

    if "LogonUI.exe" in str(output):
        return False
    else:
        return True


if __name__ == '__main__':
    print("Hello World!")
    # set_user_password(get_username(),"nicolas14") Error de win32
