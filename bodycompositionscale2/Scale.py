#!/usr/bin/env python
from bluepy.btle import Scanner, DefaultDelegate
from time import monotonic

#
# In seconds
DURATION_MEASUREMENT = 5
SCALE_ADDRESS = "5C:CA:D3:5E:65:8E"


class Scale(DefaultDelegate):
    def __init__(self, scale_address):
        DefaultDelegate.__init__(self)
        self.scanner = Scanner(0).withDelegate(self)
        self.scanner.start()
        self.scanner.clear()
        self._first_seen = False
        self.scale_address = scale_address
        self._weight = 0

    def measure(self, timeout):
        self.scanner.scan(timeout)

    @property
    def weight(self):
        return self._weight if self._weight != 0 else None

    def handleDiscovery(self, device, _, is_new_data):
        # `first_seen` is needed because the Scale send at first
        # a saved value.
        if is_new_data and device.addr == self.scale_address.lower():
            if self._first_seen:
                self._weight = (
                    int.from_bytes(
                        bytes.fromhex(device.getValueText(22)[-4:]), "little"
                    )
                    / 200
                )
            else:
                self._first_seen = True


def main():
    scale = Scale(SCALE_ADDRESS)
    timestamp = monotonic()
    while True:
        scale.measure(0.01)
        if monotonic() - timestamp >= DURATION_MEASUREMENT:
            print(f"Gewicht: {scale.weight}")
            break


if __name__ == "__main__":
    main()
