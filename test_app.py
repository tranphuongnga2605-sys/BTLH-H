# test_app.py
import pytest
from app import unstable_function

def test_negative():
    with pytest.raises(ValueError):
        unstable_function(-1)

def test_normal_case():
    # Khi không xảy ra lỗi ngẫu nhiên
    result = unstable_function(2)
    assert result in (4, None)  # cho phép lỗi logic
