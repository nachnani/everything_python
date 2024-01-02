def summer_discount_decorator(func):
    def wrapper(price):
        # take the value inside the total and return
        func(price)
        return func(price / 2)

    return wrapper


@summer_discount_decorator
def total(price):
    # Let's assume there was some code here which calculated the total amount
    return price


print(total(50))