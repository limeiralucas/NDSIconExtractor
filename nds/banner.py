from typing.io import BinaryIO

from utils import describe_attr


class NDSBanner:
    def __init__(self, data: BinaryIO, start: int):
        self.data = data
        self.data.seek(start)

        self.version = self._get_data(2)
        self.crc = self._get_data(2)

        # Skip reserved area
        self._get_data(28)

        self.icon = self._get_data(512, reverse=False)
        self.palette = self._get_data(32, reverse=False)
        self.fix_palette()

    def fix_palette(self):
        new_palette = []
        index = 0
        while index < len(self.palette):
            value = self.palette[index]
            next_value = self.palette[index + 1]

            value = next_value << 8 | value

            new_palette.append(value)
            index += 2

        self.palette = new_palette

    def describe(self) -> str:
        return "\n".join(
            [
                self._custom_describe(key, value)
                for key, value in vars(self).items()
                if key != "data"
            ],
        )

    def _get_data(self, length: int, seek: int = None, reverse: bool = True) -> bytes:
        if seek:
            self.data.seek(seek)

        data = bytearray(self.data.read(length))

        if reverse:
            data.reverse()

        return bytes(data)

    def _custom_describe(self, attr: str, value: bytes):
        filtered_attrs = {
            "icon": {"hide_hex": True},
            "palette": {"hide_hex": True},
        }

        if attr not in filtered_attrs:
            return describe_attr(attr, value)
        else:
            hex_value = (
                value.hex() if not filtered_attrs[attr].get("hide_hex") else "<hex>"
            )
            return f"{attr}: {hex_value} ({len(value)}) |"
