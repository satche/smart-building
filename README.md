# Smart Building
An academical projet to monitor and manage building facilities.

## Projet overview

This project deals with the development of a smart building software that provides a set of high-level functionalities (end-user functionalities) such as:
1. lower the temperature of a room to a given threshold when it is empty,
2. increase the temperature of a room to a given threshold when it is occupied,
3. close the blinds when the humidity is high,
4. open the blinds at day time, when the luminance is low and the room is occupied,
5. display the status of a given store and/or a given radiator,
6. manually monitor blinds and radiators of the room where the user is,
7. Provide statistics.

These functionalities can be activated automatically or manually. We assume that we are monitoring a building where blinds, valves (radiators), lamps, beacons and multi-sensors
are deployed at a large scale. Multi-sensors provide temperature, light, humidity, and physical presence. Each room of the building has a sensor, a lamp, a blind, a radiator and a beacon (for location).

Two different network protocols will be used:
1. KNX: to monitor blinds and radiators.
2. Z-Wave: to collect measures of temperature, light, humidity, presence, battery level. All these measures are provided by the multi-sensor.

Concretely speaking, the goal of the project is to
1. Set up the IoT infrastructure (perception and network layers)
2. Develop a support layer that supports:
	1. an authentication module (will be designed but not implemented),
	2. a database of all IoT devices managed by the system
	3. a security module to ensure that a given device is used only by “authorized” persons (access rights and location)
	4. any other functions that might be useful/helpful.
3. Develop an interface (end-user layer) that supports the high-level functionalities listed above