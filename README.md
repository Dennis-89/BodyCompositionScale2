# BodyCompositionScale2
Get the weight from the scale without App

Create virtual environment and install
---------------------

Follow the steps below as an example for how to create a python environment and install `BodyCompositionScale`
Note: You have to use `sudo` because of Bluetooth.
Note: You don't have to use `nano`, you can use your favorite editor. 
Note: Add the "Example Code" below in `reading_scale.py`.
```bash
dennis@test:~ $ mkdir scale_test/src -p
dennis@test:~ $ python -m venv scale_test/.venv
dennis@test:~ $ git clone https://github.com/Dennis-89/BodyCompositionScale2.git scale_test/src/
Cloning into 'scale_test/src'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 10 (delta 1), reused 6 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (10/10), 14.23 KiB | 766.00 KiB/s, done.
Resolving deltas: 100% (1/1), done.
dennis@test:~ $ . scale_test/.venv/bin/activate
(.venv) dennis@test:~ $ cd scale_test/src
(.venv) dennis@test:scale_test/src $ pip install .
(.venv) dennis@test:scale_test/src $ deactivate
dennis@test:scale_test $ cd ..
dennis@test:scale_test $ nano reading_scale.py
dennis@test:scale_test $ sudo .venv/bin/python3 reading_scale.py
```

## Example Code

The following code will measure the weight and show you the last value
after the given duration of measurement.

```python
from time import monotonic

from bodycompositionscale2.Scale import Scale

#
# In seconds
DURATION_MEASUREMENT = 5
SCALE_ADDRESS = "5C:CA:D3:5E:65:8E"

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

```
