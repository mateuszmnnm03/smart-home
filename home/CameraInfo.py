# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from dataclasses import dataclass
from dataclasses import field

from home.Coords import Coords
from home.Coords import _home_Coords_t


@dataclass
class CameraInfo:
    """
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::home::CameraInfo``.
    """
    location: Coords = field(default_factory=Coords)
    pan: float = 0.0
    tilt: float = 0.0
    zoom: float = 0.0

_home_CameraInfo_t = IcePy.defineStruct(
    "::home::CameraInfo",
    CameraInfo,
    (),
    (
        ("location", (), _home_Coords_t),
        ("pan", (), IcePy._t_float),
        ("tilt", (), IcePy._t_float),
        ("zoom", (), IcePy._t_float)
    ))

__all__ = ["CameraInfo", "_home_CameraInfo_t"]
