def decorator(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Your request: {args}')
        print(f'Working time of function: {round(end - start, 5)}\n')
        return result
    return wrapper


@decorator
def request_url(url):
    import requests
    response = requests.get(url)
    return response


request_url('https://ya.ru')
request_url('https://google.com')
request_url('http://arno-kovka.com/')
