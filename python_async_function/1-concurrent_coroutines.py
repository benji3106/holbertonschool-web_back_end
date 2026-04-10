#!/usr/bin/env python3
"""Module for concurrent coroutines."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    
    return results
