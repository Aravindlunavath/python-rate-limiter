from src.rate_limiter.fixed_window import FixedWindowRateLimiter


def test_requests_within_limit():
    limiter = FixedWindowRateLimiter(3, 60)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True


def test_request_exceeds_limit():
    limiter = FixedWindowRateLimiter(3, 60)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False


def test_different_users_have_separate_limits():
    limiter = FixedWindowRateLimiter(2, 60)

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False

    assert limiter.allow("user2") is True