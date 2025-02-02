# OBD2 Extracter

This project is to explore the extraction of taking the time series data from a OBD2 sensor in a vehicle

## Quick Start

### Setup Venv
```bash
python3 -m venv venv
source venv/bin/activate
```

### Allowing Sudo
The script needs access to run sudo commands if you are virtualizing a wifi connected OBD-II. Follow these steps if necessary:
Run both of the following: 
```bash
# fetch where chmod / socat commands are stored
which chmod
which socat

# open file for editing
sudo visudo

# add the following line to the bottom
<username> ALL=(ALL) NOPASSWD: <output-from-which-socat>, <output-from-which-chmod>

# e.g.
user ALL=(ALL) NOPASSWD: /usr/bin/socat, /usr/bin/chmod
```


### Run OBD-II Ingestor

```bash
# Connect to the OBDII wifi

# Run:
python3 main.py

# Optionally for more details / flags:
python3 main.py --help
```

## Future Considerations:
- Fetch rpi temp and shutoff if too hot (It's currently winter so not too worried about this)
- Show engine diagnostics codes if they are there
- Storing metric data locally - possibly upload to long term server storage
- Fetch tire pressure. This would involve an rf module and decoder which I don't feel like adding all that extra tech on my dashboard for now

## Drawbacks:
It seems the `OIL_TEMP` is not supported by my obd device and/or car. Tire pressure also isn't possible out of the box.


## Debugging Notes:
If you hit a `AttributeError: module 'numpy' has no attribute 'cumproduct'. Did you mean: 'cumprod'?`. Then try to uninstall numpy and reisntall less then version 2.0:
```bash
pip uninstall numpy
pip install "numpy<2.0"
```