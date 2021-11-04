import time
import itertools
from pymodbus.client.sync import ModbusSerialClient

baud_rate = [4800, 9600, 14400, 19200, 38400, 56000, 57600, 115200]
data_bit = [7, 8]
parity_bit = ["N", "E", "O"]
stop_bit = [1, 2]

# list of all possible combinations of the parameters above
all_combinations = list(itertools.product(baud_rate, data_bit, parity_bit, stop_bit))
x = 0
while x != -1:
    for index, combo in enumerate(all_combinations):
        baud = combo[0]
        byte = combo[1]
        par = combo[2]
        stop = combo[3]
        print(f"\n for index {index} -- %s %s %s %s" % (baud, byte, par, stop))
        # port varies from computer to computer, check your COM port in your computer's device manager
        client = ModbusSerialClient(method='rtu', port='COM13', stopbits=stop,
                                    bytesize=byte, parity=par, baudrate=baud, timeout=2)

# to determine if device is connected or not
        if not client.connect():
            connection = client.connect()

        connection = client.connect()
        print("\tYour connection is set to", connection)

        if client.connect():
            try:
                read = client.read_input_registers(address=1, count=2, unit=1)
                value = read.registers
                print(value)
                x = -1
                break
            except AttributeError:
                print("\tWrong parameters")
                time.sleep(5)
                continue
        else:
            print("Consider checking your device connection and try again.")
            exit()
