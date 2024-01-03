import asyncio
from xknx import XKNX
from xknx.io import ConnectionConfig, ConnectionType
from xknx.devices import Cover, Sensor, Climate

LOCAL_IP = "127.0.0.1"
GATEWAY_IP = "127.0.0.1"
GATEWAY_PORT = "3671"

LIGHT_THRESHOLD = 200
TEMP_THRESHOLD = 20

async def main():

    connection_config = ConnectionConfig(
        connection_type=ConnectionType.AUTOMATIC,
        local_ip=LOCAL_IP,
        gateway_ip=GATEWAY_IP,
        gateway_port=GATEWAY_PORT,
    )

    xknx = XKNX(connection_config=connection_config)

    async with xknx:

        # Cover device
        cover = Cover(
            xknx,
            name="TestCover",
            group_address_long="1/0/12",
            group_address_short="1/0/14",
            group_address_position_state="1/0/15",
            group_address_angle="1/0/16",
            group_address_angle_state="1/0/17",
        )

        # Light sensor device
        light_sensor = Sensor(
            xknx,
            name="LightSensor",
            group_address_state="1/0/18"
        )

        # Radiator device
        radiator = Climate(
            xknx,
            name="TestRadiator",
            group_address_temperature="1/0/19",
            group_address_target_temperature="1/0/20",
            group_address_setpoint_shift="1/0/21",
            group_address_mode="1/0/22",
        )

        while True:
            await asyncio.sleep(3600) # 1 hour
            await handle_light_sensor(cover, light_sensor, LIGHT_THRESHOLD)
            await handle_room_temperature(radiator, TEMP_THRESHOLD)


async def handle_light_sensor(cover, light_sensor, threshold):
    # Check the light level
    light_level = await light_sensor.read_state()

    # If light level is above threshold, open the cover
    if light_level > threshold:
        await cover.up()
    else:
        await cover.down()


async def handle_room_temperature(radiator, threshold):
    # Check the room temperature
    room_temperature = await radiator.temperature()

    # If temperature is below threshold, increase temperature
    if room_temperature < threshold:
        await radiator.set_target_temperature(22)

asyncio.run(main())
