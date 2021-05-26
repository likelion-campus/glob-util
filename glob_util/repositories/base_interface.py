from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from glob_util.domains.pagination import Pagination

DEFAULT_PER_PAGE = 10


class RepoBaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def list(self, filters: dict = {}, sort: dict = {}) -> List:
        pass

    @abstractmethod
    def paginate(
            self,
            page: int = 1,
            per_page: int = DEFAULT_PER_PAGE,
            filters: dict = {},
            sort: dict = {},
    ) -> Tuple[List, Pagination]:
        pass

    @abstractmethod
    def get(self, item_id):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, item_id, **kwargs):
        pass

    @abstractmethod
    def remove(self, item_id) -> bool:
        pass
