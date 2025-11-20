import random
import time

def unstable_function(x):
    if x < 0:
        raise ValueError("Input âm không hợp lệ")

    if random.random() < 0.10:
        time.sleep(2)
        raise TimeoutError("Timeout xảy ra")

    if random.random() < 0.05:
        raise RuntimeError("Crash ngẫu nhiên")

    if random.random() < 0.05:
        leak = [0] * 5_000_000
        del leak
        raise MemoryError("Giả lập Memory Leak")

    if random.random() < 0.10:
        time.sleep(0.5)

    if random.random() < 0.05:
        x = x ^ 1

    return x * 2
def safe_unstable_function(x, retries=3):
    for i in range(retries):
        try:
            return unstable_function(x)
        except (TimeoutError, RuntimeError) as e:
            print(f"Lỗi xảy ra, thử lại lần {i+1}: {e}")
    return "FAILED"

