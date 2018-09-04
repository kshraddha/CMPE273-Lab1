import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, 'https://webhook.site/cbd99238-0b0d-4515-83a3-54a8d2630737')
    futures = []
    for i in range(3):
        futures.insert(i, future)

    for res in await asyncio.gather(*futures):
        print(res.headers['Date'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())