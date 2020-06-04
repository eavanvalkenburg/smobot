"""Class for smobot status."""
"""Example json: {'time': '00:00:00', 'grl': 22, 'fd1': 999, 'fd2': 999, 'err': 999, 'p': 999, 'i': 999, 'd': 999, 'dpr': 999, 'ld': 1, 'set': 220, 'ds': 0, 'sot': 0, 'kp': 110, 'ki': 50, 'kd': 100, 'flg': 0}"""


class SmobotStatus:
    """Class for Smobot status."""

    def __init__(
        self, time, grl, fd1, fd2, err, p, i, d, dpr, ld, set, ds, sot, kp, ki, kd, flg
    ):
        """Initialize a status."""
        self.time = time
        self.grill_temperature = grl
        self._food_probe_1 = fd1
        self._food_probe_2 = fd2
        self.error = err
        self.p = p
        self.i = i
        self.damper_mode = d
        self.damper_state = dpr
        self.open_lid = ld
        self.grill_setpoint = set
        self.ds = ds
        self.sot = sot
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.flg = flg

    @property
    def food_probe_1(self):
        return None if self._food_probe_1 == 999 else self._food_probe_1

    @property
    def food_probe_2(self):
        return None if self._food_probe_2 == 999 else self._food_probe_2

    def __repr__(self):
        gr = f"Grill: {self.grill_temperature}"
        set = f"setpoint: {self.grill_setpoint}"
        dpr = f", damper mode: {self.damper_mode}, damper state: {self.damper_state}" if self.damper_mode != 999 else ""
        fp1 = f", food probe 1: {self._food_probe_1}" if self.food_probe_1 else ""
        fp2 = f", food probe 1: {self._food_probe_2}" if self.food_probe_2 else ""
        return f"{gr}, {set}{dpr}{fp1}{fp2}"
