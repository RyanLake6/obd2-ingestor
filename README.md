# OBD2 Extracter

This project is to explore the extraction of taking the time series data from a OBD2 sensor in a vehicle

## Setup

### Helper scripts to find obd2 connection

All obd2 sensors are different ips and ports and often needs some debugging to find how to connect to yours. Make sure to do these tests with your car in at least accessory mode

### Setup Venv:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Running the gui
- Connect to the OBDII wifi
- Run: `python3 main.py`

## TODO
- make sudo for the virtualization not take in a user defined password
- Make a requirements and auto pip install setup script
- pass in the obd2 client to the dash app
    - set up so that there's a default ui then maybe a way to customize?
    - maybe just make a json that gets pulled in and then comment out other guages / other stuff

## Planned guages:
- tire pressure
- engine temp
- oil temp
- voltage
- engine error codes
- RPM / speed?