def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()")
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print("hello {}!")

say("1")