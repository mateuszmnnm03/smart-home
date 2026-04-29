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

from home.CameraInfo import _home_CameraInfo_t

from home.Camera_forward import _home_CameraPrx_t

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
    from home.CameraInfo import CameraInfo
    from home.Coords import Coords
    from home.DeviceState import DeviceState


class CameraPrx(DevicePrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::home::Camera``.
    """

    def getLocation(self, context: dict[str, str] | None = None) -> Coords:
        return Camera._op_getLocation.invoke(self, ((), context))

    def getLocationAsync(self, context: dict[str, str] | None = None) -> Awaitable[Coords]:
        return Camera._op_getLocation.invokeAsync(self, ((), context))

    def getInfo(self, context: dict[str, str] | None = None) -> CameraInfo:
        return Camera._op_getInfo.invoke(self, ((), context))

    def getInfoAsync(self, context: dict[str, str] | None = None) -> Awaitable[CameraInfo]:
        return Camera._op_getInfo.invokeAsync(self, ((), context))

    def setPosition(self, pan: float, tilt: float, zoom: float, context: dict[str, str] | None = None) -> None:
        return Camera._op_setPosition.invoke(self, ((pan, tilt, zoom), context))

    def setPositionAsync(self, pan: float, tilt: float, zoom: float, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Camera._op_setPosition.invokeAsync(self, ((pan, tilt, zoom), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> CameraPrx | None:
        return checkedCast(CameraPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[CameraPrx | None ]:
        return checkedCastAsync(CameraPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> CameraPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> CameraPrx | None:
        return uncheckedCast(CameraPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Camera"

IcePy.defineProxy("::home::Camera", CameraPrx)

class Camera(Device, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::home::Camera``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::home::Camera", "::home::Device", )
    _op_getLocation: IcePy.Operation
    _op_getInfo: IcePy.Operation
    _op_setPosition: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::home::Camera"

    @abstractmethod
    def getLocation(self, current: Current) -> Coords | Awaitable[Coords]:
        pass

    @abstractmethod
    def getInfo(self, current: Current) -> CameraInfo | Awaitable[CameraInfo]:
        pass

    @abstractmethod
    def setPosition(self, pan: float, tilt: float, zoom: float, current: Current) -> None | Awaitable[None]:
        pass

Camera._op_getLocation = IcePy.Operation(
    "getLocation",
    "getLocation",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _home_Coords_t, False, 0),
    ())

Camera._op_getInfo = IcePy.Operation(
    "getInfo",
    "getInfo",
    OperationMode.Idempotent,
    None,
    (),
    (),
    (),
    ((), _home_CameraInfo_t, False, 0),
    ())

Camera._op_setPosition = IcePy.Operation(
    "setPosition",
    "setPosition",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_float, False, 0), ((), IcePy._t_float, False, 0), ((), IcePy._t_float, False, 0)),
    (),
    None,
    (_home_InvalidValueException_t, _home_DeviceOffException_t))

__all__ = ["Camera", "CameraPrx", "_home_CameraPrx_t"]
