# modbus-register-reader
This script was written for a Modbus temperature-humidity sensor of which the connection parameters (i.e. baud rate, data bit, parity bit & stop bit) were unknown.

### Parameters Known For Device
* Data being searched for (i.e. temperature, humidity) is held in the input registers of the device.
* The count for the registers to be read from is 2 (i.e. data is being read from two registers - one for temperature & one for humidity).
* Starting address of the registers is address 1.
*  Slave unit ID for the device is 1 (by default).

The code can be altered for different devices (e.g. a working three-phase energy meter was used to test the script, which had its data held in the holding registers instead).
Further development can be made to enable the script loop through the starting addresses & unit IDs as well if those are also unknown for the device under consdieration.
