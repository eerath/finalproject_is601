# app/auth/redis.py
from redis.asyncio import Redis
from app.core.config import get_settings

settings = get_settings()

redis_client: Redis | None = None

async def get_redis() -> Redis:
    global redis_client
    if redis_client is None:
        redis_client = Redis.from_url(settings.REDIS_URL or "redis://localhost")
    return redis_client

async def add_to_blacklist(jti: str, exp: int):
    """Add a token's JTI to the blacklist"""
    redis = await get_redis()
    await redis.set(f"blacklist:{jti}", "1", ex=exp)

async def is_blacklisted(jti: str) -> bool:
    """Check if a token's JTI is blacklisted"""
    redis = await get_redis()
    return await redis.exists(f"blacklist:{jti}")