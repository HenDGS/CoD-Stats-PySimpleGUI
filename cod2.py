import asyncio

import callofduty
from callofduty import Mode, Platform, Title


async def main():
    client = await callofduty.Login()

    results = await client.SearchPlayers(Platform.Activision, "Captain Price", limit=3)
    for player in results:
        print(f"{player.username} ({player.platform.name})")

    me = results[1]
    profile = await me.profile(Title.ModernWarfare, Mode.Multiplayer)

    level = profile["level"]
    kd = profile["lifetime"]["all"]["properties"]["kdRatio"]
    wl = profile["lifetime"]["all"]["properties"]["wlRatio"]

    print(f"\n{me.username} ({me.platform.name})")
    print(f"Level: {level}, K/D Ratio: {kd}, W/L Ratio: {wl}")

asyncio.get_event_loop().run_until_complete(main())
