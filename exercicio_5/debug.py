def soma(value):
    return value + 2


def mult(value):
    return value * 2


def div(value):
    return value / 2


def error(err):
    print(err)
    exit(1)


def calc(value):
    try:
        value = int(value)
        import ipdb; ipdb.set_trace()
    except ValueError as err:
        return error(err)

    if value % 2:
        return soma(value)
    if value % 3:
        return mult(value)
    if value % 5:
        return div(value)

    return 0


print(calc("50"))
print(calc("abc"))
