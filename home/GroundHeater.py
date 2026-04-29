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

from home.GroundHeater_forward import _home_GroundHeaterPrx_t

from home.Heater import Heater
from home.Heater import HeaterPrx

from home.InvalidValueException import _home_InvalidValueException_t

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from Ice.ObjectPrx import ObjectPrx
    from collections.abc import Awaitable
    from collections.abc import Sequence
    from home.DeviceState import DeviceState


class GroundHeaterPrx(HeaterPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::home::GroundHeater``.
    """

    def setFloorMaterial(self, material: str, context: dict[str, str] | None = None) -> None:
        return GroundHeater._op_setFloorMaterial.invoke(self, ((material, ), context))

    def setFloorMaterialAsync(self, material: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        return GroundHeater._op_setFloorMaterial.invokeAsync(self, ((material, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> GroundHeaterPrx | None:
        return checkedCast(GroundHeaterPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[GroundHeaterPrx | None ]:
        return checkedCastAsync(GroundHeaterPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> GroundHeaterPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> GroundHeaterPrx | None:
        return uncheckedCast(GroundHeaterPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::home::GroundHeater"

IcePy.defineProxy("::home::GroundHeater", GroundHeaterPrx)

class GroundHeater(Heater, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::home::GroundHeater``.
    """

    _ice_ids: Sequence[str] = ("::Ice::Object", "::home::Device", "::home::GroundHeater", "::home::Heater", )
    _op_setFloorMaterial: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::home::GroundHeater"

    @abstractmethod
    def setFloorMaterial(self, material: str, current: Current) -> None | Awaitable[None]:
        pass

GroundHeater._op_setFloorMaterial = IcePy.Operation(
    "setFloorMaterial",
    "setFloorMaterial",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    None,
    ())

__all__ = ["GroundHeater", "GroundHeaterPrx", "_home_GroundHeaterPrx_t"]
