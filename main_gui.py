# -*- coding: utf-8 -*-

# Import generic libraries
import time
import sys
import struct

# Import BLE and concurrency library
import asyncio
import bleak
from bleak import *
from bleak import discover, BleakClient

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint, QThread, pyqtSignal

# Import other UI components
from no_device import NoDevice
from invalid_device import InvalidDevice
from scanned_devices import ScanGui
from scanning_indicator import ScanIndicator
from connect_indicator import ConnectIndicator
from configure_settings import ConfigureSettings
from confirm_switch import ConfirmSwitch
from confirm_exit import ConfirmExit


# Import main UI file created in Qt-designer
from ui.main_ui import Ui_MainWindow

class MainGui(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainGui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI customization
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(":/images/pokit_logo.png"))
        self.center()

        # Initialized variables
        self.devices = {}
        self.current_device = ''

        # Default config of the MM Service
        self.mode = 1        # default to voltmeter
        self.range = 255     # default to autorange
        self.interval = 200  # 200ms update interval

        # UUID for Manufacturer's information
        self.man_uuid = '00002a29-0000-1000-8000-00805f9b34fb'
        self.man_id = 'Ingenuity Design'

        # Set UUID for reading and writing characteristics
        self.mm_service = 'e7481d2f-5781-442e-bb9a-fd4e3441dadc'
        self.write_uuid = '53dc9a7a-bc19-4280-b76b-002d0e23b078'
        self.read_uuid  = '047d3559-8bee-423a-b229-4417fa603b90'
        self.write_data = 0
        self.read_data = 0

        # Set default range functions
        self.volt_range = 'Auto range'
        self.amp_range = 'Auto range'
        self.ohm_range = 'Auto range'
        self.temp_deg = 'Celsius'
        self.func = []

        # Create range look-up
        self.dmm_volt_range = {'0mV - 300mV': 0,
                               '300mV - 2V': 1,
                               '2V - 6V': 2,
                               '6V - 12V': 3,
                               '12V - 30V':4,
                               '30V - 60V': 5,
                               'Auto range': 255 }

        self.dmm_amp_range = { '0A - 10mA': 0,
                               '10mA - 30mA': 1,
                               '30mA - 150mA': 2,
                               '150mA - 300mA': 3,
                               '300mA - 3A': 4,
                               'Auto range': 255 }

        self.dmm_ohm_range = { '0Ω - 160Ω': 0,
                               '160Ω - 330Ω': 1,
                               '330Ω - 890Ω': 2,
                               '890Ω - 1.5kΩ': 3,
                               '1.5kΩ - 10kΩ': 4,
                               '10kΩ - 100kΩ': 5,
                               '100kΩ - 470kΩ': 6,
                               '470kΩ - 1MΩ': 7,
                               'Auto range': 255 }

        # Connect all ui to the main gui
        self.no_device = NoDevice()                    # dialog ui indicating no device was found
        self.device_found = ScanGui()                  # ui showing the ble devices found
        self.scanning = ScanIndicator()                # wait indicator when scanning ble devices
        self.connecting = ConnectIndicator()           # wait indicator when connecting to pokitmeter
        self.configure_setting = ConfigureSettings()   # ui for MM Service settings
        self.confirm_switch = ConfirmSwitch()          # dialog ui for confirming switch to ammeter mode
        self.app_shutdown = ConfirmExit()              # dialog ui for confirming app shutdown
        self.invalid_device = InvalidDevice()            # dialog ui for handling invalid device

        # Bind callback functions to main UI widgets
        self.ui.button_dc_volt.clicked.connect(self.select_dc_volt)
        self.ui.button_ac_volt.clicked.connect(self.select_ac_volt)
        self.ui.button_dc_amp.clicked.connect(self.select_dc_amp)
        self.ui.button_ac_amp.clicked.connect(self.select_ac_amp)
        self.ui.button_dc_ohm.clicked.connect(self.select_dc_ohm)
        self.ui.button_dc_cont.clicked.connect(self.select_dc_cont)
        self.ui.button_diode.clicked.connect(self.select_diode)
        self.ui.button_temp.clicked.connect(self.select_temp)
        self.ui.button_settings.clicked.connect(self.configure_dmm)
        self.ui.button_close.clicked.connect(self.exit_app)

        # Bind callback functions to Device Found widgets
        self.device_found.ui.listWidget_devices.clicked.connect(self.device_clicked)
        self.device_found.ui.pushButton_rescan.clicked.connect(self.scan_again)

        # Bind callback functions to No Device found widgets
        self.no_device.ui.pushButton_exit.clicked.connect(self.exit_app)
        self.no_device.ui.pushButton_rescan.clicked.connect(self.scan_again)

        # Bind callback functions to Invalid Device found widget
        self.invalid_device.ui.pushButton_exit.clicked.connect(self.exit_app)
        self.invalid_device.ui.pushButton_rescan.clicked.connect(self.scan_again)

        # Bind callback functions to Connecting Indicator widget
        self.connect_device = JobThread(self.conn_device)

        # Bind callback functions to Settings widget
        self.configure_setting.ui.pushButton_ok.clicked.connect(self.close_setting)

        # Bind callback functions to Confirm Ammeter mode widget
        self.confirm_switch.ui.pushButton_switch.clicked.connect(self.switch_clicked)
        self.confirm_switch.ui.pushButton_cancel.clicked.connect(self.switch_cancelled)

        # Bind callback functions to Confirm Exit widget
        self.app_shutdown.ui.pushButton_exit_yes.clicked.connect(self.app_quit)
        self.app_shutdown.ui.pushButton_exit_no.clicked.connect(self.quit_ignore)

        # Create thread for monitoring connection status
        self.flag = 0
        self.connect_flag = VariableFlag()
        self.connect_flag.valueChanged.connect(self.connect_successful)

        # Create thread for checking device manufacturer
        self.flag_id= VariableFlag()
        self.flag_id.valueChanged.connect(self.check_invalid)

        # Create thread for monitoring results update
        self.result= VariableFlag()
        self.result.valueChanged.connect(self.update_result)

        # Initialized scanning
        self.scan_device = JobThread(self.scan_now)
        self.scan_device.signal.connect(self.scan_finished)
        self.scanning.show()
        self.scan_device.start()

    # Basic UI functions -----------------------------------------------------------------------------------------------
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def scan_now(self):
        """ Get BLE address and device name from available BLE advertisement

        :return: list of ble devices
        """
        async def ble_scan():
            devices = await discover()
            dev_list = []
            for dev in devices:
                dev_list.append(str(dev))
            return dev_list
        loop = asyncio.new_event_loop()
        devices = loop.run_until_complete(ble_scan())
        loop.close()
        self.parse_address(devices)

    def parse_address(self, devices):
        """ Parse and store data of BLE devices on a dictionary where the device name is the key
            and BLE address is the value
        :param devices: list of devices

        :return: None
        """
        for dev in devices:
            dev  = dev.split(' ')
            addr = dev[0].strip().strip(':')
            dev  = ''.join([s.strip() for s in dev[1:]])
            self.devices[dev] = addr

    def parse_data(self):
        """ Select range based on mode

        :return: None
        """
        if self.mode in (1, 2):
            self.range = self.dmm_volt_range[self.volt_range]
        elif self.mode in (3, 4):
            self.range = self.dmm_amp_range[self.amp_range]
        elif self.mode == 5:
            self.range = self.dmm_ohm_range[self.ohm_range]
        else:
            self.range = 255

        # Byte conversion using struct
        s = struct.Struct('=' + 'B B I')
        write_data = s.pack(self.mode, self.range, self.interval)
        write_data = write_data.rstrip(b' ')
        self.write_data = write_data.rstrip(b'\x00')

    def device_clicked(self):
        """ Select the ble device found during scanning

        :return: None
        """
        item = self.device_found.ui.listWidget_devices.currentItem()
        self.current_device = self.devices[item.text().strip()]
        self.device_found.close()
        self.connecting.show()
        self.connect_device.start()

    def check_invalid(self):
        """ Function to handle invalid device

        :return: None
        """
        self.connecting.close()
        self.invalid_device.show()
        self.flag = True

        # Re-initialize flags
        self.flag_id.blockSignals(True)
        self.connect_flag.blockSignals(True)
        self.flag_id.variable = 0
        self.connect_flag.variable = 0
        time.sleep(0.01)
        self.flag_id.blockSignals(False)
        self.connect_flag.blockSignals(False)

    def scan_again(self):
        """ Re-launches thread for re-scanning

        :return: None
        """
        self.invalid_device.close()
        self.device_found.close()
        self.no_device.close()
        self.scanning.show()
        self.scan_device.start()

    def scan_finished(self):
        """ Callback function for scanning, launches found devices' list

        :return: None
        """
        self.scanning.close()
        if self.devices == {}:
            self.no_device.show()
        else:
            self.device_found.add_item(self.devices)
            self.device_found.show()

    def conn_device(self):
        """ Thread for establishing connection to selected BLE device, once connected it will continuously read values
            for the selected mode.

        :return: None
        """
        async def conn(address, loop, self):

            # Use Pybleak to access GATT
            async with BleakClient(address, loop=loop) as client:
                x = await client.is_connected()
                if x:
                    read_id = bytes(await client.read_gatt_char(self.man_uuid))
                    # print(read_id)
                    if self.man_id != read_id.decode():
                        self.flag_id.variable = True

                        # Disconnect invalid device and exit function
                        await client.disconnect()
                        return

                    self.connect_flag.variable = True
                time.sleep(0.2)

                for service in client.services:
                    if service.uuid == self.mm_service:
                        while True:
                            if not await client.is_connected():
                                self.lcd_display.setText('- - - - - -')
                                self.connect_flag.blockSignals(True)
                                self.connect_flag.variable = 0
                                time.sleep(0.01)
                                self.connect_flag.blockSignals(False)
                                break

                            self.parse_data()
                            # print('mode: ', self.mode)
                            # print('range: ', self.range)
                            await client.write_gatt_char(self.write_uuid, self.write_data, True)

                            try:
                                value = bytes(await client.read_gatt_char(self.read_uuid))
                                self.read_data = struct.unpack('f', value[1:5])[0]
                                # print(self.read_data)
                                self.result.variable = self.read_data
                            except:
                                pass

        loop = asyncio.new_event_loop()
        self.flag = False

        # Try connecting to device until it succeed
        while not self.flag:
            try:
                loop.run_until_complete(conn(self.current_device, loop, self))
            except:
                time.sleep(0.02)

    def connect_successful(self):
        """ Callback function for connecting, launches main UI

        :return: None
        """
        self.flag = True
        self.connecting.close()
        self.select_dc_volt()
        self.show()

    def volt_reading(self):
        """ Set format for voltage mode

        :return: reading with suffix
        """
        if self.read_data < 1:
            return '{:0.3f} mV'.format(self.read_data * 1e3)
        else:
            return '{:0.3f} V'.format(self.read_data)

    def amp_reading(self):
        """ Set format for current mode

        :return: reading with suffix
        """
        if self.read_data < 1:
            return '{:0.3f} mA'.format(self.read_data * 1e3)
        else:
            return '{:0.3f} A'.format(self.read_data)

    def ohm_reading(self):
        """ Set format for resistance mode

        :return: reading with suffix
        """
        if self.read_data < 1e3:
            return '{:0.3f} Ω'.format(self.read_data)
        elif 1e3 < self.read_data < 1e6:
            return '{:0.3f} kΩ'.format(self.read_data / 1e3)
        else:
            return '{:0.3f} MΩ'.format(self.read_data / 1e6)

    def diode_reading(self):
        """ Set format for diode measurement

        :return: reading with suffix
        """
        if self.read_data < 1:
            return '{:0.3f} mV'.format(self.read_data * 1e3)
        elif 1 < self.read_data < 1e3:
            return '{:0.3f} V'.format(self.read_data)
        elif 1e3 < self.read_data < 1e6:
            return '{:0.3f} kV'.format(self.read_data / 1e3)
        else:
            return '{:0.3f} MV'.format(self.read_data / 1e6)

    def cont_reading(self):
        """ Set format for continuity mode

        :return: reading
        """
        return '{:0.3f}'.format(self.read_data)

    def temp_reading(self):
        """ Set format for temperature mode

        :return: reading with suffix
        """
        if self.temp_deg == 'Celsius':
            return '{:0.3f} °C'.format(self.read_data)
        else:
            return '{:0.3f} °F'.format(self.celsius_to_fahrenheit(self.read_data))

    def update_result(self):
        """ Callback function to update display reading when value changes

        :return: None
        """
        mm_mode = {1: self.volt_reading,
                   2: self.volt_reading,
                   3: self.amp_reading,
                   4: self.amp_reading,
                   5: self.ohm_reading,
                   6: self.diode_reading,
                   7: self.cont_reading,
                   8: self.temp_reading }

        self.ui.lcd_display.setText(' ')
        self.ui.lcd_display.setText(mm_mode[self.mode]())
        self.ui.lcd_display.update()


    def configure_dmm(self):
        """ Shows UI for configuring DMM settings

        :return: None
        """
        self.configure_setting.show()

    def close_setting(self):
        """ Fetch current values from the Setting ui

        :return: None
        """
        self.volt_range = self.configure_setting.ui.comboBox_volt_range.currentText().strip()
        self.amp_range = self.configure_setting.ui.comboBox_amp_range.currentText().strip()
        self.ohm_range = self.configure_setting.ui.comboBox_ohm_range.currentText().strip()
        self.temp_deg = self.configure_setting.ui.comboBox_temp.currentText().strip()
        self.configure_setting.close()

    def celsius_to_fahrenheit(self, c):
        """ Helper function for computing fahrenheit
        :param c: Values in celsius
        :return: fahrenheit value
        """
        return (c * 1.8) + 32

    def switch_clicked(self):
        """ Helper function for selecting AC or DC function

        :return: None
        """
        if len(self.func):
            self.func[-1]()
        self.confirm_switch.close()

    def switch_cancelled(self):
        """ Callback for cancelling Ammeter mode

        :return: None
        """
        self.confirm_switch.close()

    def exit_app(self):
        """ Launch dialog box for exit confirmation

        :return: None
        """
        self.app_shutdown.show()

    def quit_ignore(self):
        """ Closes dialog box and ignore exit

        :return: None
        """
        self.app_shutdown.close()

    def app_quit(self):
        """ Exit routine after exit confirmation

        :return: None
        """
        self.close()
        sys.exit()

#-----------------------------------------------------------------------------------------------------------------------
    # Different Mode Functions
    def select_dc_volt(self):
        """ Set mode for DC voltage and activate ON pixmap

        :return: None
        """
        self.mode = 1
        self.deselect_all()
        self.ui.button_dc_volt.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_dc_volt_on.png);}""")

    def select_ac_volt(self):
        """ Set mode for AC voltage and activate ON pixmap

        :return: None
        """
        self.mode = 2
        self.deselect_all()
        self.ui.button_ac_volt.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_ac_volt_on.png);}""")

    def select_dc_amp(self):
        """ Launches dialog box for confirming Switch to Current and passes DC current mode function

        :return: None
        """
        self.func = [self.select_dc_amp_ok]
        self.confirm_switch.show()

    def select_dc_amp_ok(self):
        """ Set mode for DC current and activate ON pixmap

        :return: None
        """
        self.mode = 3
        self.deselect_all()
        self.ui.button_dc_amp.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_dc_amp_on.png);}""")

    def select_ac_amp(self):
        """ Launches dialog box for confirming Switch to Current and passes AC current mode function

        :return: None
        """
        self.func = [self.select_ac_amp_ok]
        self.confirm_switch.show()

    def select_ac_amp_ok(self):
        """ Set mode for AC current and activate ON pixmap

        :return: None
        """
        self.mode = 4
        self.deselect_all()
        self.ui.button_ac_amp.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_ac_amp_on.png);}""")

    def select_dc_ohm(self):
        """ Set mode for Resistance and activate ON pixmap

        :return: None
        """
        self.mode = 5
        self.deselect_all()
        self.ui.button_dc_ohm.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_dc_ohm_on.png);}""")

    def select_diode(self):
        """ Set mode for Diode and activate ON pixmap

        :return: None
        """
        self.mode = 6
        self.deselect_all()
        self.ui.button_diode.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_diode_on.png);}""")

    def select_dc_cont(self):
        """ Set mode for Continuity and activate ON pixmap

        :return: None
        """
        self.mode = 7
        self.deselect_all()
        self.ui.button_dc_cont.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_dc_cont_on.png);}""")

    def select_temp(self):
        """ Set mode for Temperature and activate ON pixmap

        :return: None
        """
        self.mode = 8
        self.deselect_all()
        self.ui.button_temp.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_temp_on.png);}""")

    def deselect_all(self):
        """ Clears selected button and re-intialize pixmap

        :return: None
        """
        self.ui.button_dc_volt.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_dc_volt_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_dc_volt_on.png)}""")
        self.ui.button_dc_amp.setStyleSheet(""" QPushButton{ border-image: url(:/images/logo_dc_amp_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_dc_amp_on.png)}""")
        self.ui.button_dc_ohm.setStyleSheet(""" QPushButton{ border-image: url(:/images/logo_dc_ohm_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_dc_ohm_on.png)}""")
        self.ui.button_dc_cont.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_dc_cont_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_dc_cont_on.png)}""")
        self.ui.button_ac_volt.setStyleSheet("""QPushButton{ border-image: url(:/images/logo_ac_volt_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_ac_volt_on.png)}""")
        self.ui.button_ac_amp.setStyleSheet(""" QPushButton{ border-image: url(:/images/logo_ac_amp_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_ac_amp_on.png)}""")
        self.ui.button_diode.setStyleSheet("""  QPushButton{ border-image: url(:/images/logo_diode_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_diode_on.png)}""")
        self.ui.button_temp.setStyleSheet("""   QPushButton{ border-image: url(:/images/logo_temp_off.png);}
                                             QPushButton:hover{border-image: url(:/images/logo_temp_on.png)}""")
#-----------------------------------------------------------------------------------------------------------------------

class JobThread(QThread):
    """
        Thread class for performing long process tasks
    """
    signal = pyqtSignal()

    def __init__(self, job):
        QThread.__init__(self)
        self.job = job

    def run(self):
        self.job()
        self.signal.emit()


class VariableFlag(QtWidgets.QWidget):
    """
        Flag class for detecting change in variables
    """
    valueChanged = pyqtSignal(object)

    def __init__(self, parent=None):
        super(VariableFlag, self).__init__(parent)
        self._var = 0

    @property
    def variable(self):
        return self._var

    @variable.setter
    def variable(self, value):
        self._var = value
        self.valueChanged.emit(value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainGui()
    app.exec_()