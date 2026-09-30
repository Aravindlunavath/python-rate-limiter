import time
from collections import defaultdict, deque

from .limiter import RateLimiter


class SlidingWindowRateLimiter(RateLimiter):

    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)

    def allow(self, key: str) -> bool:
        current_time = time.time()
        request_times = self.requests[key]

        while request_times and current_time - request_times[0] >= self.window_seconds:
            request_times.popleft()

        if len(request_times) < self.max_requests:
            request_times.append(current_time)
            return True

        return False