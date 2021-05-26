from dataclasses import dataclass, asdict

from voluptuous import Schema, Required, Range, All, REMOVE_EXTRA, MultipleInvalid

DEFAULT_PER_PAGE = 10


@dataclass
class Pagination:
    page: int
    per_page: int
    total_page: int
    count: int
    total_count: int

    @classmethod
    def from_dict(cls, adict=None, **kwargs):
        if adict is None:
            adict = kwargs

        schema = Schema(
            {
                Required("page", default=1): All(int, Range(min=1)),
                Required("per_page", default=DEFAULT_PER_PAGE): All(int, Range(min=1)),
                Required("total_page", default=1): All(int, Range(min=1)),
                Required("count", default=0): int,
                Required("total_count", default=0): int,
            },
            extra=REMOVE_EXTRA,
        )

        try:
            rv = schema(adict)
            return cls(**rv)
        except MultipleInvalid as e:
            raise ValueError(e)

    def to_dict(self):
        return asdict(self)

    @property
    def has_next(self):
        return self.total_page > self.page
