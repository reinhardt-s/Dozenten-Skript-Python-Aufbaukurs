def log_me(func):
    def wrap():
        with open("log.txt", mode="a") as file:
            text = func()
            file.write(f"{text}\n")
        return text

    return wrap


def log_text(message):
    def decorator(func):
        def wrap(*args, **kwargs):
            with open("log.txt", mode="a") as file:
                file.write(f"{message}\n")
            result = func()
            return result
        return wrap
    return decorator


@log_me
def turn_l():
    print("Lenke nach links")
    return "Turn left"


@log_me
def turn_r():
    print("Lenke nach rechts")
    return "Turn right"


@log_text(message="Drive")
def drive():
    print("Fahre.")


print(turn_l())
turn_r()
drive()
