import json
import struct
from pathlib import Path

from jsonschema import validate

from .packet import Packet, PacketType

PACKET_LENGTH = 4  # 4 bytes is just over 4GB, sufficient for most cases

BASE_PACKET_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "type": {
            "type": "integer",
            "enum": [0, 1, 2]
        },
        "id": {
            "type": "string"
        },
        "message": {
            "type": "string"
        },
        "body": {
            "type": "object"
        }
    },
    "required": ["type", "id", "message", "body"]
}


def load_packet_schema(file: Path) -> dict:
    try:
        with file.open("r") as f:
            packet_schema = json.load(f)
            return packet_schema

    except FileNotFoundError:
        with file.open("w") as f:
            json.dump(BASE_PACKET_SCHEMA, f)
        return BASE_PACKET_SCHEMA


def validate_packet(packet: Packet, schema: dict) -> None:
    """
    Validates a `Packet` object against a given schema.

    Parameters
    ----------
    packet : Packet
        The `Packet` object to validate.
    schema : dict
         The JSON schema used for validation.

    Raises
    ------
    jsonschema.exceptions.ValidationError
        If the packet does not conform to the schema.
    """
    validate_dict_packet(packet.as_dict(), schema)


def validate_dict_packet(dict_packet: dict, schema: dict) -> None:
    """
    Validates a dictionary representation of a `Packet` object against a schema.

    Parameters
    ----------
    dict_packet : dict
        The dictionary representation of a packet.
    schema : dict
        The JSON schema used for validation.

    Raises
    ------
    jsonschema.exceptions.ValidationError
        If the dictionary does not conform to the schema.
    """
    validate(dict_packet, schema)


def packet_to_struct_packet_bytes(packet: Packet):
    """
    Converts a `Packet` object into a byte stream with a prefixed length.

    Parameters
    ----------
    packet : Packet
        The `Packet` object to convert.

    Returns
    -------
    bytes
        A byte stream that includes the packet's length (4 bytes) followed by the packet data.
    """
    return dict_packet_to_struct_packet_bytes(packet.as_dict())


def dict_packet_to_struct_packet_bytes(dict_packet: dict) -> bytes:
    """
    Converts a dictionary representation of a `Packet` object into a byte stream with a prefixed length.

    Parameters
    ----------
    dict_packet : dict
        The dictionary representation of a packet.

    Returns
    -------
    bytes
        A byte stream that includes the packet's length (4 bytes) followed by the packet data.
    """
    packet_str = json.dumps(dict_packet)
    bytes_packet = packet_str.encode()
    packet_struct_length = struct.pack(">I", len(bytes_packet))  # 4-byte length prefix
    return packet_struct_length + bytes_packet


def get_packet_length(packet_struct_length: bytes) -> int:
    """
    Extracts the packet length from the first 4 bytes of the byte stream.

    Parameters
    ----------
    packet_struct_length : bytes
        The first 4 bytes representing the length of the packet.

    Returns
    -------
    int
        The length of the packet in bytes.
    """
    return struct.unpack("!I", packet_struct_length)[0]  # Unpack 4-byte length


def packet_from_bytes(bytes_packet: bytes) -> Packet:
    return packet_from_str(bytes_packet.decode())


def packet_from_str(str_packet: str) -> Packet:
    dict_packet = json.loads(str_packet)
    dict_packet["type"] = PacketType(dict_packet["type"])
    return Packet(**dict_packet)
