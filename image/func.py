from PIL import Image

from image.pixel import Pixel


def load_image(icon_data: bytes, palette: bytes, location: str):
    image = [[Pixel() for x in range(32)] for y in range(32)]

    for index, double_pixel in enumerate(icon_data):
        upper = (double_pixel & 0xF0) >> 4
        lower = double_pixel & 0x0F

        y = ((index // 4) % 8) + (index // 128) * 8
        x = (((index * 2) % 8) + (index // 32) * 8) % 32

        image[y][x + 1] = Pixel.from_ds(palette[upper])
        image[y][x] = Pixel.from_ds(palette[lower])

    img_file = Image.new("RGBA", (32, 32), (255, 255, 255, 255))
    img = img_file.load()
    for r in range(len(image)):
        for c in range(len(image[r])):
            img[c, r] = image[r][c].to_tuple()

    img_file.save(location)
