# Report: smart building

_Thomas Robert, Emile Farine_
**11.01.2024**

[TOC]

## Introduction

The present report is the result of a project conducted in the context of the course _Internet of Things_ (IoT) at MSE formation, HES-SO. The goal of the project was to design and implement a smart building system, using the tools and techniques presented during the course. The goal is to be able to control IoT devices such as blinds, radiators, and lights and provide a user interface to overview their states.

The objectives can be summarized in three steps:

1. Set up the IoT infrastructure
2. Develop a support layer
3. Provide a front-end interface for the end-user

## Implementation

One real IoT device is used for this experiment: a Z-Wave multi-sensor. This device provides temperature, light, humidity, and physical presence. A Raspberry Pi is used as a gateway.

A KNX network is available with the [knxd](https://github.com/knxd/knxd) daemon. Since we don't have the phyiscal infrastructure to manipulate devices suchs as blinds and radiators, we add a [simulator-knx](https://github.com/isisdaude/simulator-knx). A python script will be used to change the state of the devices in the simulator and send the data to the network: we use [xknx](https://github.com/XKNX/xknx) as a library to simplify the commands.

![Screenshot of the simulator](report-assets/simulator-knx.png)

## Results

- Presentation of findings using figures, tables or screenshots
- Raw data may be included in appendices

## Conclusion

- Summary of key findings
- Implications of the results
- Recommendations.
