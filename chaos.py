# chaos.py
import random
import time
import os

def inject_failure():
    r = random.random()

    if r < 0.15:
        raise RuntimeError("🔥 Lỗi hệ thống được TIÊM bởi chaos.py!")

    elif r < 0.30:
        time.sleep(4)  # mô phỏng treo / timeout lâu

    elif r < 0.45:
        if os.path.exists("important.txt"):
            os.remove("important.txt")
            print("⚠ important.txt đã bị xóa do fault injection!")
