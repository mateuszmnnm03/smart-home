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

from home.Device import Device
from home.Device import DevicePrx

from home.DeviceOffException import _home_DeviceOffException_t

from home.DeviceState import _home_DeviceState_t

from home.Heater_forward import _home_HeaterPrx_t

from home.InvalidValueException import _home_InvalidValueException_t

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from Ice.ObjectPrx import ObjectPrx
    from collections.abc import Awaitable
    from collections.abc import Sequence
    from home.DeviceState import DeviceState


class HeaterPrx(DevicePrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::home::Heater``.
    """

    def getTemperature(self, context: dict[str, str] | None = None) -> float:
        return Heater._op_getTemperature.invoke(self, ((), context))

    def getTemperatureAsync(self, context: dict[str, str] | None = None) -> Awaitable[float]:
        return Heater._op_getTemperature.invokeAsync(self, ((), context))

    def setTemperature(self, value: float, context: dict[str, str] | None = None) -> None:
        return Heater._op_setTemperature.invoke(self, ((value, ), context))

    def setTemperatureAsync(self, value: float, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Heater._op_setTemperature.invokeAsync(self, ((value, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> HeaterPrx | None:
        return checkedCast(HeaterPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[HeaterPrx | None ]:
        return checkedCastAsync(HeaterPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> HeaterPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> HeaterPrx | None:
        return uncheckedCast(HeaterPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Heater"

IcePy.defineProxy("::home::Heater", HeaterPrx)

class Heater(Device, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::home::Heater``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::home::Device", "::home::Heater", )
    _op_getTemperature: IcePy.Operation
    _op_setTemperature: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Heater"

    @abstractmethod
    def getTemperature(self, current: Current) -> float | Awaitable[float]:
        pass

    @abstractmethod
    def setTemperature(self, value: float, current: Current) -> None | Awaitable[None]:
        pass

Heater._op_getTemperature = IcePy.Operation(
    "getTemperature",
    "getTemperature",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_float, False, 0),
    ())

Heater._op_setTemperature = IcePy.Operation(
    "setTemperature",
    "setTemperature",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_float, False, 0),),
    (),
    None,
    (_home_InvalidValueException_t, _home_DeviceOffException_t))

__all__ = ["Heater", "HeaterPrx", "_home_HeaterPrx_t"]
