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
