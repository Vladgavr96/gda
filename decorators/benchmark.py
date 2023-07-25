import time
import requests

def benchmark(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(f'Время выполнения {end - start}')
    return wrapper

@benchmark
def fetch_webpage(url):
    webpage = requests.get(url)

fetch_webpage('https://dzen.ru')
fetch_webpage('https://www.google.com')