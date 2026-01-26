import asyncio
import os, sys
from pathlib import Path


parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir)

from update_prices import update_all


async def handler(event, context):
    await update_all()

    