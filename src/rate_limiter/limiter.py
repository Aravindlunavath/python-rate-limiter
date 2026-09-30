from abc import ABC, abstractmethod


class RateLimiter(ABC):

    @abstractmethod
    def allow(self, key: str) -> bool:
        """
        Return True if the request is allowed,
        otherwise return False.
        """
        pass