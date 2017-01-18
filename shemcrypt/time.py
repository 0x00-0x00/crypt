def format_time(t):
    days = 0.0
    hours = 0.0
    minutes = 0.0
    if t > 86400:
        days = (t / 86400)
        hours = (t % 86400) / 3600
        minutes = (t % 3600) / 60
        seconds = ((t % 86400) % 3600) % 60
    elif t > 3600:
        hours = (t / 3600.0)
        minutes = ((t % 3600) / 60)
        seconds = ((t % 3600) % 60)
    elif t > 60:
        minutes = (t / 60)
        seconds = (t % 60)
    else:
        seconds = t

    return "%dd %2.fh %2.fm %2.fs" % (days, hours, minutes, seconds)