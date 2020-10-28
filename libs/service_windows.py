from support_windows import only_supported_for


def get_service_status(name):
    """Get service status
    Returns the status of a service on the machine
    :parameter name: Name of service
    :type name: string
    :return: Status
        :Example:
    >>> get_service_status('Windows Backup')
    'stopped'
    Keywords
        services, get service status, status
    Icon
        las la-cog
    """
    only_supported_for("Windows")

    import psutil

    for s in psutil.win_service_iter():
        if s.name() == name or s.display_name() == name:
            return s.status()


def start_service(name):
    """Start a service
    Starts a Windows service
    :parameter name: Name of service
    :type name: string
        :Example:
    >>> start_service('Windows Backup')
    Keywords
        services, start a service, start
    Icon
        las la-cog
    """
    only_supported_for("Windows")

    import win32serviceutil

    win32serviceutil.StartService(name)


def stop_service(name):
    """Stop a service
    Stops a Windows service
    :parameter name: Name of service
    :type name: string
        :Example:
    >>> stop_service('Windows Backup')
    Keywords
        services, stop a service, stop
    Icon
        las la-cog
    """
    only_supported_for("Windows")

    import win32serviceutil

    win32serviceutil.StopService(name)


if __name__ == '__main__':
    service_name = "AnyDesk"
    print(get_service_status(service_name))
    stop_service(service_name)
