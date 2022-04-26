def make_readable(seconds):
    HH = seconds//(60*60)
    seconds = seconds%(60*60)
    MM = seconds//60
    seconds = seconds%60
    SS = seconds
    return f"{HH:02}:{MM:02}:{SS:02}"