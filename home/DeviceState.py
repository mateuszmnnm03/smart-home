# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from enum import Enum

class DeviceState(Enum):
    """
    Notes
    -----
        The Slice compiler generated this enum class from Slice enumeration ``::home::DeviceState``.
    """

    ON = 0

    OFF = 1

    ERROR = 2

_home_DeviceState_t = IcePy.defineEnum(
    "::home::DeviceState",
    DeviceState,
    (),
    {
        0: DeviceState.ON,
        1: DeviceState.OFF,
        2: DeviceState.ERROR,
    }
)

__all__ = ["DeviceState", "_home_DeviceState_t"]
