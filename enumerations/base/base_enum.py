from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def values(cls) -> set[str]:
        return {item.value for item in cls}
