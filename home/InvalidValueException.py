# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Ice.UserException import UserException

from dataclasses import dataclass


@dataclass
class InvalidValueException(UserException):
    """
    Notes
    -----
        The Slice compiler generated this exception dataclass from Slice exception ``::home::InvalidValueException``.
    """
    message: str = ""

    _ice_id = "::home::InvalidValueException"

_home_InvalidValueException_t = IcePy.defineException(
    "::home::InvalidValueException",
    InvalidValueException,
    (),
    None,
    (("message", (), IcePy._t_string, False, 0),))

setattr(InvalidValueException, '_ice_type', _home_InvalidValueException_t)

__all__ = ["InvalidValueException", "_home_InvalidValueException_t"]
