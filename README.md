# pokitMeter-DMM-App
BLE devices transfer data based on Generic Attribute (GATT) which uses Services and Characteristics concepts. This Windows app implements GATT communication by using a Python library called [Bleak](https://pypi.org/project/bleak/)- which is a GATT client software.

![](/images/multimeter_ui.png)

 ##	GENERAL INFORMATION

1.1	System Overview
Windows based application for pokitMeter for accessing DMM functions: 

* Voltage, Current, Resistance, Diode, Continuity, Temperature
* DMM configurations
   * voltage range
   * current range
   * ohmmeter range
   * temperature scale
* DSO  and Data Logger functions:
   * Under development
* Written in Python

1.2	Core Components
* Python 3.7
* PyQt5
* Bleak

1.3	Platform
* Windows 10
* GUI is created using Qt Designer
* Exe is created using PyInstaller


## GETTING STARTED
* Run the python script 'main_gui.py'
* Run the stand-alone (exe) file 'pokitMeter_DMM'

2.1	Scanning
Once the app is started it will scan automatically and display a wait indicator as shown below:
![](/images/scanning.png)

2.2	Scanned Devices
After scanning, the app will show a list of found devices:
![](/images/scanned_devices.png)

Note that if pokitMeter does not appear on the list, a re-scan can be done by clicking the ‘Scan again’ button.
![](/images/re-scanning.png)
