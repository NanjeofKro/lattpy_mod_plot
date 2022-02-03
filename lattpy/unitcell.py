# coding: utf-8
#
# This code is part of lattpy.
#
# Copyright (c) 2022, Dylan Jones
#
# This code is licensed under the MIT License. The copyright notice in the
# LICENSE file in the root directory and this permission notice shall
# be included in all copies or substantial portions of the Software.

"""Objects for representing atoms and the unitcell of a lattice."""

import itertools
from collections import abc
from typing import Union, Any, Iterator, Dict

__all__ = ["Atom"]


class Atom(abc.MutableMapping):
    """Object representing an atom of a bravais lattice."""

    _counter = itertools.count()

    __slots__ = ["_index", "_name", "_weight", "_params"]

    def __init__(self, name: str = None, weight: float = 1.0, color: str = None,
                 size: int = 10, **kwargs):
        super().__init__()
        index = next(Atom._counter)
        self._index = index
        self._name = name or str(index)
        self._weight = weight
        self._params = dict(color=color, size=size, **kwargs)

    @property
    def id(self):
        return id(self)

    @property
    def index(self) -> int:
        """Return the index of the ``Atom`` instance."""
        return self._index

    @property
    def name(self) -> str:
        """Return the name of the ``Atom`` instance."""
        return self._name

    @property
    def weight(self):
        """Return the weight or the ``Atom`` instance."""
        return self._weight

    def dict(self) -> Dict[str, Any]:
        """Returns the data of the ``Atom`` instance as a dictionary."""
        data = dict(index=self._index, name=self._name)
        data.update(self._params)
        return data

    def copy(self) -> 'Atom':
        """Creates a deep copy of the ``Atom`` instance."""
        return Atom(self.name, self.weight, **self._params.copy())

    def get(self, key: str, default=None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def is_identical(self, other: 'Atom') -> bool:
        """Checks if the other ``Atom`` is identical to this one."""
        return self._name == other.name

    def __len__(self) -> int:
        """Return the length of the ``Atom`` attributes."""
        return len(self._params)

    def __iter__(self) -> Iterator[str]:
        """Iterate over the keys of the ``Atom`` attributes."""
        return iter(self._params)

    def __getitem__(self, key: str) -> Any:
        """Make ``Atom`` attributes accessable as dictionary items."""
        return self._params[key]

    def __setitem__(self, key: str, value: Any) -> None:
        """Make ``Atom`` attributes accessable as dictionary items."""
        self._params[key] = value

    def __delitem__(self, key: str) -> None:
        """Make ``Atom`` attributes accessable as dictionary items."""
        del self._params[key]

    def __getattribute__(self, key: str) -> Any:
        """Make ``Atom`` attributes accessable as attributes."""
        key = str(key)
        if not key.startswith("_") and key in self._params.keys():
            return self._params[key]
        else:
            return super().__getattribute__(key)

    def __setattr__(self, key: str, value: Any) -> None:
        """Make ``Atom`` attributes accessable as attributes."""
        key = str(key)
        if not key.startswith("_") and key in self._params.keys():
            self._params[key] = value
        else:
            super().__setattr__(key, value)

    def __hash__(self) -> hash:
        """Make ``Atom`` instance hashable."""
        return hash(self._name)

    def __dict__(self) -> Dict[str, Any]:  # pragma: no cover
        """Return the information of the atom as a dictionary"""
        return self.dict()

    def __copy__(self) -> 'Atom':  # pragma: no cover
        """Creates a deep copy of the ``Atom`` instance."""
        return self.copy()

    def __eq__(self, other: Union['Atom', str]) -> bool:
        if isinstance(other, Atom):
            return self.is_identical(other)
        else:
            return self._name == other

    def __repr__(self) -> str:
        argstr = f"{self._name}"
        paramstr = ", ".join(f"{k}={v}" for k, v in self._params.items() if v)
        if paramstr:
            argstr += ", " + paramstr
        return f"Atom({argstr}, {self.index})"
