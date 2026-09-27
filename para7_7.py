def checker(func):
    def cheacker(*args, **kwargs):
        try:
            result = func(*args, *kwargs)

        except Exception as exc:
            print(f"We have problems {exs}")
        else:
            print(f"No problems. Result - {result }")
    return cheacker
def calculate(expr):
    return eval(expr)


calc = checker(calculate)
calc("2+2")