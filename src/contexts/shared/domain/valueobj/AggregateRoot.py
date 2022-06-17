from abc import abstractmethod, ABC
from typing import List, NoReturn

from src.contexts.shared.domain.DomainEvent import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self.__domain_events: List[DomainEvent] = []

    @abstractmethod
    def to_primitives(self) -> dict:
        raise NotImplementedError()

    def record_event(self, event: DomainEvent) -> NoReturn:
        self.__domain_events.append(event)
