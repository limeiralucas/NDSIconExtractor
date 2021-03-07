from typing.io import BinaryIO

from utils import describe_attr


class NDSHeader:
    def __init__(self, data: BinaryIO):
        self.data = data

        self.game_title = self._get_data(12, reverse=False)
        self.game_code = self._get_data(4, reverse=False)
        self.maker_code = self._get_data(2, reverse=False)

        self.unit_code = self._get_data(1)
        self.device_type = self._get_data(1)
        self.device_size = self._get_data(1)

        # Skip reserved data
        self._get_data(9)

        self.rom_version = self._get_data(1)
        self.flags = self._get_data(1)

        self.arm9_rom_offset = self._get_data(4)
        self.arm9_execute_address = self._get_data(4)
        self.arm9_destination = self._get_data(4)
        self.arm9_binary_size = self._get_data(4)

        self._get_data(56)

        self.banner_offset = self._get_data(4)

    def describe(self) -> str:
        return "\n".join(
            [
                describe_attr(key, value)
                for key, value in vars(self).items()
                if key not in ("data", "banner")
            ],
        )

    def _get_data(self, length: int, seek: int = None, reverse: bool = True) -> bytes:
        if seek:
            self.data.seek(seek)

        data = bytearray(self.data.read(length))

        if reverse:
            data.reverse()

        return bytes(data)
