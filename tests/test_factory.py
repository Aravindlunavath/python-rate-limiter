from src.rate_limiter.factory import create_rate_limiter
from src.rate_limiter.fixed_window import FixedWindowRateLimiter
from src.rate_limiter.sliding_window import SlidingWindowRateLimiter
from src.rate_limiter.token_bucket import TokenBucketRateLimiter


def test_create_fixed_window():
    limiter = create_rate_limiter(
        "fixed_window",
        max_requests=5,
        window_seconds=60
    )

    assert isinstance(limiter, FixedWindowRateLimiter)


def test_create_sliding_window():
    limiter = create_rate_limiter(
        "sliding_window",
        max_requests=5,
        window_seconds=60
    )

    assert isinstance(limiter, SlidingWindowRateLimiter)


def test_create_token_bucket():
    limiter = create_rate_limiter(
        "token_bucket",
        capacity=5,
        refill_rate=1
    )

    assert isinstance(limiter, TokenBucketRateLimiter)


def test_unknown_algorithm():
    try:
        create_rate_limiter("unknown")
        assert False
    except ValueError:
        assert True