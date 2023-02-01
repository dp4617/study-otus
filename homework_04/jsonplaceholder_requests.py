"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from typing import List

import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_users() -> List[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:

            users_data = await response.json()
            return users_data


async def get_posts() -> List[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:

            posts_data = await response.json()
            return posts_data