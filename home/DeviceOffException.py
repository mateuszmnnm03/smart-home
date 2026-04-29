# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Ice.UserException import UserException

from dataclasses import dataclass


@dataclass
class DeviceOffException(UserException):
    """
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::home::DeviceOffException``.
    """

    _ice_id = "::home::DeviceOffException"

_home_DeviceOffException_t = IcePy.defineException(
    "::home::DeviceOffException",
    DeviceOffException,
    (),
    None,
    ())

setattr(DeviceOffException, '_ice_type', _home_DeviceOffException_t)

__all__ = ["DeviceOffException", "_home_DeviceOffException_t"]
