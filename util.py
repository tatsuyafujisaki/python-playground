def get_tens_minute():
    return datetime.datetime.now().minute // 10


def is_even(n):
    return (n % 2) == 0


def is_tens_minute_even():
    return is_even(get_tens_minute())


def rewrite_file(filename, func):
    with open(get_absolute_path(filename), "r+") as f:
        s = func(f.read())
        f.seek(0)
        f.write(s)
