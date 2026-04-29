# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from dataclasses import dataclass
from dataclasses import field

from home.CleaningMode import CleaningMode
from home.CleaningMode import _home_CleaningMode_t

from home.Coords import Coords
from home.Coords import _home_Coords_t


@dataclass
class CleanerInfo:
    """
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::home::CleanerInfo``.
    """
    location: Coords = field(default_factory=Coords)
    mode: CleaningMode = CleaningMode.SILENT

_home_CleanerInfo_t = IcePy.defineStruct(
    "::home::CleanerInfo",
    CleanerInfo,
    (),
    (
        ("location", (), _home_Coords_t),
        ("mode", (), _home_CleaningMode_t)
    ))

__all__ = ["CleanerInfo", "_home_CleanerInfo_t"]
