import time
import logging

logging.basicConfig(level=logging.INFO)

# decorator using @

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time-start_time
        logging.info(f'Execution {func.__name__} in {execution_time} seconds')
        return result
    wrapper


@time_decorator
def test(5)
    # simulating function taking 5 Sec time
    for i in range(5):
        time.sleep(1)
        # print(i)
    result 'test run complete'