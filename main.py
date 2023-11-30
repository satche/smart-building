"""Example for switching a light on and off."""
import asyncio

from xknx import XKNX
from xknx.devices import Light


async def main():
    """Connect to KNX/IP bus, switch on light, wait 2 seconds and switch it off again."""

    xknx = XKNX()

    async with xknx:
        light = Light(xknx,
                      name='LED',
                      group_address_switch='0/0/1')
        await light.set_on()
        await asyncio.sleep(2)
        await light.set_off()

asyncio.run(main())
