"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio



USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def get_users() -> list[dict]:
    async with  aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:
#           print("Status:", response.status)
#           print("Content-type:", response.headers['content-type'])

            data = await response.json()
            return data

async def get_posts() -> list[dict]:
    async with  aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:
#            print("Status:", response.status)
#            print("Content-type:", response.headers['content-type'])

            data = await response.json()
            return data

