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

from home.Cleaner_forward import _home_CleanerPrx_t

from home.CleaningMode import _home_CleaningMode_t

from home.Coords import _home_Coords_t

from home.Device import Device
from home.Device import DevicePrx

from home.DeviceOffException import _home_DeviceOffException_t

from home.DeviceState import _home_DeviceState_t

from home.InvalidValueException import _home_InvalidValueException_t

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from Ice.ObjectPrx import ObjectPrx
    from collections.abc import Awaitable
    from collections.abc import Sequence
    from home.CleaningMode import CleaningMode
    from home.Coords import Coords
    from home.DeviceState import DeviceState


class CleanerPrx(DevicePrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::home::Cleaner``.
    """

    def getMode(self, context: dict[str, str] | None = None) -> CleaningMode:
        return Cleaner._op_getMode.invoke(self, ((), context))

    def getModeAsync(self, context: dict[str, str] | None = None) -> Awaitable[CleaningMode]:
        return Cleaner._op_getMode.invokeAsync(self, ((), context))

    def getLocation(self, context: dict[str, str] | None = None) -> Coords:
        return Cleaner._op_getLocation.invoke(self, ((), context))

    def getLocationAsync(self, context: dict[str, str] | None = None) -> Awaitable[Coords]:
        return Cleaner._op_getLocation.invokeAsync(self, ((), context))

    def setMode(self, mode: CleaningMode, context: dict[str, str] | None = None) -> None:
        return Cleaner._op_setMode.invoke(self, ((mode, ), context))

    def setModeAsync(self, mode: CleaningMode, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Cleaner._op_setMode.invokeAsync(self, ((mode, ), context))

    def returnToBase(self, context: dict[str, str] | None = None) -> None:
        return Cleaner._op_returnToBase.invoke(self, ((), context))

    def returnToBaseAsync(self, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Cleaner._op_returnToBase.invokeAsync(self, ((), context))

    def moveToLocation(self, location: Coords, context: dict[str, str] | None = None) -> None:
        return Cleaner._op_moveToLocation.invoke(self, ((location, ), context))

    def moveToLocationAsync(self, location: Coords, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Cleaner._op_moveToLocation.invokeAsync(self, ((location, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> CleanerPrx | None:
        return checkedCast(CleanerPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[CleanerPrx | None ]:
        return checkedCastAsync(CleanerPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> CleanerPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> CleanerPrx | None:
        return uncheckedCast(CleanerPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Cleaner"

IcePy.defineProxy("::home::Cleaner", CleanerPrx)

class Cleaner(Device, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::home::Cleaner``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::home::Cleaner", "::home::Device", )
    _op_getMode: IcePy.Operation
    _op_getLocation: IcePy.Operation
    _op_setMode: IcePy.Operation
    _op_returnToBase: IcePy.Operation
    _op_moveToLocation: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Cleaner"

    @abstractmethod
    def getMode(self, current: Current) -> CleaningMode | Awaitable[CleaningMode]:
        pass

    @abstractmethod
    def getLocation(self, current: Current) -> Coords | Awaitable[Coords]:
        pass

    @abstractmethod
    def setMode(self, mode: CleaningMode, current: Current) -> None | Awaitable[None]:
        pass

    @abstractmethod
    def returnToBase(self, current: Current) -> None | Awaitable[None]:
        pass

    @abstractmethod
    def moveToLocation(self, location: Coords, current: Current) -> None | Awaitable[None]:
        pass

Cleaner._op_getMode = IcePy.Operation(
    "getMode",
    "getMode",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _home_CleaningMode_t, False, 0),
    ())

Cleaner._op_getLocation = IcePy.Operation(
    "getLocation",
    "getLocation",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _home_Coords_t, False, 0),
    ())

Cleaner._op_setMode = IcePy.Operation(
    "setMode",
    "setMode",
    OperationMode.Normal,
    None,
    (),
    (((), _home_CleaningMode_t, False, 0),),
    (),
    None,
    (_home_DeviceOffException_t,))

Cleaner._op_returnToBase = IcePy.Operation(
    "returnToBase",
    "returnToBase",
    OperationMode.Normal,
    None,
    (),
    (),
    (),
    None,
    (_home_DeviceOffException_t,))

Cleaner._op_moveToLocation = IcePy.Operation(
    "moveToLocation",
    "moveToLocation",
    OperationMode.Normal,
    None,
    (),
    (((), _home_Coords_t, False, 0),),
    (),
    None,
    (_home_DeviceOffException_t, _home_InvalidValueException_t))

__all__ = ["Cleaner", "CleanerPrx", "_home_CleanerPrx_t"]
