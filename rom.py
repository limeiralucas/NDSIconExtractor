from nds.header import NDSHeader
from nds.banner import NDSBanner

from image.func import load_image


class ROM:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = open(filename, "rb")
        self.header = NDSHeader(self.file)
        self.banner = self._get_banner()

    def _get_bytes(self, start: int, end: int) -> bytes:
        return self.mmfile[start:end]

    def _get_banner(self):
        offset = int(self.header.banner_offset.hex(), 16)

        return NDSBanner(self.file, offset)

    def load_image(self, save_location):
        load_image(self.banner.icon, self.banner.palette, save_location)

    def close(self):
        if not self.file.closed:
            self.file.close()
