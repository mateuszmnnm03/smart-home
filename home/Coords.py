# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from dataclasses import dataclass


@dataclass
class Coords:
    """
    Notes
    -----
        The Slice compiler generated this dataclass from Slice struct ``::home::Coords``.
    """
    x: float = 0.0
    y: float = 0.0

_home_Coords_t = IcePy.defineStruct(
    "::home::Coords",
    Coords,
    (),
    (
        ("x", (), IcePy._t_float),
        ("y", (), IcePy._t_float)
    ))

__all__ = ["Coords", "_home_Coords_t"]
