import pytest
from app import unstable_function


def test_timeout_error():
    """
    Kiểm tra xem TimeoutError có thể xảy ra.
    """
    caught = False
    for _ in range(300):
        try:
            unstable_function(10)
        except TimeoutError:
            caught = True
            break
        except Exception:
            continue

    assert caught, "Không phát hiện TimeoutError trong 300 lần chạy"


def test_random_crash():
    """
    Kiểm tra RuntimeError (crash ngẫu nhiên)
    """
    caught = False
    for _ in range(300):
        try:
            unstable_function(10)
        except RuntimeError:
            caught = True
            break
        except Exception:
            continue

    assert caught, "Không phát hiện RuntimeError trong 300 lần chạy"


def test_memory_error():
    """
    Kiểm tra MemoryError.
    Các lỗi khác (TimeoutError, RuntimeError) phải được bỏ qua.
    """
    caught = False
    for _ in range(400):
        try:
            unstable_function(10)
        except MemoryError:
            caught = True
            break
        except Exception:
            continue

    assert caught, "Không phát hiện MemoryError trong 400 lần chạy"


def test_bit_flip_fault():
    """
    Kiểm tra bit flip: giá trị bị thay đổi bất thường (không đúng x*2).
    """
    flip_detected = False

    for _ in range(400):
        try:
            result = unstable_function(10)

            if result != 20:  # giá trị đúng là 20
                flip_detected = True
                break

        except Exception:
            continue  # bỏ qua lỗi để tiếp tục test bit flip

    assert flip_detected, "Không phát hiện lỗi bit-flip trong 400 lần chạy"

def test_recovery():
    result = safe_unstable_function(10)
    assert result == 20 or result == "FAILED"

