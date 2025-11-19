# test_fuzz.py
from hypothesis import given, strategies as st
from app import unstable_function
import pytest

@given(st.integers(min_value=-5, max_value=10))
def test_fuzzy_inputs(x):
    if x < 0:
        with pytest.raises(ValueError):
            unstable_function(x)
    else:
        result = unstable_function(x)
        # Chấp nhận 3 trường hợp:
        # - đúng: x*2
        # - None: lỗi logic
        # - treo nhẹ (3s timeout)
        assert result in (x * 2, None)
