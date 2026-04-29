# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from enum import Enum

class CleaningMode(Enum):
    """
    Notes
    -----
        The Slice compiler generated this enum class from Slice enumeration ``::home::CleaningMode``.
    """

    SILENT = 0

    NORMAL = 1

    TURBO = 2

_home_CleaningMode_t = IcePy.defineEnum(
    "::home::CleaningMode",
    CleaningMode,
    (),
    {
        0: CleaningMode.SILENT,
        1: CleaningMode.NORMAL,
        2: CleaningMode.TURBO,
    }
)

__all__ = ["CleaningMode", "_home_CleaningMode_t"]
