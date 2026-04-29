# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Ice.Object import Object

from Ice.ObjectPrx import ObjectPrx
from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from abc import ABC
from abc import abstractmethod

from home.DeviceState import _home_DeviceState_t

from home.Device_forward import _home_DevicePrx_t

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from collections.abc import Awaitable
    from collections.abc import Sequence
    from home.DeviceState import DeviceState


class DevicePrx(ObjectPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::home::Device``.
    """

    def getName(self, context: dict[str, str] | None = None) -> str:
        return Device._op_getName.invoke(self, ((), context))

    def getNameAsync(self, context: dict[str, str] | None = None) -> Awaitable[str]:
        return Device._op_getName.invokeAsync(self, ((), context))

    def getState(self, context: dict[str, str] | None = None) -> DeviceState:
        return Device._op_getState.invoke(self, ((), context))

    def getStateAsync(self, context: dict[str, str] | None = None) -> Awaitable[DeviceState]:
        return Device._op_getState.invokeAsync(self, ((), context))

    def turnOn(self, context: dict[str, str] | None = None) -> None:
        return Device._op_turnOn.invoke(self, ((), context))

    def turnOnAsync(self, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Device._op_turnOn.invokeAsync(self, ((), context))

    def turnOff(self, context: dict[str, str] | None = None) -> None:
        return Device._op_turnOff.invoke(self, ((), context))

    def turnOffAsync(self, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Device._op_turnOff.invokeAsync(self, ((), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> DevicePrx | None:
        return checkedCast(DevicePrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[DevicePrx | None ]:
        return checkedCastAsync(DevicePrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> DevicePrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> DevicePrx | None:
        return uncheckedCast(DevicePrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Device"

IcePy.defineProxy("::home::Device", DevicePrx)

class Device(Object, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::home::Device``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::home::Device", )
    _op_getName: IcePy.Operation
    _op_getState: IcePy.Operation
    _op_turnOn: IcePy.Operation
    _op_turnOff: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Device"

    @abstractmethod
    def getName(self, current: Current) -> str | Awaitable[str]:
        pass

    @abstractmethod
    def getState(self, current: Current) -> DeviceState | Awaitable[DeviceState]:
        pass

    @abstractmethod
    def turnOn(self, current: Current) -> None | Awaitable[None]:
        pass

    @abstractmethod
    def turnOff(self, current: Current) -> None | Awaitable[None]:
        pass

Device._op_getName = IcePy.Operation(
    "getName",
    "getName",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), IcePy._t_string, False, 0),
    ())

Device._op_getState = IcePy.Operation(
    "getState",
    "getState",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _home_DeviceState_t, False, 0),
    ())

Device._op_turnOn = IcePy.Operation(
    "turnOn",
    "turnOn",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    None,
    ())

Device._op_turnOff = IcePy.Operation(
    "turnOff",
    "turnOff",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    None,
    ())

__all__ = ["Device", "DevicePrx", "_home_DevicePrx_t"]
