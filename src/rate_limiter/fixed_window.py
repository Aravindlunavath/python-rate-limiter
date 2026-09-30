import time
from .limiter import RateLimiter


class FixedWindowRateLimiter(RateLimiter):

    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}

    def allow(self, key: str) -> bool:
        current_time = time.time()

        if key not in self.requests:
            self.requests[key] = {
                "count": 1,
                "window_start": current_time
            }
            return True

        data = self.requests[key]

        if current_time - data["window_start"] >= self.window_seconds:
            data["count"] = 1
            data["window_start"] = current_time
            return True

        if data["count"] < self.max_requests:
            data["count"] += 1
            return True

        return False