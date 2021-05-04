# cowin-vaccine-slot-script
CoWiN vaccination slot availability automation script which polls CoWIN API and generates notifications on MacOS


## Usage

Edit the `cowin.py` file to configure the following variables:
* district_ids
* numdays
* age
* availability_threshhold
* cooldown_time

Run:

```bash
python3 cowin.py
```

This will poll the CoWIN API to look for available slots with the configured parameters. 
If found, it will generate a MacOS alert with relevant details of the center and session such as: `Date`, `Pincode`, `Price`, `Center Name` and `Available Capacity`
Otherwise, it will keep running and hitting the API after cooldown period.


**Note**: This script uses Mac's osascript to generate notifications. So for non-macos usages, feel free to use other utilities such as `notify-send` & `zenity`