def func_outer(x: int) -> int:
    print(x)
    def func_inner(y: int) -> int:
        return x*y
    return func_inner

print(func_outer(3)(8))