from src.rate_limiter.sliding_window import SlidingWindowRateLimiter


def test_requests_within_limit():
    limiter = SlidingWindowRateLimiter(3, 60)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True


def test_request_exceeds_limit():
    limiter = SlidingWindowRateLimiter(3, 60)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False


def test_different_users_have_separate_limits():
    limiter = SlidingWindowRateLimiter(2, 60)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False

    assert limiter.allow("user2") is True


def test_expired_requests_are_removed():
    limiter = SlidingWindowRateLimiter(2, 1)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True

    import time
    time.sleep(1.1)

    assert limiter.allow("user1") is True