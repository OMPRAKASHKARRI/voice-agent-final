import time

def track(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} latency: {(end-start)*1000:.2f} ms")

        return result
    return wrapper