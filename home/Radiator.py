# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from abc import ABC
from abc import abstractmethod

from home.DeviceOffException import _home_DeviceOffException_t

from home.DeviceState import _home_DeviceState_t

from home.Heater import Heater
from home.Heater import HeaterPrx

from home.InvalidValueException import _home_InvalidValueException_t

from home.Radiator_forward import _home_RadiatorPrx_t

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from Ice.ObjectPrx import ObjectPrx
    from collections.abc import Awaitable
    from collections.abc import Sequence
    from home.DeviceState import DeviceState


class RadiatorPrx(HeaterPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::home::Radiator``.
    """

    def setFanSpeed(self, speed: int, context: dict[str, str] | None = None) -> None:
        return Radiator._op_setFanSpeed.invoke(self, ((speed, ), context))

    def setFanSpeedAsync(self, speed: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Radiator._op_setFanSpeed.invokeAsync(self, ((speed, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> RadiatorPrx | None:
        return checkedCast(RadiatorPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[RadiatorPrx | None ]:
        return checkedCastAsync(RadiatorPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> RadiatorPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> RadiatorPrx | None:
        return uncheckedCast(RadiatorPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Radiator"

IcePy.defineProxy("::home::Radiator", RadiatorPrx)

class Radiator(Heater, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::home::Radiator``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::home::Device", "::home::Heater", "::home::Radiator", )
    _op_setFanSpeed: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Radiator"

    @abstractmethod
    def setFanSpeed(self, speed: int, current: Current) -> None | Awaitable[None]:
        pass

Radiator._op_setFanSpeed = IcePy.Operation(
    "setFanSpeed",
    "setFanSpeed",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    None,
    (_home_InvalidValueException_t, _home_DeviceOffException_t))

__all__ = ["Radiator", "RadiatorPrx", "_home_RadiatorPrx_t"]
