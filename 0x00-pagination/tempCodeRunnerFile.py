cache = {}


def cache(a, b):
    if (a, b) in cache:
        return cache[(a, b)]
    result = add(a, b)
    cache[(a, b)] = result


print(add(3, 5))