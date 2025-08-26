from abc import ABC
from enum import Enum


class Errors(Enum):
    pass


class LexingError(Errors):
    DOC_IS_NOT_THE_ROOT_ELEM="A DOC element should be the root elemnt"