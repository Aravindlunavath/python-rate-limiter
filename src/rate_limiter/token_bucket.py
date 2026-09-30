import time
from .limiter import RateLimiter


class TokenBucketRateLimiter(RateLimiter):

    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets = {}

    def allow(self, key: str) -> bool:
        current_time = time.time()

        if key not in self.buckets:
            self.buckets[key] = {
                "tokens": self.capacity,
                "last_refill": current_time
            }

        bucket = self.buckets[key]

        elapsed_time = current_time - bucket["last_refill"]

        new_tokens = elapsed_time * self.refill_rate

        bucket["tokens"] = min(
            self.capacity,
            bucket["tokens"] + new_tokens
        )

        bucket["last_refill"] = current_time

        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True

        return False