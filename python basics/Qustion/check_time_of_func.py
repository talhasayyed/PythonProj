from typing import Callable 
import time

def time_function(func: Callable [[int], int], n: int) -> None:
    start_time: float = time.perf_counter()
    result: int = func(n)
    end_time: float = time.perf_counter()
    # Print information
    print(f'{func.___name__}({n})={result}')
    print(f'Total time: {end_time - start_time:.4f}s')