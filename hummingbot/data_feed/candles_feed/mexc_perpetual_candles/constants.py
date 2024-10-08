from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit

REST_URL = "https://contract.mexc.com"
HEALTH_CHECK_ENDPOINT = "/api/v1/contract/ping"
CANDLES_ENDPOINT = "/api/v1/contract/kline"

WSS_URL = "wss://contract.mexc.com/edge"

INTERVALS = {
    "1m": "Min1",
    "5m": "Min5",
    "15m": "Min15",
    "30m": "Min30",
    "1h": "Min60",
    "4h": "Hour4",
    "8h": "Hour8",
    "1d": "Day1",
    "1w": "Week1",
    "1M": "Month1"
}

MAX_RESULTS_PER_CANDLESTICK_REST_REQUEST = 2000

RATE_LIMITS = [
    RateLimit(CANDLES_ENDPOINT, limit=20, time_interval=2, linked_limits=[LinkedLimitWeightPair("raw", 1)]),
    RateLimit(HEALTH_CHECK_ENDPOINT, limit=20, time_interval=2, linked_limits=[LinkedLimitWeightPair("raw", 1)])]
