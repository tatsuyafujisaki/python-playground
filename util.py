def get_tens_minute():
    return datetime.datetime.now().minute // 10


def is_even(n):
    return (n % 2) == 0


def is_tens_minute_even():
    return is_even(get_tens_minute())


def add_hashtags(xs):
    return [f"#{x}" for x in xs]


def join_or(xs):
    return " OR ".join(xs)


def format_unwanted_accounts(accounts):
    return " ".join([f"-from:{account}" for account in accounts])
