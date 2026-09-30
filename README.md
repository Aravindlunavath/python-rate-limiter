# Python Rate Limiter

A simple, extensible, and production-oriented rate limiter for Python applications.

## Features

* Fixed Window rate limiting
* Sliding Window rate limiting
* Token Bucket rate limiting
* Simple Python API
* Extensible architecture
* Automated tests

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd rate-limiter
```

Install the package:

```bash
python -m pip install -e .
```

## Quick Start

```python
from rate_limiter import TokenBucketRateLimiter

limiter = TokenBucketRateLimiter(
    capacity=5,
    refill_rate=1
)

if limiter.allow("user123"):
    print("Request allowed")
else:
    print("Rate limit exceeded")
```

## Algorithms

### Fixed Window

Limits the number of requests within a fixed time interval.

### Sliding Window

Tracks requests within a continuously moving time window for more accurate limiting.

### Token Bucket

Allows controlled bursts while refilling tokens at a configured rate.

## Running Tests

```bash
python -m pytest
```

## Project Structure

```text
rate-limiter/
├── src/
│   └── rate_limiter/
│       ├── __init__.py
│       ├── limiter.py
│       ├── fixed_window.py
│       ├── sliding_window.py
│       ├── token_bucket.py
│       └── factory.py
│
├── tests/
├── examples/
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

## License

MIT License
