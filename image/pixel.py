class Pixel:
    def __init__(self):
        self.red = 255
        self.green = 255
        self.blue = 255
        self.alpha = 0

    def to_tuple(self):
        return (
            self.red,
            self.green,
            self.blue,
            self.alpha,
        )

    @staticmethod
    def from_ds(ds_pixel: hex):
        pixel = Pixel()
        pixel.red = ds_pixel & 0x1F
        pixel.green = (ds_pixel >> 10) & 0x1F
        pixel.blue = (ds_pixel >> 5) & 0x1F

        pixel.red = (pixel.red << 3) + (pixel.red >> 2)
        pixel.green = (pixel.green << 3) + (pixel.green >> 2)
        pixel.blue = (pixel.blue << 3) + (pixel.blue >> 2)

        pixel.alpha = 255 if ds_pixel else 0

        return pixel
