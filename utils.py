import time
import os
import psutil
import gc
from functools import wraps


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:6f} seconds")
        return result
    return wrapper


def measure_time_block():
    class TimeContext:
        def __enter__(self):
            self.start_time = time.time()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end_time = time.time()
            self.execution_time = self.end_time - self.start_time
            print(f"Code block executed in {self.execution_time:6f} seconds")

    return TimeContext()


def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024*1024)


def memory_usage(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Garbage collector
        gc.collect()

        mem_before = get_process_memory()

        result = func(*args, **kwargs)

        gc.collect()

        mem_after = get_process_memory()

        print(f"Function '{func.__name__}' memory usage: {mem_after - mem_before:.2f} MB")
        print(f"Total memory: {mem_after:.2f} MB")

        return result
    return wrapper


def measure_memory_block():
    class MemoryContext:
        def __enter__(self):
            gc.collect()
            self.mem_before = get_process_memory()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            gc.collect()
            self.mem_after = get_process_memory()
            print(f"Code block memory usage: {self.mem_after - self.mem_before:.2f} MB")
            print(f"Total memory: {self.mem_after:.2f} MB")

    return MemoryContext()


def performance_metrics(func):
    """Decorator to measure execution time, memory usage, and CPU usage."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Force garbage collection
        gc.collect()
        
        # Get initial metrics
        process = psutil.Process(os.getpid())
        mem_before = get_process_memory()
        cpu_percent_start = process.cpu_percent(interval=None)
        start_time = time.time()
        
        # Execute function
        result = func(*args, **kwargs)
        
        # Get final metrics
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Force garbage collection again
        gc.collect()
        
        # Calculate metrics
        mem_after = get_process_memory()
        cpu_percent = process.cpu_percent(interval=None) / execution_time
        
        # Print performance report
        print(f"\n--- Performance Report for '{func.__name__}' ---")
        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"Memory usage: {mem_after - mem_before:.2f} MB")
        print(f"CPU usage: {cpu_percent:.2f}%")
        print("-------------------------------------------\n")
        
        return result
    return wrapper