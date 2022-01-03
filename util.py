def get_tens_minute():
    return datetime.datetime.now().minute // 10


def is_even(n):
    return (n % 2) == 0


def is_tens_minute_even():
    return is_even(get_tens_minute())


def add_hashtags(xs):
    return [f"#{x}" for x in xs]


def get_hashtags():
    return " OR ".join(add_hashtags(read_lines("hashtags.txt")))


def get_evil_accounts():
    return " ".join([f"-from:{x}" for x in read_lines("evil-accounts.txt")])


def read_lines(filename):
    with open(get_absolute_path(filename)) as f:
        return [line.strip() for line in f.readlines()]

    
def read_file(filename):
    with open(get_absolute_path(filename)) as f:
        return f.read().strip()


def write_file(filename, s):
    with open(get_absolute_path(filename), "w") as f:
        return f.write(str(s))


def rewrite_file(filename, func):
    with open(get_absolute_path(filename), "r+") as f:
        s = func(f.read())
        f.seek(0)
        f.write(s)
