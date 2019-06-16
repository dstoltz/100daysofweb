import requests
import bs4
import asyncio
import aiohttp
#from colorama import Fore


async def get_html(episode_number: int) -> str:
    print(f"Getting HTML for episode {episode_number}", flush=True)

    url = f'https://talkpython.fm/{episode_number}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            await resp.raise_for_status()

            return await resp.text()


async def get_title(html: str, episode_number: int) -> str:
    print(f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    await asyncio.sleep(1)
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range())      
    print("Done.")


async def get_title_range():
    # Please keep this range pretty small to not DDoS my site. ;)
    tasks = []
    
    for n in range(150, 160):
        html = tasks.append((n, asyncio.create_task(get_html(n))) )
        await asyncio.sleep(1)
        title = await get_title(html, n)
        await asyncio.sleep(1)
        print(f"Title found: {title}", flush=True)

    for n, t in tasks:
        html = await t
    


if __name__ == '__main__':
    asyncio.run(main())
