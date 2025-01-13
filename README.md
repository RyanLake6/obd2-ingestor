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

### Allowing sudo commands
The script needs access to run sudo commands if you are virtualizing a wifi connected OBD-II. Follow these steps if necessary:
Run both of the following: `which chmod` and `which socat`
Then `sudo visudo`
and place the following line in the file:
`<username> ALL=(ALL) NOPASSWD: <output-from-which-socat>, <output-from-which-chmod>`
Example:
`user ALL=(ALL) NOPASSWD: /usr/bin/socat, /usr/bin/chmod`


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

## Drawbacks:
It seems the `OIL_TEMP` is not supported by my obd device and/or car. Tire pressure also doesn't possible out of the box. It might be possible if I find the direct PID but I have not been able to get this to work yet.


Debugging Notes:
If you hit a `AttributeError: module 'numpy' has no attribute 'cumproduct'. Did you mean: 'cumprod'?`. Then try to uninstall numpy and reisntall less then version 2.0:
```bash
pip uninstall numpy
pip install "numpy<2.0"
```