def get_absolute_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def read_lines_as_single_line(filename):
    return " ".join(read_lines(filename))


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


#
# Twitter
#

def read_hashtags():
    with open(get_absolute_path("hashtags.txt")) as f:
        return " OR ".join(["#" + line.strip() for line in f.readlines()])
