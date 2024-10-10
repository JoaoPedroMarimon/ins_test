from dataclasses import dataclass
from enum import Enum


class PacketType(Enum):
    REQUEST = 0
    RESPONSE = 1
    NOTIFICATION = 2


@dataclass
class Packet:
    id: str
    type: PacketType
    message: str
    body: dict

    def as_dict(self):
        return {"id": self.id, "type": self.type.value,
                "message": self.message, "body": self.body}

    def notification(self) -> bool:
        return self.type == PacketType.NOTIFICATION

    def request(self) -> bool:
        return self.type == PacketType.REQUEST

    def response(self) -> bool:
        return self.type == PacketType.RESPONSE
