import asyncio
from update_prices import update_all

async def handler(event, context):
    await update_all()

    