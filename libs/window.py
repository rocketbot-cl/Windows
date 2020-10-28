from support_windows import only_supported_for


def maximize_window(title):
    """Maximize window
    Maximizes a window by its title
    :parameter title: Title of window
    :type title: string
        :Example:
    >>> maximize_window('Untitled - Notepad')
    Keywords
        window, maximize, title
    Icon
        las la-window-restore
    """
    only_supported_for("Windows")

    import win32con
    import win32gui

    handle = win32gui.FindWindow(None, title)

    if not handle:
        raise Exception(
            'Could not find a window with title "{}"'.format(title)
        )

    win32gui.ShowWindow(handle, win32con.SW_SHOWMAXIMIZED)
    win32gui.SetForegroundWindow(handle)


def restore_window(title):
    """Restore window
    Restore a window by its title
    :parameter title: Title of window
    :type title: string
        :Example:
    >>> restore_window('Untitled - Notepad')
    Keywords
        window, restore, title
    Icon
        las la-window-restore
    """
    only_supported_for("Windows")

    import win32con
    import win32gui

    handle = win32gui.FindWindow(None, title)

    if not handle:
        raise Exception(
            'Could not find a window with title "{}"'.format(title)
        )

    win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(handle)


def minimize_window(title):
    """Minimize window
    Minimizes a window by its title
    :parameter title: Title of window
    :type title: string
        :Example:
    >>> minimize_window(title)
    Keywords
        window, minimize, title
    Icon
        las la-window-restore
    """
    only_supported_for("Windows")

    import win32gui

    handle = win32gui.FindWindow(None, title)

    if not handle:
        raise Exception(
            'Could not find a window with title "{}"'.format(title)
        )

    win32gui.CloseWindow(handle)


def find_window_title(searchterm, partial=True):
    """Find window with specific title
    Find a specific window based on the name, either a perfect match or a partial match.
    :parameter searchterm: Ttile to look for, e.g. 'Calculator' when looking for the Windows calculator
    :type searchterm: string
    :parameter partial: Option to look for titles partially, e.g. 'Edge' will result in finding 'Microsoft Edge' when partial is set to True. Default value is True
    :type pertial: bool, optional
    :return: Window found (True)
        :Example:
    >>> # Make text file
    >>> testfile = make_text_file()
    >>> # Open the file
    >>> open_file(testfile)
    >>> #Find 'Notepad' in window titles
    >>> find_window_title('Notepad')
    'generated_text_file.txt - Notepad'
    Keywords
        windows, user, password, remote desktop, remote, citrix, vnc, remotedesktop
    Icon
        lab la-readme
    """

    import ctypes

    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(
        ctypes.c_bool,
        ctypes.POINTER(ctypes.c_int),
        ctypes.POINTER(ctypes.c_int),
    )
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    if partial:
        for title in titles:
            if searchterm in title:
                return True

    if not partial:
        for title in titles:
            if searchterm == title:
                return True

    else:
        return False


def set_foreground_app(app_name):
    try:
        import win32gui

        def set_window_to_foreground(title):
            import win32gui
            import win32con
            import win32com
            try:
                handle = win32gui.FindWindow(None, title)
                if not handle:
                    raise Exception('Could not find a window with title "{}"'.format(title))

                win32gui.ShowWindow(handle, win32con.SW_NORMAL)
                win32gui.SetForegroundWindow(handle)
            except Exception as ex:
                raise ex

        set_window_to_foreground(app_name)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        print(e)
        raise e


if __name__ == '__main__':
    title = "Mineria de Datos"
    # minimize_window(title)
    # print(find_window_title(title))
    set_foreground_app(title)
