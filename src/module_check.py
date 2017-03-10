from sys import exit


def import_error(pkg):
    """
    Prints to the screen an error message and informing which package is missing
    :param pkg:
    :return: void
    """
    print("Error: You need to install the package: {0}".format(pkg))
    return


try:
    import shemutils
except ImportError:
    import_error("shemutils")
    exit(-1)

try:
    import gevent
    from gevent.event import Event
except ImportError:
    import_error("gevent")
    exit(-1)
