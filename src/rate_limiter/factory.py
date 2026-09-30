from .fixed_window import FixedWindowRateLimiter
from .sliding_window import SlidingWindowRateLimiter
from .token_bucket import TokenBucketRateLimiter


def create_rate_limiter(algorithm: str, **kwargs):

    if algorithm == "fixed_window":
        return FixedWindowRateLimiter(**kwargs)

    if algorithm == "sliding_window":
        return SlidingWindowRateLimiter(**kwargs)

    if algorithm == "token_bucket":
        return TokenBucketRateLimiter(**kwargs)

    raise ValueError(f"Unknown rate limiter algorithm: {algorithm}")