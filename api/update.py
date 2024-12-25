from kupi import update_prices

async def handler(event, context):
    await update_prices()
    return {"status": "Update completed"}