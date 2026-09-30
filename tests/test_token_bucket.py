import time

from src.rate_limiter.token_bucket import TokenBucketRateLimiter


def test_requests_within_capacity():
    limiter = TokenBucketRateLimiter(
        capacity=3,
        refill_rate=1
    )

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True


def test_request_exceeds_capacity():
    limiter = TokenBucketRateLimiter(
        capacity=3,
        refill_rate=1
    )

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False


def test_tokens_refill():
    limiter = TokenBucketRateLimiter(
        capacity=1,
        refill_rate=1
    )

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False

    time.sleep(1.1)

    assert limiter.allow("user1") is True


def test_different_users_have_separate_buckets():
    limiter = TokenBucketRateLimiter(
        capacity=1,
        refill_rate=1
    )

    assert limiter.allow("user1") is True
    assert limiter.allow("user1") is False

    assert limiter.allow("user2") is True